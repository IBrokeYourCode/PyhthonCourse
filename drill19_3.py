from sys import argv
#script, arg1, arg2 = argv
def brak_sera(arg1, arg2):
    print "***BRAK SERA***\n***KOD BLEDU %d\n***DUPA %d" % (arg1, arg2)

#brak_sera(10, 15)
#brak_sera(int(arg1), int(arg2))
basic = int(raw_input("What is the meaning of life? "))
brak_sera(basic, basic * 2)
