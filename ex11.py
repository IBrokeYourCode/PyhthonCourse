#the comma at the end of the line makes the raw_input() print in the same line as the question
print "How old are you?",
#raw_input presents a prompt, gets input, returns the user as a string. The argument in brackets is the prompt.
age = int(raw_input())
height = raw_input("How tall are you? ")
print "How much do you weigh?",
weight = raw_input("> ")

print "So, you're %d old, %s tall, and %s heavy" % (age, height, weight)
