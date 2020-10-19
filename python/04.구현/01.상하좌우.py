n = input();

data = list(map(str, input().split()));

# x <= n
# y <= n

x = 1;
y = 1;

for i in data: 
  if i == 'R' and y != 5:
    y += 1;
  if i == 'L' and y != 1:
    y -= 1;
  if i == 'U' and x != 1:
    x -= 1;
  if i == 'D' and x != 5:
    x += 1;

print(x, y);
    
    
