def min(arr):
    arr.sort()
    return (arr[len(arr)-1])

def max(arr):
    arr.sort(reverse = True)
    return (arr[len(arr)-1])

#best solution from Codewars (changed the name of methods to be different than in description
# and used Python's native functions)

#def m(arr):
#    return min(arr)
#
#def m(arr):
#    return max(arr)
