num=input()
num=int(num)

if num%4==0 and num%100!=0:
    print("1")
elif num%4==0 and num%400==0:
    print("1")
else:
    print("0")
