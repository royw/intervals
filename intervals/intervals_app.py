# coding=utf-8
"""
The Intervals application.

"""
from fullmonty.graceful_interrupt_handler import GracefulInterruptHandler
from fullmonty.simple_logger import Logger, info, error, FileLogger, debug

__docformat__ = 'restructuredtext en'
__all__ = ("IntervalsApp",)


class IntervalsApp(object):
    """
    This is the application class.

    Usage::

        cli = IntervalsCLI()
        cli.execute(IntervalsApp())

    """

    def __init__(self):
        """
        The Intervals application.
        """
        # noinspection PyArgumentEqualDefault
        Logger.set_verbose(True)
        Logger.set_debug(False)

    # noinspection PyUnresolvedReferences
    def execute(self, settings):
        """
        Execute the tasks specified in the settings object.

        :param settings: the application settings
        :type settings: argparse.Namespace
        :return: None
        :raises: ArgumentError
        """
        Logger.set_verbosity(settings.verbosity)
        if settings.logfile is not None and settings.logfile:
            Logger.add_logger(FileLogger(settings.logfile))

        with GracefulInterruptHandler() as handler:
            # TODO: implement app here
            if handler.interrupted:
                pass

        return None
