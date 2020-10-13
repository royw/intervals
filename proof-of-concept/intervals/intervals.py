import collections
from typing import List

"""
# Background info for scale intervals

## Major Scale

A major scale is a diatonic scale. The sequence of intervals between the notes of a major scale is:

    whole, whole, half, whole, whole, whole, half

A major scale may be seen as two identical tetrachords separated by a whole tone.
Each tetrachord consists of two whole tones followed by a semitone (i.e. whole, whole, half).

The major scale is maximally even.

## Natural Minor Scale

The intervals between the notes of a natural minor scale follow the sequence below:
    whole, half, whole, whole, half, whole, whole
The natural minor scale is maximally even.

## Harmonic Minor Scale

The harmonic minor scale (or Aeolian ♯7 scale) has the same notes as the natural minor scale except that the
seventh degree is raised by one semitone, creating an augmented second between the sixth and seventh degrees.

Thus, a harmonic minor scale is represented by the following notation:

    1, 2, ♭3, 4, 5, ♭6, 7, 8

Thus, a harmonic minor scale can be built by lowering the 3rd and 6th degrees of the parallel major scale by
one semitone.

Because of this construction, the 7th degree of the harmonic minor scale functions as a leading tone to the
tonic because it is a semitone lower than the tonic, rather than a whole tone lower than the tonic as it is
in natural minor scales. The intervals between the notes of a harmonic minor scale follow the sequence below:

    whole, half, whole, whole, half, augmented second, half

## Melodic minor scale

The distinctive sound of the harmonic minor scale comes from the augmented second between its sixth and seventh 
scale degrees. While some composers have used this interval to advantage in melodic composition, others felt it 
to be an awkward leap, particularly in vocal music, and preferred a whole step between these scale degrees for 
smooth melody writing. To eliminate the augmented second, these composers either raised the sixth degree by a 
semitone or lowered the seventh by a semitone.

The melodic minor scale is formed by using both of these solutions. In particular, the raised sixth appears in 
the ascending form of the scale, while the lowered seventh appears in the descending form of the scale. 
Traditionally, these two forms are referred to as:

the ascending melodic minor scale (also known as the heptatonia seconda, jazz minor scale, 
or Ionian ♭3): This form of the scale is also the 5th mode of the acoustic scale.
the descending melodic minor scale: This form is identical to the natural minor scale .
The ascending and descending forms of the A melodic minor scale are shown below:

The ascending melodic minor scale can be notated as    
    1, 2, ♭3, 4, 5, 6, 7, 8
while the descending melodic minor scale is
    1, 2, ♭3, 4, 5, ♭6, ♭7, 8
Using these notations, the two melodic minor scales can be built by altering the parallel major scale.
"""


class Intervals(object):
    """
    Strings are 1 offset
    High string is 1, low string is N_STRINGS
    Frets are 0 offset so 0 = open string, 1 = first fret, ...

    """
    MAJOR_INTERVALS = [0, 2, 4, 5, 7, 9, 11]
    MINOR_INTERVALS = [0, 2, 3, 5, 7, 8, 10]
    SHARP = '♯'
    FLAT = '♭'
    NOTES_SEMITONES: collections.OrderedDict = {
        'A': 0,
        'A♯/B♭': 1,
        'B': 2,
        'C': 3,
        'C♯/D♭': 4,
        'D': 5,
        'D♯/E♭': 6,
        'E': 7,
        'F': 8,
        'F♯/G♭': 9,
        'G': 10,
        'G♯/A♭': 11
    }
    SEMITONES_NOTES: collections.OrderedDict = collections.defaultdict(set)
    for k, v in NOTES_SEMITONES.items():
        SEMITONES_NOTES[v].add(k)

    def __init__(self, key: str, tuning: List[str], frets:int):
        """
        :param key: The root note for the intervals
        :param tuning: list of note names for the open strings
        :param frets: the number of frets to display
        """
        self.minor_key = 'm' in key
        self.major_key = 'm' not in key
        self.key = key[0]
        self.tuning = tuning
        self.frets = frets
        self.n_strings = len(tuning)

        # find the list of integers for the notes of the tuning.  Ex:  'EADGBE' => [5, 1, 4, 7, 2, 5]
        self.string_intervals = list(reversed([int(x) for x in self._translate(tuning, "ABCDEFG", "1234567")]))
        self.strings = []
        # string_notes = [A, 0, B, C, 0, D, 0, E, F, 0, G, 0, A, ...]
        # string_notes = [1, 0, 2, 3, 0, 4, 0, 5, 6, 0, 7, 0, 1, ...]
        for string_root_note in self.tuning:
            self.strings.append(self.string_semitones(string_root_note))

    @property
    def key_name(self):
        if self.major_key:
            return f"{self.key} Major"
        if self.minor_key:
            return f"{self.key} Minor"
        return self.key

    def note_from_semitone(self, semitone):
        note = ''
        for note_ in self.SEMITONES_NOTES[semitone % 12]:
            note = note_
            if self.SHARP in note:
                return note
            if self.FLAT not in note:
                return note
        return note

    def string_semitones(self, string_tuning_note: str) -> List[int]:
        root_semitone = self.NOTES_SEMITONES[string_tuning_note]
        return list(range(root_semitone, root_semitone + self.frets))

    def interval_from_semitone(self, semitone: int) -> str:
        key_semitone = self.NOTES_SEMITONES[self.key]
        scale = self._semitone_scale()
        semitone -= key_semitone
        semitone %= 12
        if semitone in scale:
            return str(scale.index(semitone) + 1)
        return '.'

    def semitone(self, semitone: int) -> int:
        # this is here to facilitate function abstraction
        return semitone

    def _semitone_scale(self):
        if self.major_key:
            return self.MAJOR_INTERVALS
        if self.minor_key:
            return self.MINOR_INTERVALS

    def _translate(self, srcString: str, charsToReplace: str, replacementChars: str, deleteChars: str = None) -> str:
        """
        Translate and optionally delete characters.  The charsToReplace string and replacementChars string must
        be the same length.  Also each character in the charsToReplace string will be replaced with the character
        in the replacementChars string that has the same index.  I.e., if charsToReplace is "abc", and replacementChars
        is "efg", then every occurrence of 'a' in the source string will be replaced with an 'e', same for 'b' => 'f',
        and 'c' -> 'g'

        :param srcString:          The string to translate
        :param charsToReplace:     A string containing characters to replace in the source string
        :param replacementChars:   A string containing the replacement characters
        :param deleteChars:        A string containing the characters to delete from the source string
        :return:                   The translated string
        """
        if deleteChars is None:
            return srcString.translate(str.maketrans(charsToReplace, replacementChars, ""))
        return srcString.translate(str.maketrans(charsToReplace, replacementChars, deleteChars))
