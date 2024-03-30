from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from xsdata.models.datatype import XmlDateTime


class RfimitigationDomainType(Enum):
    """
    Enumeration of RFI mitigation domains.
    """

    TIME = "Time"
    FREQUENCY = "Frequency"
    TIME_AND_FREQUENCY = "TimeAndFrequency"


class RfimitigationPerformedType(Enum):
    """
    Enumeration of RFI mitigation policies.
    """

    NEVER = "Never"
    ALWAYS = "Always"
    BASED_ON_NOISE_MEAS = "BasedOnNoiseMeas"


class BandwidthType(Enum):
    """
    Enumeration of the available bandwidths for SAR signals in the timeline.
    """

    IMAGE = "Image"
    FULL = "Full"


class BaqCodeType(Enum):
    """
    Enumeration of BAQ/FDBAQ LUT index codes.
    """

    BAQ_3_BIT = "BAQ 3-Bit"
    BAQ_4_BIT = "BAQ 4-Bit"
    BAQ_5_BIT = "BAQ 5-Bit"
    BRC_0 = "BRC 0"
    BRC_1 = "BRC 1"
    BRC_2 = "BRC 2"
    BRC_3 = "BRC 3"
    BRC_4 = "BRC 4"


class BistaticDelayMethodType(Enum):
    """
    Enumeration of bi-static delay compensation methods.
    """

    FINE = "Fine"
    COARSE = "Coarse"


class CalCombinationMethodType(Enum):
    """
    Enumeration of valid methods for combining calibration pulses.
    """

    PCC2 = "PCC2"
    AVERAGE = "Average"
    ISOLATION_SUBTRACTION = "Isolation Subtraction"


class ChirpSourceType(Enum):
    """
    Enumeration of the available chirp schemes.
    """

    NOMINAL = "Nominal"
    EXTRACTED = "Extracted"


@dataclass(frozen=True, slots=True, kw_only=True)
class ComplexArray:
    """String containing an array of complex value pairs separated by spaces in the
    form of I Q I Q I Q ...

    The mandatory count attribute defines the number of complex elements
    in the array.
    """

    class Meta:
        name = "complexArray"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
    units: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class DcInputDataType(Enum):
    """
    Enumeration of Doppler centroid input data formats.
    """

    RAW = "Raw"
    RANGE_COMPRESSED = "Range Compressed"


class DcMethodType(Enum):
    """
    Enumeration of Doppler centroid calculation/estimation methods.
    """

    DATA_ANALYSIS = "Data Analysis"
    ORBIT_AND_ATTITUDE = "Orbit and Attitude"
    PRE_DEFINED = "Pre-defined"


