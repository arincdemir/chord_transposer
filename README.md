# chord_transposer
A program to quickly give out all the transposes of a song's chords.

- Copy the chords with the lyrics from a website.
- Paste it to the text file.
- Run the program.
- A new text file with the transposes should appear.

For now the program crashes if a chord appears several times in a line(a row). You might want to split the line so that there is no multiple instance of a chord before running the program.  

Also, It doesn't work with chords like Cmaj7 since I currently distinguish chords lyrics by looking at its length. The code thinks that Cmaj7 is a meaningful word, not a chord since it is longer than 3 characters.

Yeah I know, I'll fix these whenever possible. Though probably only I will be using this :(
