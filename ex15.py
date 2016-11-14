from sys import argv
#the script and filename variables will be pulled from argv
script, filename = argv
#opens the file and loads it into memory
txt = open(filename)
#shows the file name
print "Here's your file %r" % filename
#shows the contents of the file loaded in line 5
print txt.read()
txt.close()
print "Type the filename again."
file_again = raw_input("> ")
#open the file requested in 12
txt_again = open(file_again)
#prints the file opened in 14
print txt_again.read()
txt_again.close()
