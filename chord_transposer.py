
# Get the chords from the user
fhand = open("paste_chords_here.txt", "r")
text = fhand.read()
fhand.close()

splitted = text.split("\n")

print(splitted)