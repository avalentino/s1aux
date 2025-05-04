"""Core functions for Sentinel-1 Auxiliary XML data parsing."""

import os
import re
import enum
import pathlib
import functools
import importlib
import contextlib
from xml.etree import ElementTree as etree  # noqa: N813
from collections.abc import Sequence

from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.handlers import XmlEventHandler

_AUX_PRODUCT_RE = re.compile(
    r"(?P<mission_id>S1[ABCD_])_"
    r"AUX_"
    r"(?P<product_type>(CAL|INS|ITC|ML2|PP1|PP2|SCF|SCS))_"
    r"V(?P<validity_start>\d{8}T\d{6})_"
    r"G(?P<generation_date>\d{8}T\d{6})"
    r".SAFE"
)
_AUX_DATAFILE_RE = re.compile(
    r"(?P<mission_id>s1[abcd-])"
    r"-aux-"
    r"(?P<product_type>(cal|ins|itc|pp1|pp2|scf)).xml"
)


class EProductType(enum.Enum):
    """Sentinel-1 Auxiliary product types."""

    CAL = "CAL"
    INS = "INS"
    ITC = "ITC"
    ML2 = "ML2"
    PP1 = "PP1"
    PP2 = "PP2"
    SCF = "SCF"
    SCS = "SCS"


def get_product_type(name: str) -> EProductType:
    """Return the product type corresponding to the input filename."""
    mobj = _AUX_PRODUCT_RE.match(name)
    if not mobj:
        mobj = _AUX_DATAFILE_RE.match(name)
        if not mobj:
            raise ValueError(
                f"{name!r} is not a valid name for datafiles of Sentinel-1 "
                "auxiliary products"
            )
        return EProductType(mobj.group("product_type").upper())
    return EProductType(mobj.group("product_type"))


class S1AuxParseError(ValueError):
    """Error in S1 AUX file parsing."""


def _get_type_name(product_type: EProductType) -> str:
    type_mapping = {
        EProductType.CAL: "AuxiliaryCalibration",
        EProductType.INS: "AuxiliaryInstrument",
        EProductType.ITC: "AuxiliarySetap",
        EProductType.PP1: "L1AuxiliaryProcessorParameters",
        EProductType.PP2: "L2AuxiliaryProcessorParameters",
        EProductType.SCF: "SetapConf",
    }

    try:
        xml_type_name = type_mapping[product_type]
    except KeyError:
        raise NotImplementedError(
            f"Loading of {product_type.name!r} products is still "
            "not implemented"
        ) from None

    return xml_type_name


@functools.cache
def _get_available_spec_versions() -> Sequence[str]:
    def _key_func(version_str: str):
        assert version_str[0] == "v"
        return tuple(map(int, version_str[1:].split("_")))

    package_path = pathlib.Path(__file__).parent
    versions = [d.name for d in package_path.glob("v?_??") if d.is_dir()]
    return tuple(sorted(versions, key=_key_func, reverse=True))


def _get_spec_versions(schema_version: str | None) -> Sequence[str]:
    spec_versions = list(_get_available_spec_versions())
    if schema_version is not None:
        major, minor = schema_version.split(".")
        schema_version = f"v{major}_{minor:>02}"

        if schema_version in spec_versions:
            spec_versions.remove(schema_version)
            spec_versions.insert(0, schema_version)
    return spec_versions


def load(path: os.PathLike[str] | str):
    """Load the Sentinel-1 Auxiliary (AUX) file specified in input.

    The input `path` parameter is expected to be the path to the data
    file in the auxiliary product. E.g.::

      S1A_AUX_INS_V20190228T092500_G20211103T111906.SAFE/data/s1a-aux-ins.xml

    """
    path = pathlib.Path(path)
    product_type = get_product_type(path.name)
    xml_type_name = _get_type_name(product_type)

    try:
        xmldoc = etree.parse(path)
    except etree.ParseError as exc:
        raise S1AuxParseError(f"unable to parse: '{path}'") from exc

    root = xmldoc.getroot()
    assert root.tag.lower() == xml_type_name.lower()

    spec_versions = _get_spec_versions(root.attrib.get("schemaVersion"))

    for version in spec_versions:
        modname = f".{version}.{product_type.name.lower()}"
        try:
            mod = importlib.import_module(modname, package="s1aux")
        except ImportError:
            pass
        else:
            xml_obj_type = getattr(mod, xml_type_name)
            parser = XmlParser(handler=XmlEventHandler)
            with contextlib.suppress(ParserError, TypeError):
                return parser.parse(xmldoc, xml_obj_type)

    raise S1AuxParseError(f"Unable to load '{path}'")
