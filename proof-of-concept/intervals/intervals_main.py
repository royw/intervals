#!/usr/bin/env python
# coding=utf-8
"""
This is the console entry point (from setup.py) for the Intervals application.

"""

# hack the system path so you can run this file directly in your dev environment and it also works fine packaged.
# note that importing hack_sys_path will modify the system path so should be the first import in your "main" module.
# noinspection PyUnresolvedReferences
import hack_sys_path

from intervals.intervals_app import IntervalsApp
from intervals.intervals_cli import IntervalsCLI

__docformat__ = 'restructuredtext en'
__all__ = ('main',)


def main():
    """
    This is the console entry point.
    """

    cli = IntervalsCLI()
    cli.execute(IntervalsApp())


if __name__ == '__main__':
    main()
