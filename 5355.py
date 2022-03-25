import sys
N=int(sys.stdin.readline())
for i in range(N):
  arr=[]
  arr=list(map(str, input().split()))
  sum=float(arr[0])
  for j in range(1,len(arr)):

    if arr[j]=="@":
      sum=sum*3
    elif arr[j]=="%":
      sum=sum+5
    elif arr[j]=="#":
      sum=sum-7

  print("{:.2f}".format(sum))