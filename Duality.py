import sys,random

input = sys.stdin.readline

for _ in range(int(input())):
    dots = []
    new = []
    n = int(input())
    for i in range(1,n+1):
        x,y = map(int, input().split())
        dots.append([i, x, y])
    dots.sort(key= lambda x: (x[1],x[2]))
    k = 1
    for name_,x,y in dots:
        new_y = y + 10**8
        new.append([name_,x+1,new_y])
        k *= -1
    for name,x,y in new:
        print(name, x, y)