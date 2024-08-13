from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional, Tuple

from .s1_object_types import Double


class ActivateTotalHsBeam(Enum):
    WV1 = "WV1"
    WV2 = "WV2"


class GmfPolarisationType(Enum):
    HH = "HH"
    VV = "VV"


class UseOnlyInferenceFor(Enum):
    TOTAL_HS = "TotalHS"
    QUALITY_FLAG = "QualityFlag"


class VelthreshBeam(Enum):
    WV1 = "WV1"
    WV2 = "WV2"
    S1 = "S1"
    S2 = "S2"
    S3 = "S3"
    S4 = "S4"
    S5 = "S5"
    S6 = "S6"


@dataclass(frozen=True, slots=True, kw_only=True)
class WaveRangeAzimuthParamsType:
    """
    Range and azimuth auxiliary processing parameters for wave spectra.
    """

    class Meta:
        name = "waveRangeAzimuthParamsType"


@dataclass(frozen=True, slots=True, kw_only=True)
class GmfIndexType:
    class Meta:
        name = "gmfIndexType"

    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 21,
        }
    )
    polarisation: Optional[GmfPolarisationType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class RvlProcParamsType:
    """
    RVL component processing parameters record.

    Parameters
    ----------
    range_block_size
        Size of the Doppler estimation block in the range direction [m].
    azimuth_block_size
        Size of the Doppler estimation block in the azimuth direction [m].
    range_cell_size
        Size of grid cell interval in range direction [m].
    azimuth_cell_size
        Size of grid cell interval in azimuth direction [m].
    """

    class Meta:
        name = "rvlProcParamsType"

    range_block_size: Double = field(
        metadata={
            "name": "rangeBlockSize",
            "type": "Element",
            "required": True,
        }
    )
    azimuth_block_size: Double = field(
        metadata={
            "name": "azimuthBlockSize",
            "type": "Element",
            "required": True,
        }
    )
    range_cell_size: Double = field(
        metadata={
            "name": "rangeCellSize",
            "type": "Element",
            "required": True,
        }
    )
    azimuth_cell_size: Double = field(
        metadata={
            "name": "azimuthCellSize",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class SpectralEstimationParamsType:
    """
    Spectral estimation unit auxiliary parameters record.

    Parameters
    ----------
    frequency_separation
        Frequency separation of neighbouring looks [Hz].
    range_look_filter_width
        Range look filter width [Hz].
    azimuth_look_filter_width
        Azimuth look filter width [Hz].
    number_of_looks
        Number of individual looks.
    num_range_pixels
        Number of range pixels from input L1 product to be used in the
        estimation of the OSW [pixels].  Only used for SM, for WV all range
        pixels are used.
    num_azimuth_pixels
        Number of azimuth pixels from input L1 product to be used in the
        estimation of the OSW [pixels].  Only used for SM, for WV all
        azimuth pixels are used.
    """

    class Meta:
        name = "spectralEstimationParamsType"

    frequency_separation: Double = field(
        metadata={
            "name": "frequencySeparation",
            "type": "Element",
            "required": True,
        }
    )
    range_look_filter_width: Double = field(
        metadata={
            "name": "rangeLookFilterWidth",
            "type": "Element",
            "required": True,
        }
    )
    azimuth_look_filter_width: Double = field(
        metadata={
            "name": "azimuthLookFilterWidth",
            "type": "Element",
            "required": True,
        }
    )
    number_of_looks: int = field(
        metadata={
            "name": "numberOfLooks",
            "type": "Element",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 4294967295,
        }
    )
    num_range_pixels: int = field(
        metadata={
            "name": "numRangePixels",
            "type": "Element",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 4294967295,
        }
    )
    num_azimuth_pixels: int = field(
        metadata={
            "name": "numAzimuthPixels",
            "type": "Element",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 4294967295,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class SpectralInversionParamsType:
    """
    Spectral inversion unit auxiliary parameters record.

    Parameters
    ----------
    shortest_wavelength
        Shortest wavelength of output polar grid [m].
    longest_wavelength
        Longest wavelength of output polar grid [m].
    wave_number_bins
        Number of wavenumber bins in polar grid.
    directional_bins
        Number of directional bins in polar grid.
    velthresh
        Threshold Factor for velocity bunching.
    """

    class Meta:
        name = "spectralInversionParamsType"

    shortest_wavelength: Double = field(
        metadata={
            "name": "shortestWavelength",
            "type": "Element",
            "required": True,
        }
    )
    longest_wavelength: Double = field(
        metadata={
            "name": "longestWavelength",
            "type": "Element",
            "required": True,
        }
    )
    wave_number_bins: int = field(
        metadata={
            "name": "waveNumberBins",
            "type": "Element",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 4294967295,
        }
    )
    directional_bins: int = field(
        metadata={
            "name": "directionalBins",
            "type": "Element",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 4294967295,
        }
    )
    velthresh: Tuple["SpectralInversionParamsType.Velthresh", ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 6,
        },
    )

    @dataclass(frozen=True, slots=True, kw_only=True)
    class Velthresh:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        beam: Optional[VelthreshBeam] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass(frozen=True, slots=True, kw_only=True)
class OswProcParamsType:
    """
    OSW processing auxiliary parameters record.

    Parameters
    ----------
    spectral_estimation_params
        This record contains the auxiliary parameters required for OSW
        spectral estimation.
    spectral_inversion_params
        This record contains the auxiliary parameters required for OSW
        spectral inversion.
    activate_total_hs
        Activate the computation of totalHs.
    activate_group_dir
        Activate the computation of group direction.
    activate_noise_correction
        activate the noise correction.
    sea_coverage_threshold
        Threshold on percentage of Sea Coverage. Imagettes having a
        percentage of Sea Coverage below this threshold will not be
        processed with a full OSW inversion. Variables not generated will
        contain fill values. Default is 0%.
    use_only_inference
        If false try to use inference with model provided in AUX_ML2: if
        fail continue process either with legacy process or fill value. If
        true perform inference with model provided in AUX_ML2: if fail stop
        LOP process with error.
    """

    class Meta:
        name = "oswProcParamsType"

    spectral_estimation_params: SpectralEstimationParamsType = field(
        metadata={
            "name": "spectralEstimationParams",
            "type": "Element",
            "required": True,
        }
    )
    spectral_inversion_params: SpectralInversionParamsType = field(
        metadata={
            "name": "spectralInversionParams",
            "type": "Element",
            "required": True,
        }
    )
    activate_total_hs: Tuple["OswProcParamsType.ActivateTotalHs", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "activateTotalHs",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
    activate_group_dir: str = field(
        default="false",
        metadata={
            "name": "activateGroupDir",
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        },
    )
    activate_noise_correction: Optional[str] = field(
        default=None,
        metadata={
            "name": "activateNoiseCorrection",
            "type": "Element",
            "pattern": r"(false)|(true)",
        },
    )
    sea_coverage_threshold: Optional[float] = field(
        default=None,
        metadata={
            "name": "seaCoverageThreshold",
            "type": "Element",
            "min_inclusive": 0.0,
            "max_inclusive": 100.0,
        },
    )
    use_only_inference: Tuple["OswProcParamsType.UseOnlyInference", ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "useOnlyInference",
                "type": "Element",
                "max_occurs": 2,
            },
        )
    )

    @dataclass(frozen=True, slots=True, kw_only=True)
    class ActivateTotalHs:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        beam: Optional[ActivateTotalHsBeam] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass(frozen=True, slots=True, kw_only=True)
    class UseOnlyInference:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        for_value: Optional[UseOnlyInferenceFor] = field(
            default=None,
            metadata={
                "name": "for",
                "type": "Attribute",
            },
        )


@dataclass(frozen=True, slots=True, kw_only=True)
class OwiProcParamsType:
    """
    OWI processing auxiliary parameters record.

    Parameters
    ----------
    range_cell_size
        Size of the SAR derived wind field in the range direction [m]. Wind
        cells should typically be square therefore nominally rangeCellSize =
        azimuthCellSize.
    azimuth_cell_size
        Size of the SAR derived wind field in the azimuth direction [m].
        Wind cells should typically be square therefore nominally
        azimuthCellSize = rangeCellSize.
    distance_to_shore
        Distance to shore where the processing is not performed [km].
    wind_speed_std_dev
        Standard deviation error of the wind speed provided by ancillary
        wind information [m/s].
    wind_dir_std_dev
        Standard deviation error of the wind direction provided by ancillary
        wind information [degrees].
    gmf_index
        Name (or index) of the Geophysical Model Function (GMF) to be used
        for the wind inversion
    pr_index
        Name (or index) of the Polarisation Ratio Function to be used for
        the wind inversion (used for HH polarisation data).  This function
        converts HH NRCS into VV NRCS before applying the GMF to retrieve
        the wind.
    inversion_quality_threshold
        Value above which minimization in the inversion is considered low
        quality.
    calibration_quality_threshold
        Value above which the calibration of the product is considered to be
        incorrect.
    nrcs_quality_threshold
        Value above which the NRCS estimated at the SAR wind cell resolution
        is considered as low quality.
    bright_target_pfa
        Probability of false alarm for the removal of bright target.
    activate_noise_correction
        Activate noise correction.
    """

    class Meta:
        name = "owiProcParamsType"

    range_cell_size: Double = field(
        metadata={
            "name": "rangeCellSize",
            "type": "Element",
            "required": True,
        }
    )
    azimuth_cell_size: Double = field(
        metadata={
            "name": "azimuthCellSize",
            "type": "Element",
            "required": True,
        }
    )
    distance_to_shore: Double = field(
        metadata={
            "name": "distanceToShore",
            "type": "Element",
            "required": True,
        }
    )
    wind_speed_std_dev: Double = field(
        metadata={
            "name": "windSpeedStdDev",
            "type": "Element",
            "required": True,
        }
    )
    wind_dir_std_dev: Double = field(
        metadata={
            "name": "windDirStdDev",
            "type": "Element",
            "required": True,
        }
    )
    gmf_index: Tuple[GmfIndexType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "gmfIndex",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
    pr_index: int = field(
        metadata={
            "name": "prIndex",
            "type": "Element",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 3,
        }
    )
    inversion_quality_threshold: Double = field(
        metadata={
            "name": "inversionQualityThreshold",
            "type": "Element",
            "required": True,
        }
    )
    calibration_quality_threshold: Double = field(
        metadata={
            "name": "calibrationQualityThreshold",
            "type": "Element",
            "required": True,
        }
    )
    nrcs_quality_threshold: Double = field(
        metadata={
            "name": "nrcsQualityThreshold",
            "type": "Element",
            "required": True,
        }
    )
    bright_target_pfa: Double = field(
        metadata={
            "name": "brightTargetPfa",
            "type": "Element",
            "required": True,
        }
    )
    activate_noise_correction: Optional[str] = field(
        default=None,
        metadata={
            "name": "activateNoiseCorrection",
            "type": "Element",
            "pattern": r"(false)|(true)",
        },
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class OcnProcParamsType:
    """
    OCN processing auxiliary parameters record.

    Parameters
    ----------
    osw_proc_params
        OSW component processor parameters.
    owi_proc_params
        OWI component processor parameters.
    rvl_proc_params
        RVL component processor parameters.
    """

    class Meta:
        name = "ocnProcParamsType"

    osw_proc_params: OswProcParamsType = field(
        metadata={
            "name": "oswProcParams",
            "type": "Element",
            "required": True,
        }
    )
    owi_proc_params: OwiProcParamsType = field(
        metadata={
            "name": "owiProcParams",
            "type": "Element",
            "required": True,
        }
    )
    rvl_proc_params: RvlProcParamsType = field(
        metadata={
            "name": "rvlProcParams",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class L2ProductType:
    """
    Standard L2 product record that holds the all the applicable auxiliary data for
    this product type.

    Parameters
    ----------
    product_id
        L2 Product type identifier as per External ICD to which this set of
        parameters applies. The productId is used to index and find the
        correct set of auxiliary parameters for each standard L2 product the
        IPF is capable of generating.
    ocn_proc_params
        OCN processing auxiliary parameters. This record contains the
        auxiliary parameters required during OSW, OWI, and RVL processing.
        This record is only present for products that require OCN
        processing.
    """

    class Meta:
        name = "l2ProductType"

    product_id: str = field(
        metadata={
            "name": "productId",
            "type": "Element",
            "required": True,
        }
    )
    ocn_proc_params: OcnProcParamsType = field(
        metadata={
            "name": "ocnProcParams",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class L2ProductListType:
    """
    Auxiliary parameters list for standard L2 products.

    Parameters
    ----------
    product
        Product auxiliary parameters. This DSR contains all of the auxiliary
        parameters required to process a single product. The parameters are
        stored in structures that are grouped together by the logical
        processing steps used during image creation. This DSR contains the
        productId element which is used to identify the product that this
        set of parameters applies to. The parameters within this DSR and its
        children are not polarisation dependent and in generally apply to
        the entire product.
    count
        The number of elements contained in the list. There is an entry for
        each standard L2 product type that the IPF is capable of generating.
    """

    class Meta:
        name = "l2ProductListType"

    product: Tuple[L2ProductType, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 10,
        },
    )
    count: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class L2AuxiliaryProcessorParametersType:
    """
    Sentinel-1 IPF L2 processing parameters auxiliary file specification.

    Parameters
    ----------
    product_list
        List of L2 standard products containing the applicable auxiliary
        parameters for each. This list contains an entry for each product
        the IPF is capable of generating, indexed by its unique product
        identifier.
    schema_version
    """

    class Meta:
        name = "l2AuxiliaryProcessorParametersType"

    product_list: L2ProductListType = field(
        metadata={
            "name": "productList",
            "type": "Element",
            "required": True,
        }
    )
    schema_version: Decimal = field(
        init=False,
        default=Decimal("3.12"),
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class L2AuxiliaryProcessorParameters(L2AuxiliaryProcessorParametersType):
    """
    L2 Processor parameters auxiliary file definition (AUX_PP2).
    """

    class Meta:
        name = "l2AuxiliaryProcessorParameters"
