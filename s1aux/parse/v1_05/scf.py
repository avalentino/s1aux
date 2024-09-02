from dataclasses import dataclass, field
from decimal import Decimal
from typing import Tuple


@dataclass(frozen=True, slots=True, kw_only=True)
class ListOfGlobalParamsType:
    class Meta:
        name = "listOfGlobalParamsType"

    tropospheric_delay_correction: bool = field(
        default=True,
        metadata={
            "name": "troposphericDelayCorrection",
            "type": "Element",
            "required": True,
        },
    )
    ionospheric_delay_correction: bool = field(
        default=True,
        metadata={
            "name": "ionosphericDelayCorrection",
            "type": "Element",
            "required": True,
        },
    )
    solid_earth_tide_correction: bool = field(
        default=True,
        metadata={
            "name": "solidEarthTideCorrection",
            "type": "Element",
            "required": True,
        },
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class ListOfModeParamsType:
    class Meta:
        name = "listOfModeParamsType"

    correction_grid_range_sampling: "ListOfModeParamsType.CorrectionGridRangeSampling" = field(
        metadata={
            "name": "correctionGridRangeSampling",
            "type": "Element",
            "required": True,
        }
    )
    correction_grid_azimuth_sampling: "ListOfModeParamsType.CorrectionGridAzimuthSampling" = field(
        metadata={
            "name": "correctionGridAzimuthSampling",
            "type": "Element",
            "required": True,
        }
    )
    bistatic_azimuth_correction: bool = field(
        default=True,
        metadata={
            "name": "bistaticAzimuthCorrection",
            "type": "Element",
            "required": True,
        },
    )
    doppler_shift_range_correction: bool = field(
        metadata={
            "name": "dopplerShiftRangeCorrection",
            "type": "Element",
            "required": True,
        }
    )
    fm_mismatch_azimuth_correction: bool = field(
        metadata={
            "name": "fmMismatchAzimuthCorrection",
            "type": "Element",
            "required": True,
        }
    )

    @dataclass(frozen=True, slots=True, kw_only=True)
    class CorrectionGridRangeSampling:
        value: int = field(
            default=200,
            metadata={
                "required": True,
            },
        )
        unit: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(frozen=True, slots=True, kw_only=True)
    class CorrectionGridAzimuthSampling:
        value: int = field(
            default=200,
            metadata={
                "required": True,
            },
        )
        unit: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass(frozen=True, slots=True, kw_only=True)
class GeneralProcessorConfType:
    class Meta:
        name = "generalProcessorConfType"

    list_of_global_params: ListOfGlobalParamsType = field(
        metadata={
            "name": "listOfGlobalParams",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class ListOfModesType:
    class Meta:
        name = "listOfModesType"

    mode: Tuple["ListOfModesType.Mode", ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    count: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass(frozen=True, slots=True, kw_only=True)
    class Mode:
        name: str = field(
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        list_of_mode_params: ListOfModeParamsType = field(
            metadata={
                "name": "listOfModeParams",
                "type": "Element",
                "required": True,
            }
        )


@dataclass(frozen=True, slots=True, kw_only=True)
class ModeRelatedConfType:
    class Meta:
        name = "modeRelatedConfType"

    list_of_modes: ListOfModesType = field(
        metadata={
            "name": "listOfModes",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class SetapConfType:
    """
    Root element.
    """

    class Meta:
        name = "setapConfType"

    general_processor_conf: GeneralProcessorConfType = field(
        metadata={
            "name": "generalProcessorConf",
            "type": "Element",
            "required": True,
        }
    )
    mode_related_conf: ModeRelatedConfType = field(
        metadata={
            "name": "modeRelatedConf",
            "type": "Element",
            "required": True,
        }
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
class SetapConf(SetapConfType):
    """
    SETAP configuration auxiliary file definition (AUX_SCF).
    """

    class Meta:
        name = "setapConf"
