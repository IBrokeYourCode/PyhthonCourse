def positive_sum(arr):
    # Your code here
    if len(arr) == 0:
        return 0
    sumOfPositives = 0
    for i in arr:
        if i >= 0:
            sumOfPositives += i
    return sumOfPositives
#    return sum(x for x in arr if x > 0)
