#defines a function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses." % cheese_count
    print "You have %d boxes of crackers." % boxes_of_crackers
    print "That's enough for a party! \n"
#end of function


print "We can just give the function numbers directly:"
#calls the function
cheese_and_crackers(20, 30)


print "Or we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
#calls the function using the two variables above as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside:"
cheese_and_crackers(10 + 20, 5 + 6)


print "Or we can combine variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print "We can ask for values:"
#raw_input returns a string, you have to int() it to get an integer
asked_cheese = int(raw_input("How many cheeses? >"))
asked_crackers = int(raw_input("How many crackers? >"))
cheese_and_crackers(asked_cheese, asked_crackers)
