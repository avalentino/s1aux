"""Sentinel-1 Auxiliary XML data parsing sub-package."""

import re
import enum
import pathlib
import functools
import importlib
from xml.etree import ElementTree as etree

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


@functools.cache
def _get_available_spec_versions():
    def _key_func(s: str):
        assert s[0] == "v"
        return tuple(map(int, s[1:].split("_")))

    package_path = pathlib.Path(__file__).parent
    versions = [d.name for d in package_path.glob("v?_??") if d.is_dir()]
    return tuple(sorted(versions, key=_key_func, reverse=True))


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


class S1AuxParseError(ParserError):
    """Error in S1 AUX file parsing."""


def load(path):
    path = pathlib.Path(path)
    product_type = get_product_type(path.name)

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

    spec_versions = list(_get_available_spec_versions())

    try:
        xmldoc = etree.parse(path)
    except etree.ParseError:
        raise S1AuxParseError(f"unable to parse: '{path}'")

    root = xmldoc.getroot()
    assert root.tag.lower() == xml_type_name.lower(), (
        f"root.tag: {root.tag}, xml_type_name: {xml_type_name}"
    )

    if "schemaVersion" in root.attrib:
        major, minor = root.attrib["schemaVersion"].split(".")
        schema_version = f"v{major}_{minor:>02}"

        if schema_version in spec_versions:
            spec_versions.remove(schema_version)
            spec_versions.insert(0, schema_version)

    for version in spec_versions:
        modname = f".{version}.{product_type.name.lower()}"
        try:
            mod = importlib.import_module(modname, package="s1aux.parse")
            xml_obj_type = getattr(mod, xml_type_name)
        except ImportError:
            pass
        else:
            parser = XmlParser(handler=XmlEventHandler)
            try:
                return parser.parse(xmldoc, xml_obj_type)
            except (ParserError, TypeError):
                pass

    raise S1AuxParseError(f"Unable to load '{path}'")
