"""Tools and utilities for the management of Sentinel-1 auxiliary products."""

from ._core import (  # noqa: F401
    load,
    get_product_type,
    EProductType,
    S1AuxParseError,
)

__version__ = "0.2.dev0"
