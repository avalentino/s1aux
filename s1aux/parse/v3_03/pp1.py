from typing import Optional
from decimal import Decimal
from dataclasses import field, dataclass

from .s1_object_types import (
    Float,
    Int32,
    Double,
    Uint32,
    SwathType,
    FloatArray,
    DcMethodType,
    PgSourceType,
    ChirpSourceType,
    DcInputDataType,
    RrfSpectrumType,
    OutputPixelsType,
    WeightingWindowType,
    FloatCoefficientArray,
    DoubleCoefficientArray,
    BistaticDelayMethodType,
    TopsFilterConventionType,
)


@dataclass(frozen=True, slots=True, kw_only=True)
class GrdProcParamsType:
    """
    GRD processing auxiliary parameters record.

    Parameters
    ----------
    apply_srgr_conversion_flag
        SRGR conversion flag. True if SRGR conversion is to be performed,
        false otherwise.
    remove_thermal_noise_flag
        Thermal noise removal flag. True if thermal noise removal is to be
        performed, false otherwise.
    """

    class Meta:
        name = "grdProcParamsType"

    apply_srgr_conversion_flag: str = field(
        metadata={
            "name": "applySrgrConversionFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        }
    )
    remove_thermal_noise_flag: str = field(
        metadata={
            "name": "removeThermalNoiseFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class AziProcBlockParamsType:
    """
    Parameters
    ----------
    swath
        Swath identifier. This parameter defines the swath to which this
        record applies.
    azi_proc_bandwidth
        Total processing bandwidth [Hz]. This parameter defines the
        bandwidth (Bw) to use during processing. The processing bandwidth
        (Bw) must be 0 &lt; Bw &lt;= PRF.
    azi_block_size
        Azimuth processing block size [lines].  Only used for SM and IM
        modes.
    extra_azi_proc_block_overlap
        Extra azimuth block overlap to account for possible variation of
        Doppler centroid frequency from azimuth block to azimuth block
        [lines].  Only used for SM and IM modes.
    max_fdc
        For SM this is the maximum expected absolute value of Doppler
        centroid frequency [Hz]. Used to calculate the SM SLC azimuth
        matched filter throwaway component of azimuth block overlap as
        applicable to all azimuth blocks in a segment. This parameter is
        maxDeltaFdc from [A-11]. Although this field is an array, for SM
        only the first coefficient is applicable. For TOPS this is the
        polynomial that describes the expected offset and maximum excursion
        of the Doppler centroid frequency over the total slant range time
        extent, TSR, of all swaths in the mode. This is an array of five
        floating point coefficients separated by spaces. The first
        coefficient is the Doppler centroid offset [Hz] and the remaining
        coefficients describe the expected variation of the Doppler centroid
        frequency along range. The polynomial is evaluated as a function of
        the slant range time t as: maxFdc(t) = C0 + C1 * t + C2 * t^2 + C3 *
        t^3 + C4 * t^4        {t = 0 .. TSR}
    """

    class Meta:
        name = "aziProcBlockParamsType"

    swath: SwathType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    azi_proc_bandwidth: Float = field(
        metadata={
            "name": "aziProcBandwidth",
            "type": "Element",
            "required": True,
        }
    )
    azi_block_size: Uint32 = field(
        metadata={
            "name": "aziBlockSize",
            "type": "Element",
            "required": True,
        }
    )
    extra_azi_proc_block_overlap: Uint32 = field(
        metadata={
            "name": "extraAziProcBlockOverlap",
            "type": "Element",
            "required": True,
        }
    )
    max_fdc: FloatCoefficientArray = field(
        metadata={
            "name": "maxFdc",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class AzimuthParamsType:
    """
    Azimuth processing parameters record.

    Parameters
    ----------
    swath
        Swath identifier. This parameter defines the swath to which this
        record applies.
    weighting_window
        Name of the weighting window to use during processing.
    window_coefficient
        Value of the weighting window coefficient to use during processing.
    processing_bandwidth
        Total processing bandwidth [Hz]. This parameter defines the
        bandwidth (Bw) to use during processing. For range, the processing
        bandwidth (Bw) must be 0 &lt; Bw &lt;= pulse Bw, for azimuth the
        processing bandwidth (Bw) must be 0 &lt; Bw &lt;= PRF.
    look_bandwidth
        Look bandwidth [Hz]. This parameter defines the bandwidth to use for
        each look during processing.
    number_of_looks
        Number of looks. This parameter defines the number of looks to use
        during multi-look processing.
    pixel_spacing
        Spacing between pixels in the output image [m].
    multi_look_throwaway
        Number of output azimuth samples to be discarded at both block edges
        .
    """

    class Meta:
        name = "azimuthParamsType"

    swath: SwathType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    weighting_window: WeightingWindowType = field(
        metadata={
            "name": "weightingWindow",
            "type": "Element",
            "required": True,
        }
    )
    window_coefficient: Double = field(
        metadata={
            "name": "windowCoefficient",
            "type": "Element",
            "required": True,
        }
    )
    processing_bandwidth: Double = field(
        metadata={
            "name": "processingBandwidth",
            "type": "Element",
            "required": True,
        }
    )
    look_bandwidth: Double = field(
        metadata={
            "name": "lookBandwidth",
            "type": "Element",
            "required": True,
        }
    )
    number_of_looks: Uint32 = field(
        metadata={
            "name": "numberOfLooks",
            "type": "Element",
            "required": True,
        }
    )
    pixel_spacing: Double = field(
        metadata={
            "name": "pixelSpacing",
            "type": "Element",
            "required": True,
        }
    )
    multi_look_throwaway: Int32 = field(
        metadata={
            "name": "multiLookThrowaway",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class DcProcParamsType:
    """
    Doppler centroid processing auxiliary parameters.

    Parameters
    ----------
    dc_method
        Doppler centroid estimation method. Although the DCE from both orbit
        and attitude data and data analysis are always performed and the
        results provided in the output product annotations, this parameter
        is used to specify exactly which Doppler centroid estimation method
        to use during the image focusing.
    dc_input_data
        Type of input data used for Doppler centroid estimation.  Options
        are “Raw” and “Range Compressed”.
    dc_predefined_coefficients
        Pre-defined Doppler centroid coefficients.  These Doppler centroid
        coefficients shall be used during processing if and only if the
        dcMethod element is set to "Pre-defined". This parameter is an array
        of up to five double precision floating point numbers separated by
        spaces. These values represent Doppler centroid coefficients as a
        function of slant range time: d0, d1, d2, d3, and d4 where: Doppler
        Centroid = d0 + d1(tSR - t0) + d2(tSR-t0)^2 + d3(tSR-t0)^3 +
        d4(tSRt0)^4
    dc_rms_error_threshold
        Doppler centroid estimation signal-to-noiseroot mean squared (RMS)
        error threshold. If the RMS error of the Doppler centroid estimate
        from data is below this threshold they shall not be used during
        processing; instead, the Doppler centroid calculated from orbit and
        attitude shall be used, unless overridden by the dcMethod = Pre-
        defined.
    """

    class Meta:
        name = "dcProcParamsType"

    dc_method: DcMethodType = field(
        metadata={
            "name": "dcMethod",
            "type": "Element",
            "required": True,
        }
    )
    dc_input_data: DcInputDataType = field(
        metadata={
            "name": "dcInputData",
            "type": "Element",
            "required": True,
        }
    )
    dc_predefined_coefficients: FloatCoefficientArray = field(
        metadata={
            "name": "dcPredefinedCoefficients",
            "type": "Element",
            "required": True,
        }
    )
    dc_rms_error_threshold: Float = field(
        metadata={
            "name": "dcRmsErrorThreshold",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class EllipsoidParamsType:
    """
    Ellipsoid and DEM parameters.

    Parameters
    ----------
    ellipsoid_name
        Name of the reference ellipsoid.
    ellipsoid_semi_major_axis
        Semi-major axis of ellipsoid [m].
    ellipsoid_semi_minor_axis
        Semi-minor axis of ellipsoid [m].
    use_dem_flag
        This flag is used to control the use of a DEM during processing.
        Set to true if a DEM is to be used during processing, false
        otherwise.
    """

    class Meta:
        name = "ellipsoidParamsType"

    ellipsoid_name: str = field(
        metadata={
            "name": "ellipsoidName",
            "type": "Element",
            "required": True,
        }
    )
    ellipsoid_semi_major_axis: Double = field(
        metadata={
            "name": "ellipsoidSemiMajorAxis",
            "type": "Element",
            "required": True,
        }
    )
    ellipsoid_semi_minor_axis: Double = field(
        metadata={
            "name": "ellipsoidSemiMinorAxis",
            "type": "Element",
            "required": True,
        }
    )
    use_dem_flag: str = field(
        metadata={
            "name": "useDemFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class QlProcParamsType:
    """
    Quick-look processing auxiliary parameters record.

    Parameters
    ----------
    range_decimation_factor
        Range decimation factor for the image.
    range_averaging_factor
        Range averaging factor for the image.
    azimuth_decimation_factor
        Azimuth decimation factor for the  image.
    azimuth_averaging_factor
        Azimuth averaging factor for the  image.
    """

    class Meta:
        name = "qlProcParamsType"

    range_decimation_factor: Uint32 = field(
        metadata={
            "name": "rangeDecimationFactor",
            "type": "Element",
            "required": True,
        }
    )
    range_averaging_factor: Uint32 = field(
        metadata={
            "name": "rangeAveragingFactor",
            "type": "Element",
            "required": True,
        }
    )
    azimuth_decimation_factor: Uint32 = field(
        metadata={
            "name": "azimuthDecimationFactor",
            "type": "Element",
            "required": True,
        }
    )
    azimuth_averaging_factor: Uint32 = field(
        metadata={
            "name": "azimuthAveragingFactor",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class RangeParamsType:
    """
    Range processing parameters record.

    Parameters
    ----------
    swath
        Swath identifier. This parameter defines the swath to which this
        record applies.
    weighting_window
        Name of the weighting window to use during processing.
    window_coefficient
        Value of the weighting window coefficient to use during processing.
    processing_bandwidth
        Total processing bandwidth [Hz]. This parameter defines the
        bandwidth (Bw) to use during processing. For range, the processing
        bandwidth (Bw) must be 0 &lt; Bw &lt;= pulse Bw, for azimuth the
        processing bandwidth (Bw) must be 0 &lt; Bw &lt;= PRF.
    look_bandwidth
        Look bandwidth [Hz]. This parameter defines the bandwidth to use for
        each look during processing.
    number_of_looks
        Number of looks. This parameter defines the number of looks to use
        during multi-look processing.
    pixel_spacing
        Spacing between pixels in the output image [m].
    multi_look_throwaway
        Number of ground range samples to be discarded at both block edges .
    """

    class Meta:
        name = "rangeParamsType"

    swath: SwathType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    weighting_window: WeightingWindowType = field(
        metadata={
            "name": "weightingWindow",
            "type": "Element",
            "required": True,
        }
    )
    window_coefficient: Double = field(
        metadata={
            "name": "windowCoefficient",
            "type": "Element",
            "required": True,
        }
    )
    processing_bandwidth: Double = field(
        metadata={
            "name": "processingBandwidth",
            "type": "Element",
            "required": True,
        }
    )
    look_bandwidth: Double = field(
        metadata={
            "name": "lookBandwidth",
            "type": "Element",
            "required": True,
        }
    )
    number_of_looks: Uint32 = field(
        metadata={
            "name": "numberOfLooks",
            "type": "Element",
            "required": True,
        }
    )
    pixel_spacing: Double = field(
        metadata={
            "name": "pixelSpacing",
            "type": "Element",
            "required": True,
        }
    )
    multi_look_throwaway: Int32 = field(
        metadata={
            "name": "multiLookThrowaway",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class ReplicaThresholdParamsType:
    """
    Pulse thresholds auxiliary parameters record.

    Parameters
    ----------
    max_xcorr_pulse_irw
        Maximum allowable broadening of the IRW of the cross-correlation
        with the nominal replica [%]. Used for setting the
        replicaReconstructionFailedFlag in the output product annotations.
    max_xcorr_pulse_pslr
        Maximum allowable PSLR of the cross correlation with the nominal
        replica [dB]. Used for setting the replicaReconstructionFailedFlag
        in the output product annotations.
    max_xcorr_pulse_islr
        Maximum allowable ISLR of the cross correlation with the nominal
        replica [dB]. Used for setting the replicaReconstructionFailedFlag
        in the output product annotations.
    max_pg_amp_std_fraction
        Maximum deviation from the mean allowed for the PG product
        amplitude, measured as a fraction of the standard deviation.
        Relative PG product validation shall fail if this value is exceeded.
    max_pg_phase_std_fraction
        Maximum deviation from the mean allowed for the PG product phase,
        measured as a fraction of the standard deviation. Relative PG
        product validation shall fail if this value is exceeded.
    max_pg_amp_error
        Maximum deviation allowed for a PG product amplitude from the
        corresponding PG product model value [dB]. Absolute PG product
        validation shall fail if this value is exceeded.
    max_pg_phase_error
        Maximum deviation allowed for a PG product phase from the
        corresponding PG product model value [degrees]. Absolute PG product
        validation shall fail if this value is exceeded.
    max_num_invalid_pg_val_fraction
        Maximum number of invalid PG product values allowed, expressed as a
        fraction of the total number of PG values. If the percentage of the
        invalid PG products does not exceed this value, then the invalid PG
        values will be discarded and only the valid PG values will be
        further used in the linear interpolation and application to the
        data. Otherwise if the percentage of the invalid PG products does
        exceed this value, then all the calculated PG product values will be
        discarded and replaced with the corresponding PG product model
        values.
    """

    class Meta:
        name = "replicaThresholdParamsType"

    max_xcorr_pulse_irw: Double = field(
        metadata={
            "name": "maxXCorrPulseIrw",
            "type": "Element",
            "required": True,
        }
    )
    max_xcorr_pulse_pslr: Double = field(
        metadata={
            "name": "maxXCorrPulsePslr",
            "type": "Element",
            "required": True,
        }
    )
    max_xcorr_pulse_islr: Double = field(
        metadata={
            "name": "maxXCorrPulseIslr",
            "type": "Element",
            "required": True,
        }
    )
    max_pg_amp_std_fraction: Float = field(
        metadata={
            "name": "maxPgAmpStdFraction",
            "type": "Element",
            "required": True,
        }
    )
    max_pg_phase_std_fraction: Float = field(
        metadata={
            "name": "maxPgPhaseStdFraction",
            "type": "Element",
            "required": True,
        }
    )
    max_pg_amp_error: Float = field(
        metadata={
            "name": "maxPgAmpError",
            "type": "Element",
            "required": True,
        }
    )
    max_pg_phase_error: Float = field(
        metadata={
            "name": "maxPgPhaseError",
            "type": "Element",
            "required": True,
        }
    )
    max_num_invalid_pg_val_fraction: Float = field(
        metadata={
            "name": "maxNumInvalidPgValFraction",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class ScalingLutType:
    """
    Application scaling LUT.

    Parameters
    ----------
    output_pixels
        Pixel format. Application scaling LUTs are specific to output pixel
        data type. This field specifies the output pixel type to which this
        LUT applies.
    incidence_angle_start
        Incidence angle of the first value in the LUT [degrees].
    angle_increment
        Step size of the incidence angle between each value [degrees].
    values
        Application LUT values. This element is a vector containing
        attribute "count" single precision floating point values separated
        by spaces [linear].
    """

    class Meta:
        name = "scalingLutType"

    output_pixels: OutputPixelsType = field(
        metadata={
            "name": "outputPixels",
            "type": "Element",
            "required": True,
        }
    )
    incidence_angle_start: Double = field(
        metadata={
            "name": "incidenceAngleStart",
            "type": "Element",
            "required": True,
        }
    )
    angle_increment: Double = field(
        metadata={
            "name": "angleIncrement",
            "type": "Element",
            "required": True,
        }
    )
    values: FloatArray = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class SlcSwathParamsType:
    """
    Azimuth processing bandwidth.

    Parameters
    ----------
    swath
        Swath identifier. This parameter defines the swath to which this
        record applies.
    gain
        Product and polarisation specific gain. This parameter defines the
        gain that is applied to each output sample during azimuth
        processing. This parameter is an array of double precision floating
        point numbers separated by spaces, one for each of the possible
        polarisations in the following order: HH HV VV VH
    instantaneous_bandwidth
        Azimuth instantaneous bandwidth [Hz]. This field is applicable only
        to IW and EW modes.
    nominal_beam_width
        Nominal width of the beam [degrees].
    """

    class Meta:
        name = "slcSwathParamsType"

    swath: SwathType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    gain: DoubleCoefficientArray = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    instantaneous_bandwidth: Float = field(
        metadata={
            "name": "instantaneousBandwidth",
            "type": "Element",
            "required": True,
        }
    )
    nominal_beam_width: Double = field(
        metadata={
            "name": "nominalBeamWidth",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class AziProcBlockParamsListType:
    """
    Parameters
    ----------
    azi_proc_block_params
        Azimuth processing block parameters record indexed by swath.  There
        will be one record per swath.
    count
        Number of parameter records in this list. There is one record per
        swath for each instrument mode.
    """

    class Meta:
        name = "aziProcBlockParamsListType"

    azi_proc_block_params: tuple[AziProcBlockParamsType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "aziProcBlockParams",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 7,
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
class AzimuthParamsListType:
    """
    List of azimuth processing parameters record.

    Parameters
    ----------
    azimuth_params
        This record contains the set of auxiliary parameters required during
        azimuth processing. For each product type, there is one record for
        each applicable swath within the product.  There will be one record
        per swath for each mode.  For example, for S1 IW there will be 3
        records, and for ASAR IM there will be 7 records.
    count
        Number of parameter records in this list. There is one record per
        swath for each instrument mode.
    """

    class Meta:
        name = "azimuthParamsListType"

    azimuth_params: tuple[AzimuthParamsType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "azimuthParams",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 7,
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
class PreProcParamsType:
    """
    Pre-processing parameters record.

    Parameters
    ----------
    input_mean_expected
        This parameter specifies the expected mean of the input I and Q
        samples and is used in verifying that the calculated mean of the
        output samples is within the tolerated threshold.
    input_mean_threshold
        Threshold for setting the inputDataMeanOutsideNominalRange flag in
        the ouput product annotations. This is the value T, such that the
        measured mean must fall between the inputMeanExpected-T and
        inputMeanExpected+T. This threshold is used for both the I and Q
        channels.
    input_std_dev_expected
        This parameter specifies the expected standard deviation of the
        input I and Q samples and is used in verifying that the calculated
        std. dev. of the output samples is within the tolerated threshold.
    input_std_dev_threshold
        Threshold for setting the inputDataStdDevOutsideNominalRange flag in
        the ouput product annotations. This is the value D, such that the
        measured std. dev. must fall between the inputStdDevExpected-D and
        inputStdDevExpected+D. This threshold is used for both the I and Q
        channels.
    terrain_height_azi_spacing
        Frequency of terrain height estimates along azimuth [s].
    terrain_height_azi_block_size
        Size of the block along azimuth used to calculate an average terrain
        height [s].
    chirp_replica_source
        Chirp replica to use during processing. The extracted replica will
        be used if this parameter is set to "Extracted" and the IPF
        determines that the reconstructed replica is valid; otherwise, the
        nominal chirp will be used if this field is set to "Nominal" or the
        reconstructed replica is deemed invalid.
    replica_thresholds
        Thresholds used to assess the quality of the replica reconstruction
        and the PG product.
    missing_lines_threshold
        Threshold for setting the missingLinesSignificant flag in the output
        product annotations.  This parameter ranges between 0 and 1 and
        specifies the percentage of missing lines to total lines [%].
    lines_per_gap_threshold
        This parameter specifies the number of consecutive missing lines in
        the input data which constitute a gap [lines].
    missing_gaps_threshold
        Threshold for setting the significantGapsInInputData flag in the
        output product annotations. This parameter specifies the number of
        missing gaps permitted in the input data.
    perform_internal_calibration_flag
        Flag controlling the calculation of the internal calibration from
        the calibration pulses extracted from the downlink. If this flag is
        set to true then the internal calibration information will be
        calculated by the IPF using the calibration pulses extracted from
        the downlink. If this flag is set to false then the internal
        calibration information will not be calculated from the calibration
        pulses extracted from the downlink. In addition, if this flag is set
        to false, the values provided for chirpReplicaSource and pgSource
        will be ignored and set to "Nominal" and "Model" respectively.
    pg_source
        PG source to use during processing.  The PG derived from the
        extracted replica will be used if this parameter is set to
        “Extracted” and the IPF determines that the reconstructed replica is
        valid; otherwise, the pgModel will be used if this field is set to
        “Model” or the reconstructed replica is deemed invalid.
    estimate_noise_equivalent_power_flag
        If true, then estimate the noise equivalent power from the noise
        equivalent echoes.
    """

    class Meta:
        name = "preProcParamsType"

    input_mean_expected: Double = field(
        metadata={
            "name": "inputMeanExpected",
            "type": "Element",
            "required": True,
        }
    )
    input_mean_threshold: Double = field(
        metadata={
            "name": "inputMeanThreshold",
            "type": "Element",
            "required": True,
        }
    )
    input_std_dev_expected: Double = field(
        metadata={
            "name": "inputStdDevExpected",
            "type": "Element",
            "required": True,
        }
    )
    input_std_dev_threshold: Double = field(
        metadata={
            "name": "inputStdDevThreshold",
            "type": "Element",
            "required": True,
        }
    )
    terrain_height_azi_spacing: Double = field(
        metadata={
            "name": "terrainHeightAziSpacing",
            "type": "Element",
            "required": True,
        }
    )
    terrain_height_azi_block_size: Double = field(
        metadata={
            "name": "terrainHeightAziBlockSize",
            "type": "Element",
            "required": True,
        }
    )
    chirp_replica_source: ChirpSourceType = field(
        metadata={
            "name": "chirpReplicaSource",
            "type": "Element",
            "required": True,
        }
    )
    replica_thresholds: ReplicaThresholdParamsType = field(
        metadata={
            "name": "replicaThresholds",
            "type": "Element",
            "required": True,
        }
    )
    missing_lines_threshold: Double = field(
        metadata={
            "name": "missingLinesThreshold",
            "type": "Element",
            "required": True,
        }
    )
    lines_per_gap_threshold: Uint32 = field(
        metadata={
            "name": "linesPerGapThreshold",
            "type": "Element",
            "required": True,
        }
    )
    missing_gaps_threshold: Uint32 = field(
        metadata={
            "name": "missingGapsThreshold",
            "type": "Element",
            "required": True,
        }
    )
    perform_internal_calibration_flag: str = field(
        metadata={
            "name": "performInternalCalibrationFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        }
    )
    pg_source: PgSourceType = field(
        metadata={
            "name": "pgSource",
            "type": "Element",
            "required": True,
        }
    )
    estimate_noise_equivalent_power_flag: str = field(
        metadata={
            "name": "estimateNoiseEquivalentPowerFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class RangeParamsListType:
    """
    List of range processing parameters record.

    Parameters
    ----------
    range_params
        This record contains the set of auxiliary parameters required during
        range processing. For each product type, there is one record for
        each applicable swath within the product.  There will be one record
        per swath for each mode.  For example, for S1 IW there will be 3
        records, and for ASAR IM there will be 7 records.
    count
        Number of parameter records in this list. There is one record per
        swath for each instrument mode.
    """

    class Meta:
        name = "rangeParamsListType"

    range_params: tuple[RangeParamsType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "rangeParams",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 7,
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
class ScalingLutListType:
    """
    List of application scaling LUTs.

    Parameters
    ----------
    scaling_lut
        Application scaling LUT record. This record provides the necessary
        scaling LUT for outputPixels.
    count
        Number of scalingLut records in the list.
    """

    class Meta:
        name = "scalingLutListType"

    scaling_lut: tuple[ScalingLutType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "scalingLut",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 4,
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
class SlcSwathParamsListType:
    """
    List of azimuth processing bandwidths indexed by swath.

    Parameters
    ----------
    swath_params
        Azimuth processing bandwidth record indexed by swath.  There will be
        one record per swath for each mode.  For example, for S1 IW there
        will be 3 records, and for ASAR IM there will be 7 records.
    count
        Number of swathParams records in the list.
    """

    class Meta:
        name = "slcSwathParamsListType"

    swath_params: tuple[SlcSwathParamsType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "swathParams",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 7,
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
class ApplicationLutType:
    """
    Application LUT record.

    Parameters
    ----------
    application_lut_id
        Name of this application scaling LUT.
    scaling_lut_list
        List of application scaling LUTs for this applicationLutId. There is
        one entry for each output pixel type.
    """

    class Meta:
        name = "applicationLutType"

    application_lut_id: str = field(
        metadata={
            "name": "applicationLutId",
            "type": "Element",
            "required": True,
        }
    )
    scaling_lut_list: ScalingLutListType = field(
        metadata={
            "name": "scalingLutList",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class CommonProcParamsType:
    """
    Common processing parameters shared by mulitple processing modules.

    Parameters
    ----------
    correct_iqbias_flag
        Flag to control the correctin of the constant biases from the I and
        Q channels. IQ bias correction will be performed if and only if this
        flag is set to "true".
    correct_iqgain_imbalance_flag
        Flag to control the correctin of the IQ gain imbalance. IQ gain
        imbalance correction will be performed if and only if this flag is
        set to "true".
    correct_iqorthogonality_flag
        Flag to control the correctin of the IQ orthogonality. IQ
        orthorgonality correction will be performed if and only if this flag
        is set to "true".
    correct_bistatic_delay_flag
        Flag to compensate for the bi-static delay. Correction will be
        performed if and only if this flag is set to "true".
    correct_bistatic_delay_method
        Method used to compensate for the bi-static delay.
    correct_rx_variation_flag
        Flag to control the correction of the gain variation across the
        receive window. Receive variation correction will be performed if
        and only this flag is set to “true”.
    ellipsoid_params
        Ellipsoid and DEM parameters.
    azi_proc_block_params_list
        Azimuth processing block parameters used for SM processing.  One
        record per SM swath.
    output_mean_expected
        This parameter specifies the expected mean of the samples in the
        output mage and is used in verifying that the calculated mean of the
        output samples is within the tolerated threshold.
    output_mean_threshold
        Threshold for setting the outputDataMeanOutsideNominalRange flag in
        the ouput product annotations. This is the value T, such that the
        measured mean must fall between the outputMeanExpected-T and
        outputMeanExpected+T.
    output_std_dev_expected
        This parameter specifies the expected standard deviation of the
        samples in the output image and is used in verifying that the
        calculated std. dev. of the output samples is within the tolerated
        threshold.
    output_std_dev_threshold
        Threshold for setting the outputDataStdDevOutsideNominalRange flag
        in the ouput product annotations.  This is the value D, such that
        the measured standard deviation must fall between the
        outputStdDevExpected-D and outputStdDevExpected+D.
    tops_filter_convention
        Name of the TOPS filter convention to use during processing. This
        field controls how the TOPS ramping/de-ramping filters are defined.
        If set to "Only Echo Lines" then the filter is defined using only
        the echo lines in a burst; otherwise, if set to "All Lines" then the
        filter is defined using all the lines in a burst.
    orbit_model_margin
        Additional time to add to the start and end of the orbit model
        generated by the IPF [s]. This provides margin for performing
        interpolation near the boundaries of the sensing start and stop
        times and extrapolation beyond the boundaries of the sensing start
        and stop times. For example, if the sensing start time is Tstart,
        the sensing stop time is Tstop and <orbitModelMargin
        xmlns="">2.0</orbitModelMargin>, then the orbit model generated by
        the IPF will range from (Tstart - 2.0) .. (Tstop + 2.0)
    """

    class Meta:
        name = "commonProcParamsType"

    correct_iqbias_flag: str = field(
        metadata={
            "name": "correctIQBiasFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        }
    )
    correct_iqgain_imbalance_flag: str = field(
        metadata={
            "name": "correctIQGainImbalanceFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        }
    )
    correct_iqorthogonality_flag: str = field(
        metadata={
            "name": "correctIQOrthogonalityFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        }
    )
    correct_bistatic_delay_flag: str = field(
        metadata={
            "name": "correctBistaticDelayFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        }
    )
    correct_bistatic_delay_method: BistaticDelayMethodType = field(
        metadata={
            "name": "correctBistaticDelayMethod",
            "type": "Element",
            "required": True,
        }
    )
    correct_rx_variation_flag: str = field(
        metadata={
            "name": "correctRxVariationFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        }
    )
    ellipsoid_params: EllipsoidParamsType = field(
        metadata={
            "name": "ellipsoidParams",
            "type": "Element",
            "required": True,
        }
    )
    azi_proc_block_params_list: AziProcBlockParamsListType = field(
        metadata={
            "name": "aziProcBlockParamsList",
            "type": "Element",
            "required": True,
        }
    )
    output_mean_expected: Double = field(
        metadata={
            "name": "outputMeanExpected",
            "type": "Element",
            "required": True,
        }
    )
    output_mean_threshold: Double = field(
        metadata={
            "name": "outputMeanThreshold",
            "type": "Element",
            "required": True,
        }
    )
    output_std_dev_expected: Double = field(
        metadata={
            "name": "outputStdDevExpected",
            "type": "Element",
            "required": True,
        }
    )
    output_std_dev_threshold: Double = field(
        metadata={
            "name": "outputStdDevThreshold",
            "type": "Element",
            "required": True,
        }
    )
    tops_filter_convention: TopsFilterConventionType = field(
        metadata={
            "name": "topsFilterConvention",
            "type": "Element",
            "required": True,
        }
    )
    orbit_model_margin: Double = field(
        metadata={
            "name": "orbitModelMargin",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class PostProcParamsType:
    """
    GRD processing auxiliary parameters record.

    Parameters
    ----------
    range_params_list
        Range processing parameters. This list contains the swath-dependent
        auxiliary parameters required for range processing. The list
        contains a separate record for each swath, indexed using the
        applicable swath identifier.
    azimuth_params_list
        Azimuth processing parameters. This list contains the swath-
        dependent auxiliary parameters required for azimuth processing. The
        list contains a separate record for each swath, indexed using the
        applicable swath identifier.
    annotation_vector_step_size
        The decimation factor used on annotation vectors when written to the
        output product. Inside the IPF, each annotation vector could have a
        point for every range sample. To reduce product size, only points
        every annotationVectorStepSize are written to the output annotation
        vectors.
    generate_calibration_luts_flag
        Flag to control the generation of the absolute calilbration LUTs.
        True if the calibration LUTs are to be created, false otherwise.
    apply_azimuth_antenna_pattern_flag
        Azimuth Antenna Pattern Flag. True if the AAP is to be applied,
        false otherwise.
    apply_tops_descalloping_flag
        Perform de-scalloping flag. True if de-scalloping is to be
        performed, false otherwise. This parameter is only applicable to IW
        and EW modes.
    detect_flag
        True to detect power and square root extract measurement data, false
        otherwise.  This flag should only be set to true for GRD products.
    merge_flag
        True to merge the swaths of output data and annotations, false
        otherwise.  Only valid for IW and EW, not applicable to other modes.
        This flag should only be set to true for GRD products.
    create_internal_slcflag
        True if the output of post-processing is an internal SLC product, in
        which case post-processing will pass the input SLC product through
        without applying further processing.
    grd_proc_params
        GRD processing auxiliary parameters. This record contains the
        auxiliary parameters required during GRD image processing.
    create_ql_image_flag
        Create Quick-look product flag. This flag controls the creation of a
        Quick-look image. It is set to true if a Quick-look image should be
        created; or, false otherwise.
    ql_proc_params
        Quick-look processing auxiliary parameters. This record contains the
        auxiliary parameters required during Quick-look image processing.
        This structure need only be present if the createQlImageFlag is
        true.
    """

    class Meta:
        name = "postProcParamsType"

    range_params_list: RangeParamsListType = field(
        metadata={
            "name": "rangeParamsList",
            "type": "Element",
            "required": True,
        }
    )
    azimuth_params_list: AzimuthParamsListType = field(
        metadata={
            "name": "azimuthParamsList",
            "type": "Element",
            "required": True,
        }
    )
    annotation_vector_step_size: Uint32 = field(
        metadata={
            "name": "annotationVectorStepSize",
            "type": "Element",
            "required": True,
        }
    )
    generate_calibration_luts_flag: str = field(
        metadata={
            "name": "generateCalibrationLutsFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        }
    )
    apply_azimuth_antenna_pattern_flag: str = field(
        metadata={
            "name": "applyAzimuthAntennaPatternFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        }
    )
    apply_tops_descalloping_flag: str = field(
        metadata={
            "name": "applyTopsDescallopingFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        }
    )
    detect_flag: str = field(
        metadata={
            "name": "detectFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        }
    )
    merge_flag: str = field(
        metadata={
            "name": "mergeFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        }
    )
    create_internal_slcflag: str = field(
        metadata={
            "name": "createInternalSLCFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        }
    )
    grd_proc_params: GrdProcParamsType = field(
        metadata={
            "name": "grdProcParams",
            "type": "Element",
            "required": True,
        }
    )
    create_ql_image_flag: str = field(
        metadata={
            "name": "createQlImageFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        }
    )
    ql_proc_params: QlProcParamsType = field(
        metadata={
            "name": "qlProcParams",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class SlcProcParamsType:
    """
    SLC processing auxiliary parameters record.

    Parameters
    ----------
    apply_elevation_antenna_pattern_flag
        Elevation antenna pattern correction flag. True if the EAP is to be
        applied, false otherwise.
    apply_range_spreading_loss_flag
        Range spreading loss correction flag. True if the RSL is to be
        applied, false otherwise.
    estimate_thermal_noise_flag
        Thermal noise estimation flag. True if thermal noise estimation is
        to be performed, false otherwise.
    rrf_spectrum
        The type of range matched filter to use during processing.
        "Unextended": range reference function is unextended in frequency
        domain; "Extended Flat": range reference function is extended and
        flat in frequency domain; and, "Extended Tapered": range reference
        function is extended and tapered in frequency domain.
    swath_params_list
        List of azimuth processing bandwidths. There is an entry for each
        relevant swath within the product.
    """

    class Meta:
        name = "slcProcParamsType"

    apply_elevation_antenna_pattern_flag: str = field(
        metadata={
            "name": "applyElevationAntennaPatternFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        }
    )
    apply_range_spreading_loss_flag: str = field(
        metadata={
            "name": "applyRangeSpreadingLossFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        }
    )
    estimate_thermal_noise_flag: str = field(
        metadata={
            "name": "estimateThermalNoiseFlag",
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        }
    )
    rrf_spectrum: RrfSpectrumType = field(
        metadata={
            "name": "rrfSpectrum",
            "type": "Element",
            "required": True,
        }
    )
    swath_params_list: SlcSwathParamsListType = field(
        metadata={
            "name": "swathParamsList",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class ApplicationLutListType:
    """
    List of application LUT records.

    Parameters
    ----------
    application_lut
        Application LUT record. This element contains the information
        required to identify the application scaling LUT specified in the
        Job Order. The ICD currently defines four default application
        scaling LUTs, one for each mode.  However, more can be added, so
        long as the applicationLutId matches the Application_LUT processing
        parameter in the Job Order.
    count
        Number of applicationLut records in the list.
    """

    class Meta:
        name = "applicationLutListType"

    application_lut: tuple[ApplicationLutType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "applicationLut",
            "type": "Element",
            "min_occurs": 2,
            "max_occurs": 20,
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
class L1ProductType:
    """
    Standard L1 product record that holds the all the applicable auxiliary data for
    this product type.

    Parameters
    ----------
    product_id
        Product type identifier to which this set of parameters applies. The
        productId is used to index and find the correct set of auxiliary
        parameters for each product the IPF is capable of generating.  This
        field corresponds to the first 9 characters of the product type
        identifiers listed in the Job Order File_Type field.  For example,
        the S1 IPF ICD [A-7] defines a product identifier for SM SLC
        standard products as “SM_SLC__1S”, so the parameters that correspond
        to this product are identified by the string “SM_SLC__1”.
    common_proc_params
        Common processing auxiliary parameters. This record holds the
        parameters that are common among multiple steps in the image
        processing chain.
    pre_proc_params
        Pre-processing auxiliary parameters. This record contains the
        auxiliary parameters required during image pre-processing.
    dc_proc_params
        Doppler centroid processing auxiliary parameters. This record
        contains the auxiliary parameters required during Doppler centroid
        processing.
    slc_proc_params
        SLC processing auxiliary parameters. This record contains the
        auxiliary parameters required during SLC image processing.
    post_proc_params
        Post processing auxiliary parameters. This record contains the
        auxiliary parameters required during image post processing. This
        includes: SLC post-processing, GRD processing; Browse processing;
        and, Quick-look image processing.
    """

    class Meta:
        name = "l1ProductType"

    product_id: str = field(
        metadata={
            "name": "productId",
            "type": "Element",
            "required": True,
        }
    )
    common_proc_params: Optional[CommonProcParamsType] = field(
        default=None,
        metadata={
            "name": "commonProcParams",
            "type": "Element",
        },
    )
    pre_proc_params: Optional[PreProcParamsType] = field(
        default=None,
        metadata={
            "name": "preProcParams",
            "type": "Element",
        },
    )
    dc_proc_params: Optional[DcProcParamsType] = field(
        default=None,
        metadata={
            "name": "dcProcParams",
            "type": "Element",
        },
    )
    slc_proc_params: Optional[SlcProcParamsType] = field(
        default=None,
        metadata={
            "name": "slcProcParams",
            "type": "Element",
        },
    )
    post_proc_params: Optional[PostProcParamsType] = field(
        default=None,
        metadata={
            "name": "postProcParams",
            "type": "Element",
        },
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class L1ProductListType:
    """
    Auxiliary parameters list for standard products.

    Parameters
    ----------
    product
        Product auxiliary parameters. This DSR contains all of the auxiliary
        parameters required to process a single product. The parameters are
        stored in structures that are grouped together by the logical
        processing steps used during image creation. The parameters within
        this DSR and its children are not polarisation dependent and in
        general apply to the entire product; however, in some cases a
        distinction must be made amongst swaths and when this is necessary
        the records are indexed with a swath identifier.  There are 16
        standard product types defined in the ICD [A-7] for the IPF so in
        general there will be 16 product type entries in the list, however
        more products can be defined and therefore more than 16 product
        types are allowed in this list.
    count
        The number of elements contained in the list. There is an entry for
        each standard L1 product type that the IPF is capable of generating.
    """

    class Meta:
        name = "l1ProductListType"

    product: tuple[L1ProductType, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 48,
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
class L1AuxiliaryProcessorParametersType:
    """
    Sentinel-1 IPF L1 processing parameters auxiliary file specification.

    Parameters
    ----------
    product_list
        List of L1 products containing the applicable auxiliary parameters
        for each. This list contains an entry for each product the IPF is
        capable of generating, indexed by its unique product identifier.
    application_lut_list
        List of application LUTs. This element is a list of all available
        application LUTs. The application identifier used to index the list
        comes from the Job Order.
    schema_version
    """

    class Meta:
        name = "l1AuxiliaryProcessorParametersType"

    product_list: L1ProductListType = field(
        metadata={
            "name": "productList",
            "type": "Element",
            "required": True,
        }
    )
    application_lut_list: ApplicationLutListType = field(
        metadata={
            "name": "applicationLutList",
            "type": "Element",
            "required": True,
        }
    )
    schema_version: Decimal = field(
        init=False,
        default=Decimal("3.3"),
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class L1AuxiliaryProcessorParameters(L1AuxiliaryProcessorParametersType):
    """
    L1 Processor parameters auxiliary file definition (AUX_PP1).
    """

    class Meta:
        name = "l1AuxiliaryProcessorParameters"
