from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Tuple

from .s1_object_types import (
    BandwidthType,
    BaqCodeType,
    CalCombinationMethodType,
    Complex,
    ComplexArray,
    Double,
    DoubleArray,
    DoubleCoefficientArray,
    Float,
    FloatArray,
    FloatCoefficientArray,
    Int32,
    IntArray,
    PolarisationType,
    RxPolarisationType,
    SensorModeType,
    SignalType,
    SwathType,
    Uint32,
)


@dataclass(frozen=True, slots=True, kw_only=True)
class HuffmanLutType:
    """
    Huffman decoding LUT record.

    Parameters
    ----------
    baq_code
        Bit Rate Code (as extracted from the BAQ block) to which this LUT
        applies.
    values
        Huffman binary decoding tree values. The tree is implemented using a
        simple binary coding in which starting at the root, the left side is
        defined and then the right side is defined. Each node is identified
        by a 0 followed by a 0 or 1 representing the value of the node. Each
        leaf is identified by a 1 followed by a 0 or 1 representing the
        value of the leaf followed by 4 bits representing the MCode value.
        This encoding scheme is a proposal and will be confirmed prior to
        CDR.
    """

    class Meta:
        name = "huffmanLutType"

    baq_code: BaqCodeType = field(
        metadata={
            "name": "baqCode",
            "type": "Element",
            "required": True,
        }
    )
    values: IntArray = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class IspType:
    """
    ISP record.

    Parameters
    ----------
    swath
        Canonical name of the swath used to acquire the packet(s).
    signal
        Signal type.
    bandwidth
        Signal bandwidth.
    num_pri
        The number of packets of this signal type expected in series.
    """

    class Meta:
        name = "ispType"

    swath: SwathType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    signal: SignalType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    bandwidth: BandwidthType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    num_pri: Uint32 = field(
        metadata={
            "name": "numPri",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class OnBoardDecimationFilterPowTransferFun:
    """
    On-board decimation filter power transfer function.

    Parameters
    ----------
    frequency_increment
        The frequency increment.
    values
        Power transfer function coefficients.
    """

    class Meta:
        name = "onBoardDecimationFilterPowTransferFun"

    frequency_increment: Float = field(
        metadata={
            "name": "frequencyIncrement",
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
class PccParamsType:
    """
    PCC decoding control parameters.

    Parameters
    ----------
    signal
        Signal type.
    order
        PCC pulse selection order. This is a list of integers separated by
        spaces that defines the order in which the pulses are combined using
        the method below. For example, an entry of: &lt;order
        count="2"&gt;20 19&lt;/order&gt; will select the 20th pulse first
        and the 19th pulse second.
    method
        Method to use to combine the calibration pulses selected by the
        order above. The PCC2 method subtracts the pulses in order and
        averages over the number of pulses. The Average method add the
        pulses in order and averages over the number of pulses. The
        Isolation Subtraction method finds the corresponding isolation pulse
        PCC params and subtracts the selected isolation pulse from the
        selected nominal pulse.
    """

    class Meta:
        name = "pccParamsType"

    signal: SignalType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    order: IntArray = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    method: CalCombinationMethodType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class PgProductModelType:
    """
    Modeled PG Product LUT.

    Parameters
    ----------
    pg_model_interval
        Interval between adjacent PG Product values in the list [s].
    values
        Array of modeled complex PG model values.  The pattern contains
        attribute "count" complex floating point values separated by spaces.
        The first value in the array corresponds to the time at the
        ascending node of the current orbit.
    """

    class Meta:
        name = "pgProductModelType"

    pg_model_interval: Double = field(
        metadata={
            "name": "pgModelInterval",
            "type": "Element",
            "required": True,
        }
    )
    values: ComplexArray = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class PulseParamsType:
    """
    Pulse parameters record.

    Parameters
    ----------
    amplitude_coefficients
        Pulse amplitude coefficients of the nominal imaging chirp replica.
    phase_coefficients
        Pulse phase coefficients of the nominal imaging chirp replica.
    nominal_tx_pulse_length
        Nominal transmit pulse length [s]. This parameter is used by the
        pre-processor and the DCE and SLC processors if it is smaller than
        the Tx Pulse Length (TXPL) extracted from the ISP headers. The
        nominal transmit pulse length can be set such that the chirp
        processed bandwidth is small enough to filter out the spurious
        signals at ±37.5 MHz. Note that if the value of this field is less
        than or equal to 0, then it is ignored by the IPF and the transmit
        pulse length extracted from the ISP headers is used.
    """

    class Meta:
        name = "pulseParamsType"

    amplitude_coefficients: FloatCoefficientArray = field(
        metadata={
            "name": "amplitudeCoefficients",
            "type": "Element",
            "required": True,
        }
    )
    phase_coefficients: FloatCoefficientArray = field(
        metadata={
            "name": "phaseCoefficients",
            "type": "Element",
            "required": True,
        }
    )
    nominal_tx_pulse_length: Double = field(
        metadata={
            "name": "nominalTxPulseLength",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class RadarParamsType:
    """
    Radar parameters record.

    Parameters
    ----------
    azimuth_steering_rate
        TOPSAR azimuth steering rate [degrees/s]. This field is only
        relevant for IW and EW swaths and is ignored for SM and WV swaths.
    """

    class Meta:
        name = "radarParamsType"

    azimuth_steering_rate: Double = field(
        metadata={
            "name": "azimuthSteeringRate",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class RadarSamplingRateType:
    """
    Radar sampling rate type.

    Parameters
    ----------
    swath
        Swath to which this radar sampling rate applies.
    value
        Radar sampling rate [Hz].
    """

    class Meta:
        name = "radarSamplingRateType"

    swath: SwathType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    value: Double = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class RlLutType:
    """
    Reconstruction Level LUT type for definition the Simple and Normalized
    Reconstruction LUTs.

    Parameters
    ----------
    baq_code
        Index code for which the LUT applies. For FDBAQ compression this is
        the Bit Rate Code extracted from the BAQ block and for BAQ
        compression this is the BAQ mode.
    values
        NRL LUT values. This element contains fifteen double precision
        floating point values separated by spaces, one entry for each MCode
        value. Note that some MCodes are not applicable for some FDBAQ and
        BAQ modes so in this case the entry shall be "NaN" to signify an
        invalid index.
    """

    class Meta:
        name = "rlLutType"

    baq_code: BaqCodeType = field(
        metadata={
            "name": "baqCode",
            "type": "Element",
            "required": True,
        }
    )
    values: DoubleArray = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class RollSteeringParamsType:
    """
    Roll steering parameters.

    Parameters
    ----------
    reference_antenna_angle
        Antenna bore sight off nadir angle at the referenceHeight [degrees].
    reference_height
        Satellite height at which the instrument elevation angle is aligned
        with the referenceAntennaAngle [m].
    roll_steering_sensitivity
        Sensitivity of the roll steering versus height [degrees/m].
    """

    class Meta:
        name = "rollSteeringParamsType"

    reference_antenna_angle: Double = field(
        metadata={
            "name": "referenceAntennaAngle",
            "type": "Element",
            "required": True,
        }
    )
    reference_height: Double = field(
        metadata={
            "name": "referenceHeight",
            "type": "Element",
            "required": True,
        }
    )
    roll_steering_sensitivity: Double = field(
        metadata={
            "name": "rollSteeringSensitivity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class RxVariationCorrectionParamsType:
    """
    Receive variation correction parameters record.

    Parameters
    ----------
    rx_polarisation
        Polarisation to which this set of receive correction parameters
        applies. "H" or "V".
    gain_trend_coefficients
        Gain trend correction coefficients.
    gain_overshoot_coefficients
        Gain overshoot correction coefficients.
    """

    class Meta:
        name = "rxVariationCorrectionParamsType"

    rx_polarisation: RxPolarisationType = field(
        metadata={
            "name": "rxPolarisation",
            "type": "Element",
            "required": True,
        }
    )
    gain_trend_coefficients: DoubleCoefficientArray = field(
        metadata={
            "name": "gainTrendCoefficients",
            "type": "Element",
            "required": True,
        }
    )
    gain_overshoot_coefficients: DoubleCoefficientArray = field(
        metadata={
            "name": "gainOvershootCoefficients",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class SwathMapType:
    """
    Parameters for mapping swath numbers to canonical swath names.

    Parameters
    ----------
    swath_number
        The swath number from the source packet header to map to a
        particular logical swath within the instrument mode.
    swath
        The logical swath to which the swath number applies.
    """

    class Meta:
        name = "swathMapType"

    swath_number: int = field(
        metadata={
            "name": "swathNumber",
            "type": "Element",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 127,
        }
    )
    swath: SwathType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class ThresholdLutType:
    """
    Raw data decoding configuration parameters.

    Parameters
    ----------
    baq_code
        BAQ-mode/FDBAQ-BRC to which this set of thresholds applies.
    thidx_threshold
        THIDX threshold used to determine whether to use the simple
        reconstruction method or the normal reconstruction method. If the
        THIDX extracted from the data is less than or equal to this
        threshold, then the simple reconstruction method is used; otherwise,
        the normal reconstruction method is used.
    m_code_threshold
        Mcode threshold used in simple reconstruction to determine whether
        to use the extracted Mcode or the the simple reconstruction LUT. If
        the Mcode extracted from the data is less than this threshold, then
        the extracted Mcode is used; otherwise, the simple reconstruction
        LUT is used.
    """

    class Meta:
        name = "thresholdLutType"

    baq_code: BaqCodeType = field(
        metadata={
            "name": "baqCode",
            "type": "Element",
            "required": True,
        }
    )
    thidx_threshold: Int32 = field(
        metadata={
            "name": "thidxThreshold",
            "type": "Element",
            "required": True,
        }
    )
    m_code_threshold: Int32 = field(
        metadata={
            "name": "mCodeThreshold",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class HuffmanLutListType:
    """
    List of Huffman decoding LUTs.

    Parameters
    ----------
    huffman_lut
        Huffman decoding LUT. This element contains the Huffman binary tree
        values for the applicable Bit Rate Code. The MCode is recovered by
        applying the values in the decoding LUT to the extracted HCode.
    count
        Number of Huffan decoding LUTs in the list.
    """

    class Meta:
        name = "huffmanLutListType"

    huffman_lut: Tuple[HuffmanLutType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "huffmanLut",
            "type": "Element",
            "min_occurs": 5,
            "max_occurs": 5,
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
class IspListType:
    """
    List of ISP records.

    Parameters
    ----------
    isp
        The ISP element describes one unique, or a series of unique
        transmission packets. The packets are identified by the packet
        signal type and contain the number of PRIs expected ifor this packet
        type.
    count
        The number of ISP records within the list.
    """

    class Meta:
        name = "ispListType"

    isp: Tuple[IspType, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 100,
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
class OnBoardDecimationFilterParamsType:
    """
    On-board decimation filter record.

    Parameters
    ----------
    rx_polarisation
        Polarisation to which this set of parameters applies. "H" or "V".
    power_transfer_function
        Power transfer function characterization of the on-board decimation
        filter
    spurious_frequencies
        List of the known spurious frequencies.
    """

    class Meta:
        name = "onBoardDecimationFilterParamsType"

    rx_polarisation: RxPolarisationType = field(
        metadata={
            "name": "rxPolarisation",
            "type": "Element",
            "required": True,
        }
    )
    power_transfer_function: OnBoardDecimationFilterPowTransferFun = field(
        metadata={
            "name": "powerTransferFunction",
            "type": "Element",
            "required": True,
        }
    )
    spurious_frequencies: FloatArray = field(
        metadata={
            "name": "spuriousFrequencies",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class PccParamsListType:
    """
    List of PCC decoding control parameters indexed by signal type.

    Parameters
    ----------
    pcc_params
        PCC decoding parameters for controlling the order and way in which
        calibration pulses are decoded during processing. There are a
        minimum of 5 entries in the list, one for each nominal calibration
        pulse, and a maximum of 6 entries in the list for the transmit H
        polarisation which includes an additional isolation pulse.
    count
        Number of pccParams records in the list.
    """

    class Meta:
        name = "pccParamsListType"

    pcc_params: Tuple[PccParamsType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "pccParams",
            "type": "Element",
            "min_occurs": 5,
            "max_occurs": 6,
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
class RlLutListType:
    """
    List of Reconstruction Level LUTs.

    Parameters
    ----------
    rl_lut
        Normalised Reconstruction Levels LUT. This LUT contains the NRL
        values used to retrieve the normalised reconstructed sample values
        from the BAQ encoded data. The NRL in the table are indexed by: 1-
        the Bit Rate Code extracted from the BAQ data block for FDBAQ
        compression; and, 2- the BAQ mode (3-bit, 4-bit or 5-bit) for BAQ
        compression.
    count
        Number of NRL LUTs in the list.
    """

    class Meta:
        name = "rlLutListType"

    rl_lut: Tuple[RlLutType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "rlLut",
            "type": "Element",
            "min_occurs": 8,
            "max_occurs": 8,
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
class RxVariationCorrectionParamsListType:
    """
    List of Receive variation correction parameters.

    Parameters
    ----------
    rx_variation_correction_params
        Receive variation correction parameters record. This record contains
        the coefficients used to correct the gain variation across the
        receive window. There is one record per receive polarisation.
    count
        Number of rxVariationCorrectionParams records in the list.
    """

    class Meta:
        name = "rxVariationCorrectionParamsListType"

    rx_variation_correction_params: Tuple[
        RxVariationCorrectionParamsType, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "rxVariationCorrectionParams",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
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
class SwathMapListType:
    """
    List of swath mapping parameters indexed by swath name.

    Parameters
    ----------
    swath_map
        Provides a mapping bewteen a particular swath number from the source
        packet headers to a logical swath within the instrument mode.  In
        theory the swath number can vary by signal type so the maximum
        number of swath map elements is 5 swaths * 8 signal types = 40
        records. This is the worst case for EW.
    count
        Number of swathMap records in the list
    """

    class Meta:
        name = "swathMapListType"

    swath_map: Tuple[SwathMapType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "swathMap",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 40,
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
class ThresholdLutListType:
    """
    List of raw data decoding configuration parameters indexed by encoding mode.

    Parameters
    ----------
    threshold_lut
        Threshold LUT containing the thresholds needed to decode the BAQ and
        FDBAQ encoded data. There is one record for each of the BAQ-
        modes/FDBAQ-BRCs for a total of 8.
    count
        Number of thresholdLut records in the list.
    """

    class Meta:
        name = "thresholdLutListType"

    threshold_lut: Tuple[ThresholdLutType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "thresholdLut",
            "type": "Element",
            "min_occurs": 8,
            "max_occurs": 8,
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
class DecodingParamsType:
    """
    List of FDBAQ Lookup Tables.

    Parameters
    ----------
    huffman_lut_list
        Huffman decoding LUT list. This element contains the Huffman
        decoding LUTs required to retrieve the HCode value from FDBAQ
        encoded user data.  There is one LUT for each Bit Rate Code for a
        total of 5.
    nrl_lut_list
        Normalised Reconstruction Levels LUT list. This element contains the
        NRL LUTs required to retrieve the normalised reconstructed sample
        values from the BAQ encoded data. There is one LUT per BAQ
        mode/FDBAQ Bit Rate Code for a total of 8 LUTs.
    srl_lut_list
        Simple Reconstruction Parameters LUT list. This element contains the
        Simple Reconstruction Parameters LUTs required to retrieve the
        simple reconstructed sample values from the BAQ encoded data. There
        is one LUT per BAQ mode/FDBAQ Bit Rate Code for a total of 8 LUTs.
    sigma_factor_lut
        Sigma Factors LUT. This LUT contains the values used to upscale the
        normalised reconstructed samples. The sigma factors in the table are
        indexed by the Threshold Index (THIDX) extracted from the BAQ block.
        This vector contains 255 single precision floating point numbers
        separated by spaces.
    threshold_lut_list
        Raw data decoding control LUT list. This element contains the
        parameters required to decode the BAQ and FDBAQ encoded data.
    tgu_lut
        TGU temperature calibration LUT used to convert the TGU temperature
        codes extracted from the sub-commutated ancillary data into the
        correct temperature values. This is a list of 128 floating point
        numbers separated by spaces with the index of each entry, numbered 0
        .. 127, corresponding to the code for which the temperature value
        applies.
    tile_lut
        Tile temperature calibration LUT used to convert the Tile
        temperature codes extracted from the sub-commutated ancillary data
        into the correct temperature values. This is a list of 256 floating
        point numbers separated by spaces with the index of each entry,
        numbered 0 .. 255, corresponding to the code for which the
        temperature value applies.
    """

    class Meta:
        name = "decodingParamsType"

    huffman_lut_list: HuffmanLutListType = field(
        metadata={
            "name": "huffmanLutList",
            "type": "Element",
            "required": True,
        }
    )
    nrl_lut_list: RlLutListType = field(
        metadata={
            "name": "nrlLutList",
            "type": "Element",
            "required": True,
        }
    )
    srl_lut_list: RlLutListType = field(
        metadata={
            "name": "srlLutList",
            "type": "Element",
            "required": True,
        }
    )
    sigma_factor_lut: FloatArray = field(
        metadata={
            "name": "sigmaFactorLut",
            "type": "Element",
            "required": True,
        }
    )
    threshold_lut_list: ThresholdLutListType = field(
        metadata={
            "name": "thresholdLutList",
            "type": "Element",
            "required": True,
        }
    )
    tgu_lut: FloatArray = field(
        metadata={
            "name": "tguLut",
            "type": "Element",
            "required": True,
        }
    )
    tile_lut: FloatArray = field(
        metadata={
            "name": "tileLut",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class InternalCalibrationParamsType:
    """
    Channel dependent instrument parameters.

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
    time_delay
        Time delay [s] to be applied to the reference replica, used when the
        time delay cannot be derived from the extracted replica.
    nominal_gain
        Complex gain to be applied to the reference replica when derived
        from the nominal chirp.
    extracted_gain
        Complex gain to be applied to the reference replica when derived
        from the extracted chirp.
    pg_product_model
        Modeled PG product.  The model is relative to the ascending node of
        the current orbit.
    pg_reference
        Reference absolute PG value that will be defined by offline analysis
        of the acquired data.  PG values used by the IPF will be normalised
        by this PG reference value.
    swst_bias
        SWST bias [s].
    azimuth_time_bias
        Azimuth time bias [s].
    noise
        Nominal noise value used in processing if no noise value can be
        calculated from the downlink.
    replica_pcc_params_list
        List of PCC decoding control parameters for the extracted replicas
        at nominal imaging bandwidth.
    pg_pcc_params_list
        List of PCC decoding control parameters for the PG replicas at 100
        MHz bandwidth.
    """

    class Meta:
        name = "internalCalibrationParamsType"

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
    time_delay: Double = field(
        metadata={
            "name": "timeDelay",
            "type": "Element",
            "required": True,
        }
    )
    nominal_gain: Complex = field(
        metadata={
            "name": "nominalGain",
            "type": "Element",
            "required": True,
        }
    )
    extracted_gain: Complex = field(
        metadata={
            "name": "extractedGain",
            "type": "Element",
            "required": True,
        }
    )
    pg_product_model: PgProductModelType = field(
        metadata={
            "name": "pgProductModel",
            "type": "Element",
            "required": True,
        }
    )
    pg_reference: Complex = field(
        metadata={
            "name": "pgReference",
            "type": "Element",
            "required": True,
        }
    )
    swst_bias: Double = field(
        metadata={
            "name": "swstBias",
            "type": "Element",
            "required": True,
        }
    )
    azimuth_time_bias: Double = field(
        metadata={
            "name": "azimuthTimeBias",
            "type": "Element",
            "required": True,
        }
    )
    noise: Double = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    replica_pcc_params_list: PccParamsListType = field(
        metadata={
            "name": "replicaPccParamsList",
            "type": "Element",
            "required": True,
        }
    )
    pg_pcc_params_list: PccParamsListType = field(
        metadata={
            "name": "pgPccParamsList",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class OnBoardDecimationFilterParamsListType:
    """
    List of on-board decimation filter parameters.

    Parameters
    ----------
    on_board_decimation_filter_params
        On-board decimation filter record. This record contains the power-
        transfer function of the filter and its known spurious frequencies.
    count
        Number of onBoardDecimationFilterParams records in the list.
    """

    class Meta:
        name = "onBoardDecimationFilterParamsListType"

    on_board_decimation_filter_params: Tuple[
        OnBoardDecimationFilterParamsType, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "onBoardDecimationFilterParams",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
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
class SequenceType:
    """
    ISP sequence record.

    Parameters
    ----------
    name
        The name of the activity within the data acquisition to which this
        sequence belongs. This field is not used by the IPF for processing.
        It is for informative purposes only and so the range of the field is
        unbounded.
    repeat
        Sequence repeat flag. For the imaging sequence, this field shall be
        set to “true” to indentify the ispList that represents the imaging
        operation. This field shall be set to “false” for all other
        sequences.
    isp_list
        ISP list. This element contains contains a list of the expected
        packets within this sequence in the order they should be received.
        The number of ISP entries is arbitrary but there are 30 slots
        defined to capture the worst case EW echo acquisition with PCC2
        sequences at the end of each burst.
    """

    class Meta:
        name = "sequenceType"

    name: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    repeat: str = field(
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"(false)|(true)",
        }
    )
    isp_list: IspListType = field(
        metadata={
            "name": "ispList",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class InternalCalibrationParamsListType:
    """Internal calibration parameters list.

    This element contains a list of swath/polarisation channel dependent
    instrument parameters. There is an entry for each swath/polarisation
    combination for a total of 60. The SPPDU document defines an
    additional 68 swath number codes that can be used if required.

    Parameters
    ----------
    internal_calibration_params
        Internal calibration instrument parameters. This record contains
        swath/polarisation channel dependent parameters related to the
        instrument. There may be up to one record per swath (23 nominal
        swaths) per polarisation (4 polarisation combinations for SM, IW,
        EW, EN and AN, 2 for WV) for a maximum total of 88.
    count
        Number of internalCalibrationParam records in the list.
    """

    class Meta:
        name = "internalCalibrationParamsListType"

    internal_calibration_params: Tuple[InternalCalibrationParamsType, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "internalCalibrationParams",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 88,
            },
        )
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
class SequenceListType:
    """
    List of ISP sequences.

    Parameters
    ----------
    sequence
        This record defines the sequence of expected ISPs for one distinct
        activity within the data take.  The number of sequences is arbitrary
        but there are 5 slots nominally allocated for: 1. an initial noise
        measurement sequence; 2. an initial calibration sequence; 3. an
        image acquisition sequence; 4. a final calibration sequence; and, 5.
        a final noise measurement sequence.
    count
        Number of sequence entries in the list.
    """

    class Meta:
        name = "sequenceListType"

    sequence: Tuple[SequenceType, ...] = field(
        default_factory=tuple,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 5,
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
class SwathParamsType:
    """
    Swath parameters record.

    Parameters
    ----------
    swath
        Canonical name of the swath to which this set of swathParams
        applies.
    radar_params
        This DSR contains information related to the SAR instrument
    pulse_params
        Replica pulse parameters. This DSR contains the characteristics for
        the nominal replica pulse within this swath.
    rx_variation_correction_params_list
        List of the receive variation correction parameters used to correct
        the gain variation across the receive window.
    on_board_decimation_filter_params_list
        List of the on-board decimation filter parameters.
    """

    class Meta:
        name = "swathParamsType"

    swath: SwathType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    radar_params: RadarParamsType = field(
        metadata={
            "name": "radarParams",
            "type": "Element",
            "required": True,
        }
    )
    pulse_params: PulseParamsType = field(
        metadata={
            "name": "pulseParams",
            "type": "Element",
            "required": True,
        }
    )
    rx_variation_correction_params_list: RxVariationCorrectionParamsListType = field(
        metadata={
            "name": "rxVariationCorrectionParamsList",
            "type": "Element",
            "required": True,
        }
    )
    on_board_decimation_filter_params_list: Optional[
        OnBoardDecimationFilterParamsListType
    ] = field(
        default=None,
        metadata={
            "name": "onBoardDecimationFilterParamsList",
            "type": "Element",
        },
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class SwathParamsListType:
    """
    List of swath parameters.

    Parameters
    ----------
    swath_params
        Swath Parameters. This record contains swath-dependent parameters
        related to the instrument. There may be up to one record per swath
        for a maximum total of 23 records.
    count
        Number of swathParams records in the list.
    """

    class Meta:
        name = "swathParamsListType"

    swath_params: Tuple[SwathParamsType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "swathParams",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 23,
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
class TimelineType:
    """
    Timeline ECC program parameters record.

    Parameters
    ----------
    ecc_number
        Event Control Code (ECC) number. This field uniquely identifies the
        ECC program number for this instrument mode and is used by the IPF
        for timeline selection.
    mode
        Instrument mode. This field identifies the instrument mode to which
        this timeline entry applies.
    sequence_list
        Sequence list. This element is a list of activity sequences that
        together form the expected transmission sequence from the SAR
        instrument for the data take.
    swath_map_list
        Swath mapping list. This element is a list of the swaths applicable
        to this ECC program and provides a mapping between the swath number
        fields in the source packet headers and the logical instrument swath
        name to which they apply.
    """

    class Meta:
        name = "timelineType"

    ecc_number: int = field(
        metadata={
            "name": "eccNumber",
            "type": "Element",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 47,
        }
    )
    mode: SensorModeType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    sequence_list: SequenceListType = field(
        metadata={
            "name": "sequenceList",
            "type": "Element",
            "required": True,
        }
    )
    swath_map_list: SwathMapListType = field(
        metadata={
            "name": "swathMapList",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class TimelineListType:
    """
    List of timeline ECC Program parameters records.

    Parameters
    ----------
    timeline
        Each timeline element describes the expected packet transmission
        sequence for one of the operational modes of the satellite.  The
        SPPDU [A-12] allows for up to 48 entries numbered from 0-47. At
        minimum, this list must include an entry for the mode of the data
        being processed.
    count
        Number of timeline entries in the list.
    """

    class Meta:
        name = "timelineListType"

    timeline: Tuple[TimelineType, ...] = field(
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
class AuxiliaryInstrumentType:
    """Instrument auxiliary file definition (AUX_INS).

    This file includes information related to the instrument required
    for processing.  It is required for data decompression and ISP
    decoding.

    Parameters
    ----------
    radar_frequency
        Radar frequency [Hz].
    delta_tguard1
        DeltaT Guard 1 parameter from the instrument radar database [s].
        This parameter is used to calculate the internal time delay of the
        extracted reconstructed replicas.
    delta_tsuppr
        DeltaT Suppr parameter from the SSPPDU document [s]. This parameter
        is used to calculate the times within the PRI for the echo,
        calibration and noise data.
    delta_txlatch
        The time difference between the TX pulse and the latch time as
        annotated in the radar database [s]. This parameter is used to apply
        the instrument timing correction.
    roll_steering_params
        Parameters related to the roll steering law for the instrument. The
        roll steering law defines the off nadir pointing of the antenna
        mechanical bore sight versus time.
    swath_params_list
        Swath parameters list. This element contains a list of swath
        dependent instrument parameters.
    internal_calibration_params_list
        Internal calibration parameters list. This element contains a list
        of swath/polarisation channel dependent instrument parameters.
    timeline_list
        Timeline list. This element contains a list of records that describe
        the expected packet transmission sequence for each of the Sentinel-1
        SAR modes.
    decoding_params
        Raw data decoding parameters. This DSR contains the tables and
        parameters that the IPF requires to perform image processing.
    schema_version
    """

    class Meta:
        name = "auxiliaryInstrumentType"

    radar_frequency: Double = field(
        metadata={
            "name": "radarFrequency",
            "type": "Element",
            "required": True,
        }
    )
    delta_tguard1: Double = field(
        metadata={
            "name": "deltaTGuard1",
            "type": "Element",
            "required": True,
        }
    )
    delta_tsuppr: Double = field(
        metadata={
            "name": "deltaTSuppr",
            "type": "Element",
            "required": True,
        }
    )
    delta_txlatch: Double = field(
        metadata={
            "name": "deltaTXLatch",
            "type": "Element",
            "required": True,
        }
    )
    roll_steering_params: RollSteeringParamsType = field(
        metadata={
            "name": "rollSteeringParams",
            "type": "Element",
            "required": True,
        }
    )
    swath_params_list: SwathParamsListType = field(
        metadata={
            "name": "swathParamsList",
            "type": "Element",
            "required": True,
        }
    )
    internal_calibration_params_list: InternalCalibrationParamsListType = (
        field(
            metadata={
                "name": "internalCalibrationParamsList",
                "type": "Element",
                "required": True,
            }
        )
    )
    timeline_list: TimelineListType = field(
        metadata={
            "name": "timelineList",
            "type": "Element",
            "required": True,
        }
    )
    decoding_params: DecodingParamsType = field(
        metadata={
            "name": "decodingParams",
            "type": "Element",
            "required": True,
        }
    )
    schema_version: Decimal = field(
        init=False,
        default=Decimal("3.7"),
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class AuxiliaryInstrument(AuxiliaryInstrumentType):
    """Instrument auxiliary file definition (AUX_INS).

    This file includes information related to the instrument required
    for processing.  It is required for data decompression and ISP
    decoding.
    """

    class Meta:
        name = "auxiliaryInstrument"
