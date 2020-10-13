var tunings = {
    "Standard": ["E2", "A2", "D3", "G3", "B3", "E4"],
    "Drop-D": ["D2", "A2", "D3", "G3", "B3", "E4"],
    "Nashville": ["E3", "A3", "D4", "G4", "B3", "E4"],
    "Open A": ["E", "A", "C♯", "E", "A", "E"],
    "Open A Slide": ["E", "A", "E", "A", "C♯", "E"],
    "Open A Alternative": ["E", "A", "E", "A", "E", "C♯"]
};

var tunings_data = [];
for (var k in tunings) {
    var value = k;
    value += " - ";
    value += tunings[k];
    tunings_data.push(value);
};
