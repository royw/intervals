var tunings = {
    "6 - Standard": ["E2", "A2", "D3", "G3", "B3", "E4"],
    "6 - Drop-D": ["D2", "A2", "D3", "G3", "B3", "E4"],
    "6 - Nashville": ["E3", "A3", "D4", "G4", "B3", "E4"],
    "6 - Open A (A,C♯,E)": ["E2", "A2", "C♯3", "E3", "A3", "E4"],
    "6 - Open A (A,C♯,E) Slide": ["E2", "A2", "E3", "A3", "C♯4", "E4"],
    "6 - Open A (A,C♯,E) Alternative": ["E2", "A2", "E3", "A3", "E4", "C♯4"],
    "6 - Open A	(A,C♯,E) Repetitive":	["A2", "C♯3", "E3", "A3", "C♯4", "E4"],
    "6 - Open A (A,C♯,E) Overtones": ["A", "A", "E", "A", "C♯", "E"],
    "6 - Open B	(B,D♯,F♯) Repetitive":	["B", "D♯", "F♯", "B", "D♯", "F♯"],
    "6 - Open B	(B,D♯,F♯) Overtones": ["B", "B", "F♯", "B", "D♯", "F♯"],
    "6 - Open B	(B,D♯,F♯)": ["B", "F♯", "B", "F♯", "B", "D♯"],
    "6 - Open C	(C,E,G)": ["C", "G", "C", "G", "C", "E"],
    "6 - Open C	(C,E,G) Repetitive": ["C", "E", "G", "C", "E", "G"],
    "6 - Open C	(C,E,G) Overtones": ["C", "C", "G", "C", "E", "G"],
    "6 - Open D	(D,F♯,A)": ["D", "A", "D", "F♯", "A", "D"],
    "6 - Open D	(D,F♯,A) Repetitive": ["D", "F♯", "A", "D", "F♯", "A"],
    "6 - Open D	(D,F♯,A) Overtones": ["D", "D", "A", "D", "F♯", "A"],
    "6 - Open E	(E,G♯,B)": ["E", "B", "E", "G♯", "B", "E"],
    "6 - Open E	(E,G♯,B) Repetitive": ["E", "G♯", "B", "E", "G♯", "B"],
    "6 - Open E	(E,G♯,B) Overtones": ["E", "E", "B", "E", "G♯", "B"],
    "6 - Open F	(F,A,C)": ["C", "F", "C", "F", "A", "F"],
    "6 - Open F	(F,A,C) Repetitive": ["F", "A", "C", "F", "A", "C"],
    "6 - Open F	(F,A,C) Overtones": ["F", "F", "C", "F", "A", "C"],
    "6 - Open G	(G,B,D)": ["D", "G", "D", "G", "B", "D"],
    "6 - Open G	(G,B,D) Repetitive": ["G", "B", "D", "G", "B", "D"],
    "6 - Open G	(G,B,D) Overtones": ["G", "G", "D", "G", "B", "D"],
    "4 - Reentrant ukulele": ["G4", "C4", "E4", "A4"],
    "4 - Canadian Ukulele": ["A4", "D4", "F♯4", "B4"],
    "4 - Linear  Ukulele alt": ["G3", "C4", "E4", "A4"],
    "4 - Slack-key Ukulele": ["G3", "C4", "E4", "G4"],
    "4 - Slack-key Ukulele alt": ["G4", "C4", "E4", "G4"],
    "4 - Tenor Ukulele alt 1": ["G3", "C4", "E4", "A4"],
    "4 - Tenor Ukulele alt 2": ["D4", "G3", "B3", "E4"],
    "4 - Tenor Ukulele alt 3": ["D3", "G3", "B3", "E4"],
    "4 - Baritone Ukulele": ["D3", "G3", "B3", "E4"],
    "4 - Baritone Ukulele alt": ["C3", "G3", "B3", "E4"],
    "4 - Bass Standard": ["B0", "E1", "A1", "D2"],
    "4 - Bass Standard alt": ["E0", "A0", "D1", "G1"],
    "4 - Bass Drop D": ["D0", "A0", "D1", "G1"],
    "4 - Bass Drop C": ["C0", "G1", "C2", "F2"],
    "4 - Bass Drop B": ["B0", "F#1", "B1", "E2"],
    "6 - Bass Standard": ["B0", "E1", "A1", "D2", "G2", "C3"],
    "5 - Standard": ["E2", "A2", "D3", "G3", "B3"],
    "5 - Bass Standard": ["B0", "E1", "A1", "D2", "G2"],
    "5 - Bass Tenor": ["E1", "A1", "D2", "G2", "C3"],
    "3 - Standard": ["G3", "D4", "G4"],
    "3 - Standard alt:": ["E3", "B3", "E4"],
    "3 - Open B:": ["F3#", "B3", "D4#"],
    "3 - Guitar tuning:": ["G3", "B3", "E4"],
    "3 - Open G:": ["G3", "B3", "D4"],
    "3 - Fifths:": ["E3", "B3", "F4#"]
};

let tunings_data = [];
for (let k in tunings) {
    let value = k;
    value += " - ";
    value += tunings[k];
    tunings_data.push(value);
};

function onlyUnique(value, index, self) {
  return self.indexOf(value) === index;
}

let string_data = [];
for (let k in tunings) {
    let strings = [];
    let value = k.split(" - ")[0];
    string_data.push(value);
}
string_data = string_data.filter(onlyUnique);
string_data.sort();
