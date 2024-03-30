#!/usr/bin/env python3

"""Command line tool for automatic generation of s1a.parse code form XSDs."""

import os
import sys
import shutil
import logging
import pathlib
import subprocess

from typing import Optional, TypedDict, Unpack
from urllib.parse import urlencode, urlparse

import requests

try:
    from os import EX_OK
except ImportError:
    EX_OK = 0
EX_FAILURE = 1
EX_INTERRUPT = 130


SAR_MPC_API_URL = "https://sar-mpc.eu/api/v1"
DEFAULT_QUERY_PARAMS = {
    "sentinel1__mission": "S1A",
    "sentinel1__instr_conf_id": "7",
    "adf__active": "true",
    # "mode": "extended",
}


PathType = str | os.PathLike[str]


class QueryParamsType(TypedDict):
    """Type for query parameters."""

    name: str
    value: str


def query_url(
    url: str = SAR_MPC_API_URL, **kwargs: Unpack[QueryParamsType]
) -> str:
    """Build the query for Sentinel-1 auxiliary products."""
    if len(kwargs) > 0:
        return f"{url}?{urlencode(kwargs)}"
    else:
        return url


def _download(url: str, outfile: Optional[PathType] = None) -> pathlib.Path:
    if outfile is None:
        outfile = pathlib.Path(urlparse(url).path).name
    outfile = pathlib.Path(outfile)
    response = requests.get(url)
    response.raise_for_status()
    outfile.parent.mkdir(parents=True, exist_ok=True)
    outfile.write_bytes(response.content)
    return outfile


def download_aux_products(datadir: PathType = "data") -> pathlib.Path:
    """Download a base set of auxiliary products."""
    query = query_url(**DEFAULT_QUERY_PARAMS)
    response = requests.get(query)
    response.raise_for_status()

    datadir = pathlib.Path(datadir)
    for product in response.json()["results"]:
        url = product["remote_url"]
        outfile = datadir.joinpath(product["physical_name"])
        if not outfile.exists():
            _download(url, outfile=outfile)
            shutil.unpack_archive(outfile, extract_dir=outfile.parent)

    return datadir


def _make_xds_dir(
    datadir: PathType, xsd_dir: PathType = "xsd"
) -> pathlib.Path:
    datadir = pathlib.Path(datadir)
    if not datadir.exists():
        raise FileNotFoundError(str(datadir))

    xsd_files = list(datadir.glob("**/*.xsd"))
    if len(xsd_files) == 0:
        raise FileNotFoundError(f"No XSD files found in {xsd_dir}")

    xsd_dir = pathlib.Path(xsd_dir)
    xsd_dir.mkdir(parents=True)
    for path in xsd_files:
        dst = xsd_dir.joinpath(path.name.removeprefix("s1-aux-"))
        if dst.exists():
            if dst.read_text() != path.read_text():
                raise FileExistsError(
                    f"source ('{path}') and target ('{dst}') files "
                    f"have different content"
                )
        else:
            shutil.copy(path, dst)

    return xsd_dir


def make_cmd(
    xsd_dir: PathType, config_file: PathType = ".xsdata.xml"
) -> list[str]:
    """Generate the command for xsdata execution."""
    config_file = pathlib.Path(config_file)

    cmd = ["xsdata", "-r"]
    if config_file.exists():
        cmd.extend(["-c", os.fspath(config_file)])
    else:
        default_cmd_args = (
            "--relative-imports --include-header "
            "--frozen --slots --kw-only "
            "-ds NumPy "
            "-ss filenames"
        ).split()
        cmd.extend(default_cmd_args)
    cmd.extend(["-p", "s1aux.parse"])
    cmd.append(os.fspath(xsd_dir))

    return cmd


def generate_s1aux_package(
    xsd_dir: PathType,
    outdir: PathType = "s1aux",
    *,
    config_file: PathType = ".xsdata.xml",
    overwrite: bool = False,
    quiet: bool = True,
) -> pathlib.Path:
    """Generate the Python package for s1aux using xsdata and input XSDs."""
    outdir = pathlib.Path(outdir)
    if outdir.exists() and not overwrite:
        raise FileExistsError(outdir)

    cmd = make_cmd(xsd_dir, config_file)

    subprocess.run(cmd, check=True, capture_output=quiet)

    return outdir


def main():
    """Implement the main CLI interface."""
    logging.basicConfig(format="%(levelname)s: %(message)s")
    logging.captureWarnings(True)
    log = logging.getLogger(__name__)

    # execute main tasks
    exit_code = EX_OK
    try:
        datadir = download_aux_products()
        xsd_dir = _make_xds_dir(datadir)
        outdir = generate_s1aux_package(xsd_dir)
        log.info("x1aux package generated in '%s'", outdir)
    except Exception as exc:  # noqa: B902 BLE001
        log.critical(
            "unexpected exception caught: %r %s", type(exc).__name__, exc
        )
        log.debug("stacktrace:", exc_info=True)
        exit_code = EX_FAILURE
    except KeyboardInterrupt:
        log.warning("Keyboard interrupt received: exit the program")
        exit_code = EX_INTERRUPT

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
