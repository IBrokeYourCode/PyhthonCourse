from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit Ctrl + C. (^C)"
print "If you do want that, hit RETURN."
#displays a ? prompt where you have to press enter to continue
raw_input("?")

print "Opening the file..."
#opens the file. w for writing TRUNCATES when it opens, r for reading, a for appending
#If you pass no arguments, r is the default
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
#wipes the contents of the file and SAVES the file
target.truncate

print "Now I'm going to ask you for three lines."
#asks for input
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
to_write = line1 + "\n" + line2 + "\n" + line3 + "\n"

print "I'm going to write these to the file."
#writes the lines into the files BUT DOES NOT SAVE THE FILE
target.write(to_write)

#at prompt, press ENTER to continue
raw_input("?")
print "And finally, we close it."
#saves the file
target.close()
