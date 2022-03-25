import sys
a=0
b=0
N=int(sys.stdin.readline().rstrip())
for i in range(N):
  num=int(sys.stdin.readline().rstrip())
  if num==1:
    a+=1
  elif num==0:
    b+=1

if a>b:
  print("Junhee is cute!")
else:
  print("Junhee is not cute!")