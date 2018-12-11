#make a function that accepts a list and returns a list of ints only
def filter_list(l):
    itemList = list(l)
    intList = list()
    print(itemList)
    for item in itemList:
        if type(item) is int:
            print("the item is: %d" % (item))
            intList.append(item)
            print(intList)
        else:
            print("the item is: %s" % (item))
    print(intList)
    return
filter_list([1, 2, 'z', 3, 'b', 'w', 'd', 'c'])

#topowe rozwiązanie z Codewars:
#def filter_list(l):
#  'return a new list with the strings filtered out'
#  return [i for i in l if not isinstance(i, str)]
