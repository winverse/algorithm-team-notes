# N, M, K를 공백을 기준으로 구분하여 입력 받기
# N: 배열의 크기
# M: 숫자가 더해지는 횟수
# K: 반복 제한 숫자

n, m, k = map(int, input().split());
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

# 전략 !
# 정렬 -> 최대, 다음 최댓값 구하고
# 최대값이 몇번 들어간지 계산
# 계산한 값을 전체 반복 횟수에서 빼버리면 다음 최댓값이 들어갈 횟수를 구할 수가 있다.

data.sort()

maxNum = data[-1]
nextMaxNum = data[-2]


count = int(m / (k + 1)) * k
count += m % (k + 1);

result = 0;
result += count * maxNum
result += (m - count) * nextMaxNum

print(result)
