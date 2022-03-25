import sys

N=int(sys.stdin.readline())
for j in range(N):
  num=sys.stdin.readline()
  list=[]
  sum=0
  if num[0]=="O":
    list.append(1)
  else:
    list.append(0)

  for i in range(1,len(num)):
    if num[i]=="O":
      if num[i-1]=="O":
        list.append(list[i-1]+1)
      else:
        list.append(1)
    else:
      list.append(0)
  for k in range(len(list)):
    sum=sum+list[k]
  print(sum)