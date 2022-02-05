
# The sequences of chords with half sound difference, ascending
chordList = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A",
"Am", "A#m", "Bm", "Cm", "C#m", "Dm", "D#m", "Em", "Fm", "F#m", "Gm", "G#m", "Am"]
def transposeUp(row : str):
    chords = row.split()
    for chord in chords:
        newChord = chordList[chordList.index(chord) + 1]
        row = replaceChord(row, chord, newChord)

    return row

def replaceChord(string: str, old: str, new: str):
    string = string + " "
    index = 0
    found = False
    #finding the index of the old chord
    for i in range(len(string)):
        for j in range(len(old) + 1):
            if j == len(old):
                if string[i + j] == " ":
                    index = i
                    found = True
            elif string[i + j] != old[j]:
                break
        if found:
            break
            
    newString = string[:index] + new + string[index + len(old):]
    return newString
    


# Get the chords from the user
fhand = open("paste_chords_here.txt", "r")
text = fhand.read()
fhand.close()

splitted = text.split("\n")

output = ""
lastTranspose = splitted
for i in range(12):
    currentTranspose = ""
    for row in lastTranspose:
        words = row.split()
        areChords = True
        for word in words:
            if len(word) > 3:
                areChords = False
                break
        if areChords:
            currentTranspose += transposeUp(row)
        else:
            currentTranspose += row
        currentTranspose += "\n"
    output +=  "\n\n -------------------------------------- \n\n" + currentTranspose
    lastTranspose = currentTranspose.split("\n")


# Write the transposed chords into a text file
fhand = open("transposed_chords.txt", "w")
fhand.write(output)
fhand.close()