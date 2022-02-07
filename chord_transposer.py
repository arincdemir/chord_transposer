
# The sequences of chords with half sound difference, ascending
chordList = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A",
             "Am", "A#m", "Bm", "Cm", "C#m", "Dm", "D#m", "Em", "Fm", "F#m", "Gm", "G#m", "Am",
             "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A",
             "Am", "Bbm", "Bm", "Cm", "Dbm", "Dm", "Ebm", "Em", "Fm", "Gbm", "Gm", "Abm", "Am",
             ]


def transposeRowUp(row: str):
    chords = row.split()
    for chord in chords:
        newChord = chordList[chordList.index(chord) + 1]
        oldRow = row
        row = replaceChord(row, chord, newChord)

    return row


def replaceChord(string: str, old: str, new: str):
    string = string + " "
    index = 0
    found = False
    # finding the index of the old chord
    for i in range(len(string)):
        for j in range(len(old) + 1):
            if j == len(old):
                if string[i + j] == " " or string[i + j] == "\t":
                    index = i
                    found = True
            elif string[i + j] != old[j]:
                break
        if found:
            break

    newString = string[:index] + new + string[index + len(old):]
    return newString


chordAdditives = ["dim", "sus", "maj", "aug"]


def areChords(words):
    for word in words:
        # check whether word is one of the chords in the transpose list. If it is; go check the other words
        if word in chordList:
            continue

        # check whether the word starts with a chord name like "D". If not, then it's not a chord
        startsWithChordName = False
        for name in chordList:
            if word.startswith(name):
                startsWithChordName = True
                break
        if not startsWithChordName:
            return False

        # check whether the word is longer than 6 characters. It's super unlikely to be a chord if it is.
        if len(word) > 6:
            return False

        # if the chord is longer than 4 chars, it should have additives like "sus" in it.
        if len(word) > 4:
            additive_in = False
            for additive in chordAdditives:
                if additive in word:
                    additive_in = True
                    break
            if additive_in:
                continue
            else:
                return False

        # if the chord is shorter than or equal to 4 chars, it should have "7" or "9" in it.
        if 1 < len(word) <= 4:
            if "7" in word or "9" in word:
                continue
            else:
                return False

        # if the checks above don't apply, I'll assume that it is not a chord :)
        return False

    return True


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
        if areChords(words):
            currentTranspose += transposeRowUp(row)
        else:
            currentTranspose += row
        currentTranspose += "\n"
    output += "\n\n -------------------------------------- \n\n" + currentTranspose
    lastTranspose = currentTranspose.split("\n")


# Write the transposed chords into a text file
fhand = open("transposed_chords.txt", "w")
fhand.write(output)
fhand.close()
