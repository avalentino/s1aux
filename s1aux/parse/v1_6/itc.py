from dataclasses import dataclass, field
from decimal import Decimal
from typing import Tuple

from .s1_object_types import (
    PolarisationType,
    SwathType,
)


@dataclass(frozen=True, slots=True, kw_only=True)
class InstrumentTimingCalibrationReferenceType:
    """Timing calibration reference parameters SETAP processor.

    This element contains the range and azimuth instrument reference
    calibration parameters.

    Parameters
    ----------
    range_calibration
        SETAP range reference calibration[s].
    azimuth_calibration
        SETAP azimuth reference calibration[s].
    """

    class Meta:
        name = "instrumentTimingCalibrationReferenceType"

    range_calibration: "InstrumentTimingCalibrationReferenceType.RangeCalibration" = field(
        metadata={
            "name": "rangeCalibration",
            "type": "Element",
            "required": True,
        }
    )
    azimuth_calibration: "InstrumentTimingCalibrationReferenceType.AzimuthCalibration" = field(
        metadata={
            "name": "azimuthCalibration",
            "type": "Element",
            "required": True,
        }
    )

    @dataclass(frozen=True, slots=True, kw_only=True)
    class RangeCalibration:
        value: float = field(
            metadata={
                "required": True,
            }
        )
        unit: str = field(
            init=False,
            default="s",
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass(frozen=True, slots=True, kw_only=True)
    class AzimuthCalibration:
        value: float = field(
            metadata={
                "required": True,
            }
        )
        unit: str = field(
            init=False,
            default="s",
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )


@dataclass(frozen=True, slots=True, kw_only=True)
class InstrumentTimingCalibrationOffsetType:
    """
    Channel dependent instrument timing calibration offest parameters for the SETAP
    product.

    Parameters
    ----------
    swath
        Canonical name of the swath to which this set of internal
        calibration parameters applies. The swath and polarisation are used
        to index the applicable internalCalibrationParams record.
    polarisation
        Polarisation to which this set of internal calibration parameters
        applies. The polarisation along with the swathNumber are used to
        index the applicable internalCalibrationParams record.
    range_offset
        SETAP range offset calibration for given swath and polarisation[s].
    azimuth_offset
        SETAP azimuth offset calibration for given swath and
        polarisation[s].
    """

    class Meta:
        name = "instrumentTimingCalibrationOffsetType"

    swath: SwathType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    polarisation: PolarisationType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    range_offset: "InstrumentTimingCalibrationOffsetType.RangeOffset" = field(
        metadata={
            "name": "rangeOffset",
            "type": "Element",
            "required": True,
        }
    )
    azimuth_offset: "InstrumentTimingCalibrationOffsetType.AzimuthOffset" = (
        field(
            metadata={
                "name": "azimuthOffset",
                "type": "Element",
                "required": True,
            }
        )
    )

    @dataclass(frozen=True, slots=True, kw_only=True)
    class RangeOffset:
        value: float = field(
            metadata={
                "required": True,
            }
        )
        unit: str = field(
            init=False,
            default="s",
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass(frozen=True, slots=True, kw_only=True)
    class AzimuthOffset:
        value: float = field(
            metadata={
                "required": True,
            }
        )
        unit: str = field(
            init=False,
            default="s",
            metadata={
                "type": "Attribute",
                "required": True,
            },
        )


@dataclass(frozen=True, slots=True, kw_only=True)
class InstrumentTimingCalibrationOffsetListType:
    """Timing calibration offset parameters list for the SETAP processor.

    This element contains a list of swath/polarisation channel dependent
    instrument offset parameters with respect to the reference
    calibration. There is an entry for each swath/polarisation
    combination for a total of 56. The SPPDU document defines an
    additional 68 swath number codes that can be used if required.

    Parameters
    ----------
    instrument_timing_calibration_offset
        Instrument timing calibration parameters. This record contains
        swath/polarisation channel dependent parameters related to the
        instrument. There may be up to one record per swath (23 nominal
        swaths) per polarisation (4 polarisation combinations for SM, IW,
        EW) for a maximum total of 56.
    count
        Number of internalCalibrationParam records in the list.
    """

    class Meta:
        name = "instrumentTimingCalibrationOffsetListType"

    instrument_timing_calibration_offset: Tuple[
        InstrumentTimingCalibrationOffsetType, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "instrumentTimingCalibrationOffset",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 56,
        },
    )
    count: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 4294967295,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class AuxiliarySetapType:
    """
    Root element.
    """

    class Meta:
        name = "auxiliarySetapType"

    instrument_timing_calibration_reference: InstrumentTimingCalibrationReferenceType = field(
        metadata={
            "name": "instrumentTimingCalibrationReference",
            "type": "Element",
            "required": True,
        }
    )
    instrument_timing_calibration_offset_list: InstrumentTimingCalibrationOffsetListType = field(
        metadata={
            "name": "instrumentTimingCalibrationOffsetList",
            "type": "Element",
            "required": True,
        }
    )
    schema_version: Decimal = field(
        init=False,
        default=Decimal("1.6"),
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class AuxiliarySetap(AuxiliarySetapType):
    """SETAP auxiliary file definition (AUX_ITC).

    This file includes information related to the instrument timing
    calibration.  It is annotated to the S1 ETAD product.
    """

    class Meta:
        name = "auxiliarySetap"
