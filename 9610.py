import sys

N=int(sys.stdin.readline().rstrip())
a=0
b=0
c=0
d=0
e=0
for i in range(N):
  x, y=map(int, sys.stdin.readline().rstrip().split())
  if x==0 or y==0:
    e+=1
  elif x>0 and y>0:
    a+=1
  elif x<0 and y>0:
    b+=1
  elif x<0 and y<0:
    c+=1
  elif x>0 and y<0:
    d+=1

print("Q1: "+str(a))
print("Q2: "+str(b))
print("Q3: "+str(c))
print("Q4: "+str(d))
print("AXIS: "+str(e))