@dataclass(frozen=True, slots=True, kw_only=True)
class Double:
    """
    64 bit double precision floating point number.
    """

    class Meta:
        name = "double"

    value: float = field(
        metadata={
            "required": True,
        }
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class DoubleArray:
    """String containing an array of double precision floating point values
    separated by spaces.

    The mandatory count attribute defines the number of elements in the
    array.
    """

    class Meta:
        name = "doubleArray"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
    units: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class DoubleCoefficientArray:
    """String containing an array of double precision floating point coefficient
    values separated by spaces.

    The mandatory count attribute defines the number of elements in the
    array.
    """

    class Meta:
        name = "doubleCoefficientArray"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
    units: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class Float:
    """
    32 bit single precision floating point number.
    """

    class Meta:
        name = "float"

    value: float = field(
        metadata={
            "required": True,
        }
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class FloatArray:
    """String containing an array of float values separated by spaces.

    The mandatory count attribute defines the number of elements in the
    array.
    """

    class Meta:
        name = "floatArray"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
    units: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class FloatCoefficientArray:
    """String containing an array of float coefficient values separated by spaces.

    The mandatory count attribute defines the number of elements in the
    array.
    """

    class Meta:
        name = "floatCoefficientArray"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
    units: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class FloatPatternArray:
    """String containing an array of up to 4500 float values separated by spaces.

    The mandatory count attribute defines the number of elements in the
    array.
    """

    class Meta:
        name = "floatPatternArray"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
    units: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class IntArray:
    """String containing an array of int values separated by spaces.

    The mandatory count attribute defines the number of elements in the
    array.
    """

    class Meta:
        name = "intArray"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
    units: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class MissionIdType(Enum):
    """
    Enumeration of valid Sentinel-1 mission identifiers.
    """

    S1_A = "S1A"
    S1_B = "S1B"
    ASA = "ASA"


class OutputPixelsType(Enum):
    """
    Enumeration of output pixel data types.
    """

    VALUE_32_BIT_FLOAT = "32 bit Float"
    VALUE_16_BIT_SIGNED_INTEGER = "16 bit Signed Integer"
    VALUE_16_BIT_UNSIGNED_INTEGER = "16 bit Unsigned Integer"
    VALUE_8_BIT_UNSIGNED_INTEGER = "8 bit Unsigned Integer"


class PgSourceType(Enum):
    """
    Enumeration of the available PG schemes.
    """

    EXTRACTED = "Extracted"
    MODEL = "Model"


class PolarisationType(Enum):
    """
    Enumeration of valid polarisations for the Sentinel-1 SAR instrument.
    """

    HH = "HH"
    HV = "HV"
    VH = "VH"
    VV = "VV"


class ProductType(Enum):
    """
    Enumeration of valid product types.
    """

    SLC = "SLC"
    GRD = "GRD"
    BRW = "BRW"
    OCN = "OCN"


class RrfSpectrumType(Enum):
    """
    Enumeration of valid RRF types.
    """

    UNEXTENDED = "Unextended"
    EXTENDED_FLAT = "Extended Flat"
    EXTENDED_TAPERED = "Extended Tapered"


class RxPolarisationType(Enum):
    """
    Enumeration of valid receive polarisations.
    """

    H = "H"
    V = "V"


class SensorModeType(Enum):
    """
    Enumeration of valid sensor mode abbreviations for the Sentinel-1 SAR
    instrument.
    """

    S1 = "S1"
    S2 = "S2"
    S3 = "S3"
    S4 = "S4"
    S5 = "S5"
    S6 = "S6"
    IW = "IW"
    EW = "EW"
    WV = "WV"
    EN = "EN"
    N1 = "N1"
    N2 = "N2"
    N3 = "N3"
    N4 = "N4"
    N5 = "N5"
    N6 = "N6"
    RF = "RF"
    IM = "IM"


class SignalType(Enum):
    """
    Enumeration of valid signal types for the Sentinel-1 SAR instrument.
    """

    ECHO = "Echo"
    NOISE = "Noise"
    TX_CAL = "TxCal"
    RX_CAL = "RxCal"
    EPDN_CAL = "EpdnCal"
    TX_HCAL_ISO = "TxHCalIso"
    TA_CAL = "TaCal"
    APDN_CAL = "ApdnCal"
    TA_RX_CAL = "TaRxCal"
    APDN_RX_CAL = "ApdnRxCal"
    TX_RX_OFF = "TxRxOff"
    SILENT = "Silent"


class SwathType(Enum):
    """Enumeration of all valid swath identifiers for the Sentinel-1 SAR
    instrument.

    The S1-S6 swaths apply to SM products, the IW and IW1-3 swaths apply
    to IW products (IW is used for detected IW products where the 3
    swaths are merged into one image), the EW and EW1-5 swaths apply to
    EW products (EW is used for detected EW products where the 5 swaths
    are merged into one image), and the WV1-2 swaths apply to WV
    products.  The EN, N1-N6 swaths apply to the Sentinel-1 notch modes
    used for instrument calibration.  The RF swath applies to the
    Sentinel-1 RFC mode which is not processed by the IPF.  The IS1-IS7
    swaths apply to ASAR IM and WV products.
    """

    S1 = "S1"
    S2 = "S2"
    S3 = "S3"
    S4 = "S4"
    S5 = "S5"
    S6 = "S6"
    IW = "IW"
    IW1 = "IW1"
    IW2 = "IW2"
    IW3 = "IW3"
    EW = "EW"
    EW1 = "EW1"
    EW2 = "EW2"
    EW3 = "EW3"
    EW4 = "EW4"
    EW5 = "EW5"
    WV = "WV"
    WV1 = "WV1"
    WV2 = "WV2"
    EN = "EN"
    N1 = "N1"
    N2 = "N2"
    N3 = "N3"
    N4 = "N4"
    N5 = "N5"
    N6 = "N6"
    RF = "RF"
    IS1 = "IS1"
    IS2 = "IS2"
    IS3 = "IS3"
    IS4 = "IS4"
    IS5 = "IS5"
    IS6 = "IS6"
    IS7 = "IS7"


class TopsFilterConventionType(Enum):
    """
    Enumeration of valid conventions for defining the TOPS ramping/de-ramping
    filter.
    """

    ALL_LINES = "All Lines"
    ONLY_ECHO_LINES = "Only Echo Lines"


@dataclass(frozen=True, slots=True, kw_only=True)
class Uint64Array:
    """String containing an array of 64 bit unsigned integer values separated by
    spaces.

    The mandatory count attribute defines the number of elements in the
    array.
    """

    class Meta:
        name = "uint64Array"

    value: str = field(
        default="",
        metadata={
            "required": True,
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
    units: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class UnitInteger:
    """
    Extension of the integer data type to include an optional "units" attribute.
    """

    class Meta:
        name = "unitInteger"

    value: int = field(
        metadata={
            "required": True,
        }
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class UnitNonNegativeInteger:
    """
    Extension of the nonNegativeInteger data type to include an optional "units"
    attribute.
    """

    class Meta:
        name = "unitNonNegativeInteger"

    value: int = field(
        metadata={
            "required": True,
        }
    )
    units: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class WeightingWindowType(Enum):
    """
    Enumeration of weighting windwow names.
    """

    KAISER = "Kaiser"
    HAMMING = "Hamming"
    NONE = "None"


@dataclass(frozen=True, slots=True, kw_only=True)
class AdsHeaderType:
    """Common header for all Annotation Data Sets.

    This record contains the three elements - polarisation, swath and imageNumber - used to identify Annotation Data Sets and link them to the appropriate Measurement Data Set.

    Parameters
    ----------
    mission_id
        Mission identifier for this data set.
    product_type
        Product type for this data set.
    polarisation
        Polarisation for this data set.
    mode
        Sensor mode for this data set. The sensorMode type are S1-S6, IW,
        EW, WV, and IM.
    swath
        Swath identifier for this data set. This element identifies the
        swath that applies to all data contained within this data set.  The
        swath identifier "EW" is used for products in which the 5 EW swaths
        have been merged.  Likewise, "IW" is used for products in which the
        3 IW swaths have been merged.
    start_time
        Zero Doppler start time of the output image [UTC].
    stop_time
        Zero Doppler stop time of the output image [UTC].
    absolute_orbit_number
        Absolute orbit number at data set start time.
    mission_data_take_id
        Mission data take identifier.
    image_number
        Image number. For WV products the image number is used to
        distinguish between vignettes.  For SM, IW and EW modes the image
        number is still used but refers instead to each swath and
        polarisation combination (known as the 'channel') of the data.
    """

    class Meta:
        name = "adsHeaderType"

    mission_id: MissionIdType = field(
        metadata={
            "name": "missionId",
            "type": "Element",
            "required": True,
        }
    )
    product_type: ProductType = field(
        metadata={
            "name": "productType",
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
    mode: SensorModeType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    swath: SwathType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    start_time: XmlDateTime = field(
        metadata={
            "name": "startTime",
            "type": "Element",
            "required": True,
        }
    )
    stop_time: XmlDateTime = field(
        metadata={
            "name": "stopTime",
            "type": "Element",
            "required": True,
        }
    )
    absolute_orbit_number: str = field(
        metadata={
            "name": "absoluteOrbitNumber",
            "type": "Element",
            "required": True,
            "pattern": r"[1-9][0-9]{0,5}",
        }
    )
    mission_data_take_id: str = field(
        metadata={
            "name": "missionDataTakeId",
            "type": "Element",
            "required": True,
            "pattern": r"[1-9][0-9]{0,5}",
        }
    )
    image_number: str = field(
        metadata={
            "name": "imageNumber",
            "type": "Element",
            "required": True,
            "pattern": r"00[1-9]|0[1-9][0-9]|[1-9][0-9][0-9]",
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class Complex:
    """
    64 bit complex number consisting of a 32 bit single precision floating point
    real part and a 32 bit single precision floating point imaginary part.

    Parameters
    ----------
    re
        32 bit single precision floating point real number.
    im
        32 bit single precision floating point imaginary number.
    """

    class Meta:
        name = "complex"

    re: Float = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    im: Float = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class Int64(UnitInteger):
    """
    64 bit signed integer.
    """

    class Meta:
        name = "int64"


@dataclass(frozen=True, slots=True, kw_only=True)
class Uint64(UnitNonNegativeInteger):
    """
    64 bit unsigned integer.
    """

    class Meta:
        name = "uint64"


@dataclass(frozen=True, slots=True, kw_only=True)
class Int32(Int64):
    """
    32 bit signed integer.
    """

    class Meta:
        name = "int32"


@dataclass(frozen=True, slots=True, kw_only=True)
class Uint32(Uint64):
    """
    32 bit unsigned integer.
    """

    class Meta:
        name = "uint32"


@dataclass(frozen=True, slots=True, kw_only=True)
class Int16(Int32):
    """
    16 bit signed integer.
    """

    class Meta:
        name = "int16"


@dataclass(frozen=True, slots=True, kw_only=True)
class Uint16(Uint32):
    """
    16 bit unsigned integer.
    """

    class Meta:
        name = "uint16"


@dataclass(frozen=True, slots=True, kw_only=True)
class Byte(Int16):
    """
    8 bit signed byte.
    """

    class Meta:
        name = "byte"


@dataclass(frozen=True, slots=True, kw_only=True)
class Ubyte(Uint16):
    """
    8 bit unsigned byte.
    """

    class Meta:
        name = "ubyte"
