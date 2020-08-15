# coding=utf-8
"""
The command line interface for the Intervals application.

"""

from intervals.intervals_settings import IntervalsSettings
from fullmonty.simple_logger import error, info

__docformat__ = 'restructuredtext en'
__all__ = ("ArgumentError", "IntervalsCLI")


class ArgumentError(RuntimeError):
    """There is a problem with a command line argument"""
    pass


class IntervalsCLI(object):
    """
    Command Line Interface for the Intervals App
    """

    def execute(self, app):
        """
        Handle the command line arguments then execute the app.

        :param app: the application instance
        :type app: intervals.IntervalsApp
        """
        with IntervalsSettings() as settings:
            try:
                results = app.execute(settings)
                if results is not None:
                    self.report(results)
                exit(0)
            except ArgumentError as ex:
                error(str(ex))
                exit(1)

    def report(self, results):
        """

        :param results: (success[], error[], missing_filters_for_rule_ids[])
        :type results: tuple
        """
        # TODO: implement result report
        info("Results: {results}".format(results=repr(results)))
