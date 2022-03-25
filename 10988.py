import sys

N=sys.stdin.readline().rstrip()
a=0
for i in range(int(len(N)/2)):
  if N[i]==N[len(N)-1-i]:
    a+=1

if a==int(len(N)/2):
  print(1)
else:
  print(0)