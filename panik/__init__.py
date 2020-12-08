"""Panik.

This will replace every python problem by a pytonpanik.

Example:
    >>> import panik
    >>> sometim i paniks
"""
import os
import sys

__all__ = []


with open(os.path.join(os.path.dirname(__file__), "panikman.txt")) as f:
    panik_img = "".join(f.readlines())

sys.excepthook = lambda *_: print(panik_img, file=sys.stderr)
