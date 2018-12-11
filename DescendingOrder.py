#Your task is to make a function that can take any non-negative integer as a
#argument and return it with it's digits in descending order. Essentially,
#rearrange the digits to create the highest possible number.
import sys
def Descending_Order(num):
#    digits = str(num)
#    print(digits)
#    digitsList = list(digits)
#    print(digitsList)
#    digitsList.sort(reverse = True)
#    print(digitsList)
#    sortedString = ''.join(digitsList)
#    print(sortedString)
#    print(int(sortedString))
    print(int(''.join(sorted(str(num), reverse = True))))
#    print(int(''.join(sorted(list(str(num)), reverse = True)))
Descending_Order(1416)
