import sys

a, b, c=map(int, sys.stdin.readline().split())

if a*b>=c:
  print(a*b-c)
else:
  print(0)