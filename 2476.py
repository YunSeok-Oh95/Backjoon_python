import sys
N=int(sys.stdin.readline())
arr=[]
for i in range(N):
  a, b, c=map(int, sys.stdin.readline().split())
  if a==b and b==c :
    money=10000+a*1000
  elif a==b and b!=c:
    money=1000+a*100
  elif a==c and b!=c:
    money=1000+a*100
  elif b==c and a!=b:
    money=1000+b*100
  elif a!=b and b!=c and c!=a:
    money=max(a,b,c)*100
  arr.append(money)

print(max(arr))
  
