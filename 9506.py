import sys

while True:
  arr=[]
  sum=0
  N=int(sys.stdin.readline().rstrip())
  if N==-1:
    break
  for i in range(1, N):
    if N%i==0:
      arr.append(i)
  
  for j in range(len(arr)):
    sum=sum+arr[j]
  
  if sum==N:
    print(str(N)+" = ",end="")
    for i in range(0,len(arr)):
      print(str(arr[i]),end='')
      if i==len(arr)-1:
        print()
        break
      else:
        print(" + ",end='')
  else:
    print(str(N)+" is NOT perfect.")
