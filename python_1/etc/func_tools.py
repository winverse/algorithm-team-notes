from functools import reduce

list1 = [1,2,3,4,5,6]
list2 = [7,8,9,10,11,12]

arrayAdded = list(map(lambda a, b: a + b, list1, list2))
filtered = list(filter(lambda a: a % 2 == 1, list1))
added = reduce(lambda a, b: a + b, list1)

print(arrayAdded, filtered, added)
