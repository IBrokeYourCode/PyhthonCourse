from sys import argv
from os.path import exists

script, from_file, to_file = argv
print "Copying from %s to %s" % (from_file, to_file)
#indata stores the contents of from_file
indata = open(from_file).read()
print "The input file is %d bytes long" % len(indata)
#checks if the output file exists
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, Ctrl+C to abort."
raw_input()
#if the output does not exist, it is created. If it does exist, the content is wiped
#you could use 'a' to append the contents without wiping
out_file = open(to_file, 'w')
#copies the contents of input file to output file
out_file.write(indata)

print "Done."
#opens the out file in read mode, so now wiping
out_file = open(to_file, 'r')
print out_file.read()
out_file.close()
