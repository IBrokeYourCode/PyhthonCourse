#how short can I make this?
#the semicolon functions like a line break
#argv2 is the third argument - the script name is on position 0!
from sys import argv; open(argv[2], 'w').write(open(argv[1]).read())
#no need to close() in this case
