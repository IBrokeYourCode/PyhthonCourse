#this one is like scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#you can also get rid of *args and do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r", % (arg1, arg2)
