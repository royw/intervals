var tunings = {
    "Standard": ["E2", "A2", "D3", "G3", "B3", "E4"],
    "Drop-D": ["D2", "A2", "D3", "G3", "B3", "E4"],
    "Nashville": ["E3", "A3", "D4", "G4", "B3", "E4"],
    "Open A (A,C♯,E)": ["E2", "A2", "C♯3", "E3", "A3", "E4"],
    "Open A (A,C♯,E) Slide": ["E2", "A2", "E3", "A3", "C♯4", "E4"],
    "Open A (A,C♯,E) Alternative": ["E2", "A2", "E3", "A3", "E4", "C♯4"],
    "Open A	(A,C♯,E) Repetive":	["A2", "C♯3", "E3", "A3", "C♯4", "E4"],
    "Open A (A,C♯,E) Overtones": ["A", "A", "E", "A", "C♯", "E"],
    "Open B	(B,D♯,F♯) Repetive":	["B", "D♯", "F♯", "B", "D♯", "F♯"],
    "Open B	(B,D♯,F♯) Overtones": ["B", "B", "F♯", "B", "D♯", "F♯"],
    "Open B	(B,D♯,F♯)": ["B", "F♯", "B", "F♯", "B", "D♯"],
    "Open C	(C,E,G)": ["C", "G", "C", "G", "C", "E"],
    "Open C	(C,E,G) Repetive": ["C", "E", "G", "C", "E", "G"],
    "Open C	(C,E,G) Overtones": ["C", "C", "G", "C", "E", "G"],
    "Open D	(D,F♯,A)": ["D", "A", "D", "F♯", "A", "D"],
    "Open D	(D,F♯,A) Repetive": ["D", "F♯", "A", "D", "F♯", "A"],
    "Open D	(D,F♯,A) Overtones": ["D", "D", "A", "D", "F♯", "A"],
    "Open E	(E,G♯,B)": ["E", "G♯", "B", "E", "G♯", "B"],
    "Open E	(E,G♯,B)": ["E", "E", "B", "E", "G♯", "B"],
    "Open E	(E,G♯,B)": ["E", "B", "E", "G♯", "B", "E"],
    "Open F	(F,A,C)": ["F", "A", "C", "F", "A", "C"],
    "Open F	(F,A,C)": ["F", "F", "C", "F", "A", "C"],
    "Open F	(F,A,C)": ["C", "F", "C", "F", "A", "F"],
    "Open G	(G,B,D)": ["G", "B", "D", "G", "B", "D"],
    "Open G	(G,B,D)": ["G", "G", "D", "G", "B", "D"],
    "Open G	(G,B,D)": ["D", "G", "D", "G", "B", "D"]
};

let tunings_data = [];
for (let k in tunings) {
    let value = k;
    value += " - ";
    value += tunings[k];
    tunings_data.push(value);
};
