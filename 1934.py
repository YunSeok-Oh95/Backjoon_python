import sys
def gcd(a, b):
  if b==0:
    return a
  else:
    return gcd(b, a%b)

N=int(sys.stdin.readline())
for i in range(N):
  a, b=map(int, sys.stdin.readline().split())
  print(int((a*b)/gcd(a,b)))
