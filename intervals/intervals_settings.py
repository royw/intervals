# coding=utf-8
"""
IntervalsSettings adds application specific information to the generic ApplicationSettings class.
"""
from fullmonty.application_settings import ApplicationSettings

__docformat__ = 'restructuredtext en'
__all__ = ("IntervalsSettings",)


class IntervalsSettings(ApplicationSettings):
    """
    Usage::

        with IntervalsSettings() as settings:
        try:
            app.execute(self, settings)
            exit(0)
        except ArgumentError as ex:
            error(str(ex))
            exit(1)
    """

    DEFAULT_FRETS = 24          # one octave
    DEFAULT_KEY = "C"           # C major key
    DEFAULT_TUNING = "EADGBE"   # standard tuning

    DEFAULT_OUTPUT = "stdout"   # output to the stdout device

    HELP = {
        'Intervals': "Visualize the intervals on the fretboard",

        'info_group': '',
        'version': "Show Intervals's version.",
        'longhelp': 'Long help about Intervals.',

        'output_group': 'Options that control generated output.',
        'verbosity': 'Set verbosity level: 0=none, 1=errors, 2=info+errors, 3+=debug+info+errors (default=2).',
        'logfile': 'File to log all messages (debug, info, warning, error, fatal) to.',
        'output': 'The output device.  Current supported values: "stdout".  (default={0})'.format(DEFAULT_OUTPUT),

        'parameters_group': 'Interval Parameters',
        'tuning': 'The guitar tuning from low frequency to high.  Number of values is the number of strings. '
                  '(default={0})'.format(DEFAULT_TUNING),
        'key': 'The key to locate the intervals for.  (default={0})'.format(DEFAULT_KEY),
        'frets': 'The number of frets on the guitar.  (default={0})'.format(DEFAULT_FRETS),
    }

    def __init__(self):
        super(IntervalsSettings, self).__init__('Intervals', 'intervals', ['Intervals'], self.HELP)

    def _cli_options(self, parser, defaults):
        """
        Adds application specific arguments to the parser.

        :param parser: the argument parser with --conf_file already added.
        :type parser: argparse.ArgumentParser
        """
        info_group = parser.add_argument_group(title='Informational Commands', description=self._help['info_group'])
        info_group.add_argument('--version', dest='version', action='store_true', help=self._help['version'])
        info_group.add_argument('--longhelp', dest='longhelp', action='store_true', help=self._help['longhelp'])

        output_group = parser.add_argument_group(title='Output Options', description=self._help['output_group'])
        output_group.add_argument('--verbosity', dest='verbosity', default=2, type=int, metavar='INT',
                                  help=self._help['verbosity'])
        output_group.add_argument('--logfile', type=str, metavar='FILE', help=self._help['logfile'])
        output_group.add_argument('--output', dest='output', default='stdout', metavar='DEVICE',
                                  help=self._help['output'])

        parameter_group = parser.add_argument_group(title='Interval Parameters',
                                                    description=self._help['parameters_group'])
        parameter_group.add_argument('-k', '--key', dest='key', default=self.DEFAULT_KEY, type=str, metavar='CHAR',
                                     help=self._help['key'])
        parameter_group.add_argument('-t', '--tuning', dest='tuning', default=self.DEFAULT_TUNING, type=str,
                                     metavar='STRING', help=self._help['tuning'])
        parameter_group.add_argument('-f', '--frets', dest='frets', default=self.DEFAULT_FRETS, type=str, metavar='INT',
                                     help=self._help['frets'])

    def _cli_validate(self, settings, remaining_argv):
        """
        Verify we have required options for commands.

        :param settings: the settings object returned by ArgumentParser.parse_args()
        :type settings: argparse.Namespace
        :return: the error message if any
        :rtype: str or None
        """
        return None
