a,b,c=map(int,input().split())
d=int(input())
e=int(input())

a1=a-d
if(a>0):
    if((a*(e)**2+b*e+c)<=d*(e**2) and a<=d) and b**2-4*a1*c<=0:
        print(1)
    elif(((a*(e)**2+b*e+c)<=d*(e**2) and a<=d) and b**2-4*a1*c>0):
        if(a1==0):
            print(1)
        elif(e<max(((-b+(b**2-4*a1*c)**0.5)/(2*a1)),((-b-(b**2-4*a1*c)**0.5)/(2*a1)))):
            print(0)
        else:
            print(1)
    else:
        print(0)
elif(a==0):
    print(0)
else:
    if(b**2-4*a1*c>0 and (a*(e**2)+b*e+c)<=d*(e**2)):
        if(e<max(((-b+(b**2-4*a1*c)**0.5)/(2*a1)),((-b-(b**2-4*a1*c)**0.5)/(2*a1)))):
            print(0)
        else:
            print(1)
    else:
        print(1)