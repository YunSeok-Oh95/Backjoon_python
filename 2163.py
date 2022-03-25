import sys

N,M=map(int, sys.stdin.readline().split())

row=M-1
col=(N-1)*M

print(row+col)