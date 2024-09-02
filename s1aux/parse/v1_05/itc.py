from dataclasses import dataclass, field
from decimal import Decimal
from typing import Tuple

from .s1_object_types import (
    Double,
    PolarisationType,
    SwathType,
)


@dataclass(frozen=True, slots=True, kw_only=True)
class InstrumentTimingCalibrationType:
    """
    Channel dependent instrument timing calibration parameters for the SETAP
    product.

    Parameters
    ----------
    swath
        Canonical name of the swath to which this set of internal
        calibration parameters applies. The swath and polarisation are used
        to index the applicable internalCalibrationParams record.
    polarisation
        Polarisation to which this set of internal calibration parameters
        applies. The polarisation andUsed along with the swathNumber are
        used to index the applicable internalCalibrationParams record.
    range_calibration
        SETAP range calibration[s].
    azimuth_calibration
        SETAP azimuth calibration [s].
    """

    class Meta:
        name = "instrumentTimingCalibrationType"

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
    range_calibration: Double = field(
        metadata={
            "name": "rangeCalibration",
            "type": "Element",
            "required": True,
        }
    )
    azimuth_calibration: Double = field(
        metadata={
            "name": "azimuthCalibration",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class InstrumentTimingCalibrationListType:
    """Timing calibration parameters list for the SETAP processor.

    This element contains a list of swath/polarisation channel dependent
    instrument parameters. There is an entry for each swath/polarisation
    combination for a total of 56. The SPPDU document defines an
    additional 68 swath number codes that can be used if required.

    Parameters
    ----------
    instrument_timing_calibration
        Instrument timing calibration parameters. This record contains
        swath/polarisation channel dependent parameters related to the
        instrument. There may be up to one record per swath (23 nominal
        swaths) per polarisation (4 polarisation combinations for SM, IW,
        EW) for a maximum total of 56.
    count
        Number of internalCalibrationParam records in the list.
    """

    class Meta:
        name = "instrumentTimingCalibrationListType"

    instrument_timing_calibration: Tuple[
        InstrumentTimingCalibrationType, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "instrumentTimingCalibration",
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

    instrument_timing_calibration_list: InstrumentTimingCalibrationListType = (
        field(
            metadata={
                "name": "instrumentTimingCalibrationList",
                "type": "Element",
                "required": True,
            }
        )
    )
    schema_version: Decimal = field(
        init=False,
        default=Decimal("1.5"),
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
