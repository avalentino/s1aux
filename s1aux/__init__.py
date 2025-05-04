"""Reader for Sentinel-1 auxiliary (AUX) products."""

from ._core import (  # noqa: F401
    load,
    get_product_type,
    EProductType,
    S1AuxParseError,
)

__version__ = "0.9.1.dev0"
