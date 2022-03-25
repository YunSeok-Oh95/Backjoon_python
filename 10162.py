import sys
T=int(sys.stdin.readline().rstrip())
if T%10!=0:
  print(-1)
else:
  a=T//300
  b=(T%300)//60
  c=(T%60)//10
  print(str(a)+' '+str(b)+' '+str(c))
