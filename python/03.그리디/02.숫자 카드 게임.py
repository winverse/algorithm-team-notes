m, n = list(map(int, input().split()))

arr = []

low_numbers = []

for i in range(m):
  k = list(map(int, (input().split())))
  low_numbers.append(min(k))
  
# for a in arr:
#   max_numbers = 100000;
#   for b in a:
#     if (b < max_numbers):
#       max_numbers = b;
#   low_numbers.append(max_numbers)
  
low_numbers.sort(reverse=True);

result = low_numbers[0]

print(result)
