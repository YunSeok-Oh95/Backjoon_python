import sys

a=int(sys.stdin.readline())
opt=input()
b=int(sys.stdin.readline())

if opt=="+":
  num=a+b
  print(num)
elif opt=="*":
  num=a*b
  print(num)