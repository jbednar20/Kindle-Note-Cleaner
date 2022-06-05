# Prompt user for input of their Kindle notes text file (must be in the same directory as scipt)
userInput = input("Please enter the name of your Kindle notes file: \n")

# Open/read in the text file provided by user input 
f = open(userInput, 'r')

# Clean up the book Title to a titleName.txt friendly format
titleName = f.readline() # Save book title to titleName string 
titleName = titleName.replace(":","_").replace(" ", "_").replace("'","") # Convert whitespace/pesky chars 
titleName = titleName.rstrip() # Remove newline char "\n" with rstrip()
titleName = titleName + '.txt' # Append titleName with .txt to identify/assign file type

# Write file for titleName, save Kindle notes related to current book 
bookNotes = open(titleName, 'x') # Create new .txt file called titleName
lines = open('Kindle_Clippings.txt', 'r').readlines()

i = 3 # Offset to extract the Kindle note/highlight

# Extract notes from the text file given as input (line 8)
while i < len(lines):
    bookNotes.write(lines[i])
    bookNotes.write('\n')
    i = i + 5
