import sys

N=int(sys.stdin.readline().rstrip())

for i in range(N):
  r, e, c=map(int, sys.stdin.readline().rstrip().split())

  if r+c<e:
    print("advertise")
  elif r+c==e:
    print("does not matter")
  else:
    print("do not advertise")