import sys

T=int(sys.stdin.readline().rstrip())

for i in range(T):
  N=int(sys.stdin.readline().rstrip())
  arr_a=[]
  arr_b=[]
  for j in range(N):
    a, b=map(str, sys.stdin.readline().split())
    arr_a.append(a)
    arr_b.append(int(b))
  ind=arr_b.index(max(arr_b))  
  print(arr_a[ind])