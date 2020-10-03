m = 10
k = 3

arr = [2,4,5,4,6]

n = len(arr)

arr.sort()

maxNum = arr[-1]
nextMaxNum = arr[-2]

groupLeng = k + 1
group = (maxNum * k + nextMaxNum)

rest = m % groupLeng
share = m // groupLeng

result = (share * group) + (rest * maxNum)

print(result)
