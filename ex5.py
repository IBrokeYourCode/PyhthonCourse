name = 'Zed A. Shaw'
age = 35
height = 74
height_in_cm = height * 2.54
weight = 180
weight_in_kg = weight * 0.5
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s" % name
print "He's %d inches tall" % height_in_cm
print "He's %d pounds heavy." % weight_in_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d" % (age, height_in_cm, weight_in_kg, age + height_in_cm + weight_in_kg)
