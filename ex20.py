from sys import argv

script, input_file = argv
def print_all(f):
    print f.read()


def rewind(f):
    #seek() searches the file. It takes two arguments. The first is OFFSET, which is
    #how many bytes you will move. The second is FROM_WHERE, which defaults to
    #0 (beginning of file), and can be 1 (current line) or 2 (end of file)
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First, let's print the whole file.\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape.\n"

rewind(current_file)

print "Let's print three lines:\n"

current_line = 1
print_a_line(current_line, current_file)
# current_line += 1 works the same as current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
