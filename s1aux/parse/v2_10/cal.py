from decimal import Decimal
from dataclasses import field, dataclass

from .s1_object_types import (
    Double,
    SwathType,
    ComplexArray,
    PolarisationType,
    FloatPatternArray,
)


@dataclass(frozen=True, slots=True, kw_only=True)
class AzimuthAntennaElementPatternType:
    """
    Azimuth antenna element pattern parameters record definition.

    Parameters
    ----------
    azimuth_angle_increment
        Azimuth angle increment [degrees]. This parameter defines the step
        size between the values in the two way azimuth antenna element
        pattern.
    values
        Two way azimuth antenna element pattern values [dB]. The centre
        value of the vector corresponds to 0 degrees (the vector must
        contain an odd number of values), and the values before and after
        the centre value correspond to steps of azimuthAngleIncrement
        degrees from the centre value.  The pattern contains attribute
        "count" floating point values separated by spaces.  The first value
        in the antenna pattern vector corresponds to –((count  - 1)/2) *
        azimuthAngleIncrement degrees, and the last value corresponds to
        +((count  - 1)/2) * azimuthAngleIncrement degrees.
    """

    class Meta:
        name = "azimuthAntennaElementPatternType"

    azimuth_angle_increment: Double = field(
        metadata={
            "name": "azimuthAngleIncrement",
            "type": "Element",
            "required": True,
        }
    )
    values: FloatPatternArray = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class AzimuthAntennaPatternType:
    """
    Azimuth antenna pattern parameters record definition.

    Parameters
    ----------
    azimuth_angle_increment
        Azimuth angle increment [degrees]. This parameter defines the step
        size between the values in the two way azimuth antenna pattern.
    values
        Two way azimuth antenna pattern values [dB]. The centre value of the
        vector corresponds to 0 degrees (the vector must contain an odd
        number of values), and the values before and after the centre value
        correspond to steps of azimuthAngleIncrement degrees from the centre
        value.  The pattern contains attribute "count" floating point values
        separated by spaces.  The first value in the antenna pattern vector
        corresponds to –((count  - 1)/2) * azimuthAngleIncrement degrees,
        and the last value corresponds to +((count  - 1)/2) *
        azimuthAngleIncrement degrees.
    """

    class Meta:
        name = "azimuthAntennaPatternType"

    azimuth_angle_increment: Double = field(
        metadata={
            "name": "azimuthAngleIncrement",
            "type": "Element",
            "required": True,
        }
    )
    values: FloatPatternArray = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class ElevationAntennaPatternType:
    """
    Elevation antenna pattern parameters record definition.

    Parameters
    ----------
    beam_nominal_near_range
        Elevation angle of the nominal near range extent of the beam
        [degrees].
    beam_nominal_far_range
        Elevation angle of the nominal far range extent of the beam
        [degrees].
    elevation_angle_increment
        Elevation angle increment [degrees]. This parameter defines the step
        size between the pattern values in the two way elevation antenna
        pattern.
    values
        Two-way complex antenna elevation pattern values. The centre value
        in the vector corresponds to the referenceAntennaAngle in the Roll
        Steering parameters described in the Instrument auxiliary file (the
        vector must contain an odd number of complex values), and the values
        before and after the centre value correspond to steps of
        elevationAngleIncrement from the centre value. The pattern contains
        attribute “count” complex floating point values separated by spaces
        in the order I Q I Q I Q...  The first value in the antenna pattern
        vector corresponds to –((count  - 1)/2) * elevationAngleIncrement
        degrees, and the last value corresponds to +((count  - 1)/2) *
        elevationAngleIncrement degrees. The complex values in this vector
        are applied to the complex image data as: ComplexDataCorrected(x,y)
        = ComplexData(x,y) / sqrt(ComplexEAP(x,y))
    """

    class Meta:
        name = "elevationAntennaPatternType"

    beam_nominal_near_range: Double = field(
        metadata={
            "name": "beamNominalNearRange",
            "type": "Element",
            "required": True,
        }
    )
    beam_nominal_far_range: Double = field(
        metadata={
            "name": "beamNominalFarRange",
            "type": "Element",
            "required": True,
        }
    )
    elevation_angle_increment: Double = field(
        metadata={
            "name": "elevationAngleIncrement",
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
class CalibrationParamsType:
    """
    Calibration parameters record definition.

    Parameters
    ----------
    swath
        Canonical name of the swath to which this set of calibration
        parameters applies. The swath and polarisation are used to index the
        applicable calibrationParams record.
    polarisation
        Polarisation to which this set of calibration parameters applies.
        The polarisation andUsed along with the swathNumber are used to
        index the applicable calibrationParams record.
    elevation_antenna_pattern
        Two way elevation antenna pattern parameters. The EAPs are used to
        correct the corresponding radiometric variation of the data in the
        range direction. The EAPs are also used for the estimation and
        removal of the thermal noise level.
    azimuth_antenna_pattern
        Two way azimuth antenna pattern (AAP) parameters.
    azimuth_antenna_element_pattern
        Two way azimuth antenna element pattern values. The AAEP maps
        azimuth steering angles to gain power and is used during de-
        scalloping of TOPSAR data. The AAEP is specific to IW and EW modes
        and is ignored for all others.
    absolute_calibration_constant
        Absolute calibration constant value to apply during processing.
        Although the structure of the file allows for a unique value per
        swath and polarisation the value of this field must be the same for
        all swaths and polarisations within the mode. The calibration
        constant C0 (described in the Sentinel-1 SAR Instrument Calibration
        and Characterisation Plan) should be merged into this field to
        acheive an overall gain value.
    noise_calibration_factor
        Noise calibration factor used in the estimation of the thermal
        noise.
    """

    class Meta:
        name = "calibrationParamsType"

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
    elevation_antenna_pattern: ElevationAntennaPatternType = field(
        metadata={
            "name": "elevationAntennaPattern",
            "type": "Element",
            "required": True,
        }
    )
    azimuth_antenna_pattern: AzimuthAntennaPatternType = field(
        metadata={
            "name": "azimuthAntennaPattern",
            "type": "Element",
            "required": True,
        }
    )
    azimuth_antenna_element_pattern: AzimuthAntennaElementPatternType = field(
        metadata={
            "name": "azimuthAntennaElementPattern",
            "type": "Element",
            "required": True,
        }
    )
    absolute_calibration_constant: Double = field(
        metadata={
            "name": "absoluteCalibrationConstant",
            "type": "Element",
            "required": True,
        }
    )
    noise_calibration_factor: Double = field(
        metadata={
            "name": "noiseCalibrationFactor",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class CalibrationParamsListType:
    """
    List of calibration parameter records.

    Parameters
    ----------
    calibration_params
        Calibration parameter record. There may be up to one record per
        swath (23 nominal swaths) per polarisation (4 polarisation
        combinations for SM, IW, EW, EN and AN, 2 for WV) for a maximum
        total of 88 records.
    count
        Number of calibration parameter records in the list.
    """

    class Meta:
        name = "calibrationParamsListType"

    calibration_params: tuple[CalibrationParamsType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "calibrationParams",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 92,
        },
    )
    count: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class AuxiliaryCalibrationType:
    """
    Calibration auxiliary file definition (AUX_CAL)

    Parameters
    ----------
    calibration_params_list
        List of calibration parameter records.
    schema_version
    """

    class Meta:
        name = "auxiliaryCalibrationType"

    calibration_params_list: CalibrationParamsListType = field(
        metadata={
            "name": "calibrationParamsList",
            "type": "Element",
            "required": True,
        }
    )
    schema_version: Decimal = field(
        init=False,
        default=Decimal("2.10"),
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class AuxiliaryCalibration(AuxiliaryCalibrationType):
    """
    Calibration auxiliary file definition (AUX_CAL)
    """

    class Meta:
        name = "auxiliaryCalibration"
