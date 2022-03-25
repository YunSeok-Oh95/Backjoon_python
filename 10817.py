import sys

a, b, c=map(int, sys.stdin.readline().split())

if a>=b & b>=c:
  print(b)
elif a<=b & b<=c:
  print(b)
elif b>=a & a>=c:
  print(a)
elif b<=a & a<=c:
  print(a)
elif a>=c & c>=b:
  print(c)
elif a<=c & c<=b:
  print(c)