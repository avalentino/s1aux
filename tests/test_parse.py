"""Unit tests for the s1aux package."""

import pathlib

import pytest

import s1aux
import s1aux._core

DATADIR = pathlib.Path(__file__).parent / "data"


def test__get_available_spec_versions():
    expected = (
        "v3_12",
        "v3_09",
        "v3_08",
        "v3_07",
        "v3_03",
        "v2_10",
        "v1_06",
        "v1_05",
    )
    data = s1aux._core._get_available_spec_versions()
    assert data == expected


@pytest.mark.parametrize(
    "name",
    [
        "S1A_AUX_CAL_V20190228T092500_G20190227T105149.SAFE",
        "S1A_AUX_INS_V20190228T092500_G20190227T105149.SAFE",
        "S1A_AUX_ITC_V20190228T092500_G20190227T105149.SAFE",
        "S1A_AUX_ML2_V20190228T092500_G20190227T105149.SAFE",
        "S1A_AUX_PP1_V20190228T092500_G20190227T105149.SAFE",
        "S1A_AUX_PP2_V20190228T092500_G20190227T105149.SAFE",
        "S1B_AUX_PP2_V20190228T092500_G20190227T105149.SAFE",
        "S1C_AUX_PP2_V20190228T092500_G20190227T105149.SAFE",
        "S1D_AUX_PP2_V20190228T092500_G20190227T105149.SAFE",
        "S1A_AUX_SCF_V20190228T092500_G20190227T105149.SAFE",
        "S1A_AUX_SCS_V20190228T092500_G20190227T105149.SAFE",
    ],
)
def test__aux_re_match(name):
    assert s1aux._core._AUX_PRODUCT_RE.match(name)


@pytest.mark.parametrize(
    "name",
    [
        "S1E_AUX_CAL_V20190228T092500_G20190227T105149.SAFE",
        "S1A_aux_CAL_V20190228T092500_G20190227T105149.SAFE",
        "S1A_XUA_CAL_V20190228T092500_G20190227T105149.SAFE",
        "S1A_AUX_NOT_V20190228T092500_G20190227T105149.SAFE",
        "S1A_AUX_CAL_v20190228T092500_G20190227T105149.SAFE",
        "S1A_AUX_CAL_V20190228T092500_g20190227T105149.SAFE",
        "S1A_AUX_CAL_V20190228T092500_G20190227T105149.safe",
        "S1A_AUX_CAL_V20190228T092500_G20190227T105149.EXT",
        "S1A_AUX_CAL_V20190228T092500_G20190227T105149",
        "S1A_AUX_CAL_V20190228-092500_G20190227T105149.SAFE",
        "S1A_AUX_CAL_V20190228T092500_G20190227-105149.SAFE",
        "S1A_AUX_CAL_Va0190228T092500_G20190227T105149.SAFE",
        "S1A_AUX_CAL_V20190228Ta92500_G20190227T105149.SAFE",
        "S1A_AUX_CAL_V20190228T092500_Ga0190227T105149.SAFE",
        "S1A_AUX_CAL_V20190228T092500_G20190227Ta05149.SAFE",
        "S1A_AUX_CAL_V2019022T092500_G20190227T105149.SAFE",
        "S1A_AUX_CAL_V20190228T09250_G20190227T105149.SAFE",
        "S1A_AUX_CAL_V20190228T092500_G2019022T105149.SAFE",
        "S1A_AUX_CAL_V20190228T092500_G20190227T10514.SAFE",
    ],
)
def test__aux_re_not_match(name):
    assert not s1aux._core._AUX_PRODUCT_RE.match(name)


