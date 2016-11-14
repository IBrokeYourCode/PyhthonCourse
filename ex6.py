#a string that starts the joke
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who %s and those who %s" % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
# sets a joke_evaluation variable that needs a %r value
joke_evaluation = "Isn't that joke funny?! %r"
# print the joke_evaluation where hilarious is the value of %r
print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
