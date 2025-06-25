"""
Starlette RFC 7807 - Problem Details for HTTP APIs

This package provides middleware and exception handlers for Starlette applications
to generate RFC 7807 compliant problem detail responses.
"""

from .exception import Problem
from .middleware import ProblemMiddleware, http_exception_handler

try:
    from importlib.metadata import version

    __version__ = version("starlette-rfc7807")
except ImportError:
    __version__ = "unknown"

__all__ = ["Problem", "http_exception_handler", "ProblemMiddleware"]
