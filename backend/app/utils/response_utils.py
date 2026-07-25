"""Shared API response helpers.

Every endpoint returns the same envelope so clients can handle responses
consistently: ``success``, ``message``, and ``data``.
"""

from typing import Any


def success_response(message: str, data: Any = None) -> dict[str, Any]:
    return {
        "success": True,
        "message": message,
        "data": data,
    }


def error_response(message: str, data: Any = None) -> dict[str, Any]:
    return {
        "success": False,
        "message": message,
        "data": data,
    }
