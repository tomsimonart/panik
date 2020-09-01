"""Panik.

This will replace every python problem by a pytonpanik.

Example:
    >>> import panik
    >>> sometim i paniks
"""
import sys

__all__ = []


sys.excepthook = lambda *_: print("panik", file=sys.stderr)
