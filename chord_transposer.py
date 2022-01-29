
# The sequences of chords with half sound difference, ascending
chordList = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A",
"Am", "A#m", "Bm", "Cm", "C#m", "Dm", "D#m", "Em", "Fm", "F#m", "Gm", "G#m", "Am"]
def transposeUp(row : str):
    chords = row.split()
    for chord in chords:
        newChord = chordList[chordList.index(chord) + 1]
        row = row.replace(chord, newChord)
    return row


# Get the chords from the user
fhand = open("paste_chords_here.txt", "r")
text = fhand.read()
fhand.close()

splitted = text.split("\n")

output = ""

for row in splitted:
    words = row.split()
    areChords = True
    for word in words:
        if len(word) > 3:
            areChords = False
            break
    if areChords:
        output += transposeUp(row)
    else:
        output += row
    output += "\n"


# Write the transposed chords into a text file
fhand = open("transposed_chords.txt", "w")
fhand.write(output)
fhand.close()