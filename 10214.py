import sys

T=int(sys.stdin.readline().rstrip())

for i in range(T):
  sum_a=0
  sum_b=0
  for j in range(9):
    a, b=map(int, sys.stdin.readline().split())
    sum_a=sum_a+a
    sum_b=sum_b+b
  if sum_a>sum_b:
      print("Yonsei")
  elif sum_a<sum_b:
      print("Korea")
  else:
      print("Draw")  

