"""
Starlette RFC 7807 - Problem Details for HTTP APIs

This package provides middleware and exception handlers for Starlette applications
to generate RFC 7807 compliant problem detail responses.
"""

from .exception import ProblemDetailException
from .middleware import ProblemDetailMiddleware

__version__ = "0.1.0"
__all__ = ["ProblemDetailException", "ProblemDetailMiddleware"]
