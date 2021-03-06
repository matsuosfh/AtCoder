#AtCoder Regular Contest 109
#A - Hands

#A - Hands
a,b,x,y= map(int,input().split())

h = abs(b-a)
ans = min(x*h+y,y*(h-1)+x,y*h+x)
print(ans)
