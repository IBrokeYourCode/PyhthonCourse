from sys import argv

script, filename = argv

file_read = open(filename)

print file_read.read()

file_read.close()
