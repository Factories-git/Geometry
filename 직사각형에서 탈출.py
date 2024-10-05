x,y,w,h = map(int, input().split())
print(min(abs(w-x), abs(x-0), abs(y-h), abs(y-0)))