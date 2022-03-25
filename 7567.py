import sys

N=sys.stdin.readline().rstrip()
height=10
for i in range(1, len(N)):
  if N[i]==N[i-1]:
    height=height+5
  else:
    height=height+10

print(height)