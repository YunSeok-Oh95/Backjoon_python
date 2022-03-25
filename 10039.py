import sys
arr=[]
for i in range(5):
  num=int(sys.stdin.readline().rstrip())
  arr.append(num)
for i in range(5):
  if arr[i]<40:
    arr[i]=40
num=int((arr[0]+arr[1]+arr[2]+arr[3]+arr[4])/5)
print(num)