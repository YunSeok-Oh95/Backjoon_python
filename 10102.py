import sys

num=int(sys.stdin.readline().rstrip())
vote=sys.stdin.readline().rstrip()
a=0
b=0
for i in range(len(vote)):
  if vote[i]=="A":
    a=a+1
  elif vote[i]=="B":
    b=b+1
  
if a>b:
  print("A")
elif b>a:
  print("B")
else:
  print("Tie")