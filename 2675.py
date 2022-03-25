import sys

T=int(sys.stdin.readline())
for i in range(T):
  arr=[]
  arr=list(map(str, sys.stdin.readline().split()))
  num=int(arr[0])
  S=arr[1]
  T=S[0]*num
  for j in range(1,len(S)):
    T=T+S[j]*num
  
  print(T)