import sys
N=int(sys.stdin.readline())
sum=0
i=1
while True:
  sum=sum+i
  if sum>N:
    break
  else:
    i=i+1
print(i-1)