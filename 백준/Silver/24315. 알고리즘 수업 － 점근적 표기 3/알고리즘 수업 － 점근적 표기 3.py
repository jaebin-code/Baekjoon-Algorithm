a,b = map(int,input().split())
c,d = map(int,input().split())
e = int(input())

if((a*e+b)<=d*e and (a*e+b)>=c*e and a>=c and a<=d):
    print(1)
else:
    print(0)