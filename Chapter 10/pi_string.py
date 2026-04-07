from pathlib import Path

# allows python to access the file 
path = Path('pi_digits.txt')

# the method read_text() from pathlib reads text from the file in path and the 
# content is returned as a single string and assigned to the variable contents
contents = path.read_text()

# the splitlines() method takes a long string and splits the string into a set 
# of lines. what is then returned is a list of lines and its assigned to the 
# variable lines. 
lines = contents.splitlines()

# creating an empty string and assigning it to the variable pi_string
pi_string = ''

# looping through the list generated from the method splitlines() and then
# adding the line from the list "lines" to the empty string 
for line in lines:
    pi_string += line.lstrip()
    
print(pi_string)
print(len(pi_string))