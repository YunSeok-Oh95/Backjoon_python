import sys
N=int(sys.stdin.readline().rstrip())
A=100
B=100
for i in range(N):
  a, b=map(int, sys.stdin.readline().split())
  if a>b:
    B=B-a
  elif a<b:
    A=A-b

print(A)
print(B)