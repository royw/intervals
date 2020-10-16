var modes = {
    "Ionian mode or major scale": {
        "intervals": ["1", "2", "3", "4", "5", "6", "7"],
        "steps": ["W", "W", "H", "W", "W", "W", "H"]
    },
    "Dorian mode": {
        "intervals": ["1", "2", "♭3", "4", "5", "6", "♭7"],
        "steps": ["W", "H", "W", "W", "W", "H", "W"]
    },
    "Phrygian mode": {
        "intervals": ["1", "♭2", "♭3", "4", "5", "♭6", "♭7", "1"],
        "steps": ["H", "W", "W", "W", "H", "W", "W"]
    },
    "Lydian mode": {
        "intervals": ["1", "2", "3", "♯4", "5", "6", "7"],
        "steps": ["W", "W", "W", "H", "W", "W", "H"]
    },
    "Mixolydian mode or Adonai malakh mode": {
        "intervals": ["1", "2", "3", "4", "5", "6", "♭7"],
        "steps": ["W", "W", "H", "W", "W", "H", "W"]
    },
    "Aeolian mode or natural minor scale": {
        "intervals": ["1", "2", "♭3", "4", "5", "♭6", "♭7"],
        "steps": ["W", "H", "W", "W", "H", "W", "W"]
    },
    "Locrian mode": {
        "intervals": ["1", "♭2", "♭3", "4", "♭5", "♭6", "♭7"],
        "steps": ["H", "W", "W", "H", "W", "W", "W"]
    },

    "Acoustic scale": {
        "intervals": ["1", "2", "3", "♯4", "5", "6", "♭7"],
        "steps": ["W", "W", "W", "H", "W", "H", "W"]
    },
    "Algerian scale": {
        "intervals": ["1", "2", "♭3", "♯4", "5", "♭6", "7"],
        "steps": ["W", "H", "3H", "H", "H", "3H", "H", "W", "H", "W"]
    },
    "Altered scale or Super Locrian scale": {
        "intervals": ["1", "♭2", "♭3", "♭4", "♭5", "♭6", "♭7"],
        "steps": ["H", "W", "H", "W", "W", "W", "W"]
    },
    "Augmented scale": {
        "intervals": ["1", "♭3", "3", "5", "♯5", "7"],
        "steps": ["3H", "H", "3H", "H", "3H", "H"]
    },
    "Bebop dominant scale": {
        "intervals": ["1", "2", "3", "4", "5", "6", "♭7", "7"],
        "steps": ["W", "W", "H", "W", "W", "H", "H", "H"]
    },
    "Blues scale": {
        "intervals": ["1", "♭3", "4", "♭5", "5", "♭7"],
        "steps": ["3H", "W", "H", "H", "3H", "W"]
    },
    "Chromatic scale": {
        "intervals": ["1", "♯1", "2", "♯2", "3", "4", "♯4", "5", "♯5", "6", "♯6", "7"],
        "steps": ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H"]
    },
    "Double harmonic scale": {
        "intervals": ["1", "♭2", "3", "4", "5", "♭6", "7"],
        "steps": ["H", "3H", "H", "W", "H", "3H", "H"]
    },
    "Enigmatic scale": {
        "intervals": ["1", "♭2", "3", "♯4", "♯5", "♯6", "7"],
        "steps": ["H", "3H", "W", "W", "W", "H", "H"]
    },
    "Flamenco mode": {
        "intervals": ["1", "♭2", "3", "4", "5", "♭6", "7"],
        "steps": ["H", "3H", "H", "W", "H", "3H", "H"]
    },
    "\"Gypsy\" scale": {
        "intervals": ["1", "2", "♭3", "♯4", "5", "♭6", "♭7"],
        "steps": ["W", "H", "3H", "H", "H", "W", "W"]
    },
    "Half diminished scale": {
        "intervals": ["1", "2", "♭3", "4", "♭5", "♭6", "♭7"],
        "steps": ["W", "H", "W", "H", "W", "W", "W"]
    },
    "Harmonic major scale": {
        "intervals": ["1", "2", "3", "4", "5", "♭6", "7"],
        "steps": ["W", "W", "H", "W", "H", "3H", "H"]
    },
    "Harmonic minor scale": {
        "intervals": ["1", "2", "♭3", "4", "5", "♭6", "(♮)7"],
        "steps": ["W", "H", "W", "W", "H", "3H", "H"]
    },
    "Hirajoshi scale": {
        "intervals": ["1", "3", "♯4", "5", "7"],
        "steps": ["2W", "W", "H", "2W", "H"]
    },
    "Hungarian \"Gypsy\" scale/Hungarian minor scale": {
        "intervals": ["1", "2", "♭3", "♯4", "5", "♭6", "7"],
        "steps": ["W", "H", "3H", "H", "H", "3H", "H"]
    },
    "Hungarian major scale": {
        "intervals": ["1", "♯2", "3", "♯4", "5", "6", "♭7"],
        "steps": ["3H", "H", "W", "H", "W", "H", "W"]
    },
    "In scale": {
        "intervals": ["1", "♭2", "4", "5", "♭6"],
        "steps": ["H", "2W", "W", "H", "2W"]
    },
    "Insen scale": {
        "intervals": ["1", "♭2", "4", "5", "♭7"],
        "steps": ["H", "2W", "W", "2W", "W"]
    },
    "Istrian scale": {
        "intervals": ["1", "♭2", "♭3", "♭4", "♭5", "5"],
        "steps": ["H", "W", "H", "W", ""]
    },
    "Iwato scale": {
        "intervals": ["1", "♭2", "4", "♭5", "♭7"],
        "steps": ["H", "2W", "H", "2W", "W"]
    },
    "Lydian augmented scale": {
        "intervals": ["1", "2", "3", "♯4", "♯5", "6", "7"],
        "steps": ["W", "W", "W", "W", "H", "W", "H"]
    },
    "Major bebop scale": {
        "intervals": ["1", "2", "3", "4", "5", "(♯5/♭6)", "6", "7"],
        "steps": ["W", "W", "H", "W", "(H", "H)", "W", "H"]
    },
    "Major Locrian scale": {
        "intervals": ["1", "2", "3", "4", "♭5", "♭6", "♭7"],
        "steps": ["W", "W", "H", "H", "W", "W", "W"]
    },
    "Major pentatonic scale": {
        "intervals": ["1", "2", "3", "5", "6"],
        "steps": ["W", "W", "3H", "W", "3H"]
    },
    "Melodic minor scale (ascending)": {
        "intervals": ["1", "2", "♭3", "4", "5", "6", "7"],
        "steps": ["W", "H", "W", "W", "W", "W", "H"]
    },
    "Minor pentatonic scale": {
        "intervals": ["1", "♭3", "4", "5", "♭7"],
        "steps": ["3H", "W", "W", "3H", "W"]
    },
    "Neapolitan major scale": {
        "intervals": ["1", "♭2", "♭3", "4", "5", "6", "7"],
        "steps": ["H", "W", "W", "W", "W", "W", "H"]
    },
    "Neapolitan minor scale": {
        "intervals": ["1", "♭2", "♭3", "4", "5", "♭6", "7"],
        "steps": ["H", "W", "W", "W", "H", "3H", "H"]
    }
};

var modes_data = [];
for (var k in modes) {
    var value = k;
    value += " - "
    value += modes[k]["intervals"]
    value += " - "
    value += modes[k]["steps"]
    modes_data.push(value);
};