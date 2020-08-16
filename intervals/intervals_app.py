# coding=utf-8
"""
The Intervals application.

"""
from sys import stdout

from fullmonty.graceful_interrupt_handler import GracefulInterruptHandler
from fullmonty.simple_logger import Logger, info, error, FileLogger, debug
from intervals.intervals import Intervals

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
            intervals = Intervals(key=settings.key, tuning=settings.tuning, frets=settings.frets)
            if settings.output == "stdout":
                self.streamNotes(intervals, stream=stdout)
                self.streamSemitones(intervals, stream=stdout)
                self.streamInterval(intervals, stream=stdout)
            if handler.interrupted:
                pass

        return None

    def _streamOpenNotes(self, intervals, stream, func=None):
        stream.write(f"key: {intervals.key_name}\n")
        fret = 0
        line = f"   || "
        for string_semitones in intervals.strings:
            note = intervals.note_from_semitone(string_semitones[fret])
            line += f"{note:^5s} | "
        stream.write(line)
        stream.write('\n')
        if func:
            line = f"{fret:2d} || "
            for string_semitones in intervals.strings:
                note = str(func(string_semitones[fret]))
                line += f"{note:^5s} | "
            stream.write(line)
            stream.write('\n')
        stream.write('=' * (len(line) - 1))
        stream.write('\n')

    def _streamFret(self, intervals, stream, fret, func):
        line = f"{fret:2d} || "
        for string_semitones in intervals.strings:
            note = str(func(string_semitones[fret]))
            line += f"{note:^5s}" + " | "
        stream.write(line)
        stream.write('\n')

    def streamNotes(self, intervals, stream):
        for fret in range(intervals.frets):
            if fret == 0:
                self._streamOpenNotes(intervals, stream)
            else:
                self._streamFret(intervals, stream, fret, intervals.note_from_semitone)
        stream.write('\n\n')

    def streamSemitones(self, intervals, stream):
        for fret in range(intervals.frets):
            if fret == 0:
                self._streamOpenNotes(intervals, stream, intervals.semitone)
            else:
                self._streamFret(intervals, stream, fret, intervals.semitone)
        stream.write('\n\n')

    def streamInterval(self, intervals, stream):
        for fret in range(intervals.frets):
            if fret == 0:
                self._streamOpenNotes(intervals, stream, intervals.interval_from_semitone)
            else:
                self._streamFret(intervals, stream, fret, intervals.interval_from_semitone)
        stream.write('\n\n')
