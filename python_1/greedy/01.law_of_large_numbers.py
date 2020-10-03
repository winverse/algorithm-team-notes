# N: 배열의 크기
# M: 숫자가 더해지는 전체 횟수
# K: 동일한 숫자를 더할때 초과할 수 없는 반복 횟수

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()

first = data[n - 1]
second = data[n - 2]

result = 0

while True:
  for i in range(k):
    if m == 0:
      break;
    result += first
    m -= 1
  if m == 0:
    break
  result += second
  m -= 1

print(result)