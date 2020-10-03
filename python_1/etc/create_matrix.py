'''
  create matrix
  
  example
  n = 3
  m = 4
  [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
  ]
  
  run python ./etc/create_matrix.py
'''

n = int(input())
m = int(input())

matrix = []
for i in range(n):
  matrix.append([0] * m)
  
print(matrix)