@pytest.mark.parametrize(
    "name",
    [
        "S1A_AUX_CAL_V20190228T092500_G20190227T105149.SAFE",
        "S1A_AUX_INS_V20190228T092500_G20190227T105149.SAFE",
        "S1A_AUX_ITC_V20190228T092500_G20190227T105149.SAFE",
        "S1A_AUX_ML2_V20190228T092500_G20190227T105149.SAFE",
        "S1A_AUX_PP1_V20190228T092500_G20190227T105149.SAFE",
        "S1A_AUX_PP2_V20190228T092500_G20190227T105149.SAFE",
        "S1A_AUX_SCF_V20190228T092500_G20190227T105149.SAFE",
        "S1A_AUX_SCS_V20190228T092500_G20190227T105149.SAFE",
    ],
)
def test_get_product_type(name):
    product_type = s1aux.get_product_type(name)
    assert isinstance(product_type, s1aux.EProductType)
    assert product_type.value == name[8:11]


def test_get_product_type_error():
    with pytest.raises(ValueError, match="Sentinel-1"):
        s1aux.get_product_type("invalid")


@pytest.mark.parametrize(
    "path",
    [
        "v1.05/S1__AUX_SCF_V20140406T133000_G20221003T130002.SAFE",
        "v1.05/S1B_AUX_ITC_V20160422T000000_G20221003T125747.SAFE",
        "v1.06/S1A_AUX_ITC_V20160627T000000_G20230330T093840.SAFE",
        "v2.10/S1A_AUX_CAL_V20140915T100000_G20150319T092606.SAFE",
        "v2.10/S1A_AUX_INS_V20140915T100000_G20150319T102820.SAFE",
        "v2.10/S1A_AUX_PP1_V20140915T100000_G20150319T103002.SAFE",
        "v2.10/S1A_AUX_PP2_V20150519T120000_G20150518T150710.SAFE",
        "v3.03/S1A_AUX_PP2_V20190228T092500_G20190227T105149.SAFE",
        "v3.03/S1B_AUX_INS_V20160422T000000_G20180313T094010.SAFE",
        "v3.03/S1B_AUX_PP1_V20160422T000000_G20180313T093244.SAFE",
        "v3.07/S1B_AUX_INS_V20160422T000000_G20211027T134314.SAFE",
        "v3.07/S1B_AUX_PP1_V20160422T000000_G20211027T133747.SAFE",
        "v3.08/S1B_AUX_PP2_V20160422T000000_G20220323T132618.SAFE",
        "v3.09/S1B_AUX_PP2_V20160422T000000_G20240612T131242.SAFE",
        "v3.12/S1B_AUX_PP1_V20160422T000000_G20240423T074411.SAFE",
    ],
)
def test_load(path):
    version, product_name = path.split("/")
    mobj = s1aux._core._AUX_PRODUCT_RE.match(product_name)
    assert mobj is not None
    product_info = mobj.groupdict()
    mission_id = product_info["mission_id"].lower().replace("_", "-")
    product_type = product_info["product_type"].lower()
    path = DATADIR.joinpath(
        path, "data", f"{mission_id}-aux-{product_type}.xml"
    )
    data = s1aux.load(path)
    assert data is not None
    pkg_version = data.__class__.__module__.split(".")[-2]
    assert version == pkg_version.replace("_", ".")


@pytest.mark.parametrize(
    "path",
    [
        "S1A_AUX_ML2_V20190228T092500_G20240429T092326.SAFE",
        "S1__AUX_SCS_V20140406T133000_G20240620T081444.SAFE",
    ],
)
def test_load_not__implemented_error(path):
    with pytest.raises(
        NotImplementedError,
        match="Loading of '(ML2|SCS)' products is still not implemented",
    ):
        s1aux.load(path)


@pytest.mark.parametrize(
    "path", ["S1B_AUX_PP1_V20160422T000000_G20240423T074411.SAFE"]
)
def test_load__file_not_found_error(path):
    with pytest.raises(FileNotFoundError):
        s1aux.load(path)


@pytest.mark.parametrize(
    "path", ["S1B_AUX_PP1_V20160422T000000_G20240423T074411.SAFE"]
)
def test_load__parse_error(path, tmp_path):
    fullpath = tmp_path / path
    fullpath.touch()
    with pytest.raises(s1aux.S1AuxParseError):
        s1aux.load(fullpath)
