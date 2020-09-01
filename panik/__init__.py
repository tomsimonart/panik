"""Panik.

This will replace every python problem by a pytonpanik.

Example:
    >>> import panik
    >>> sometim i paniks
"""
import sys

__all__ = []


def panik(*_):
    """De panik."""
    print("panik", file=sys.stderr)


sys.excepthook = panik
