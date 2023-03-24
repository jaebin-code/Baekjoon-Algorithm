num1,den1=map(int,input().split())
num2,den2=map(int,input().split())

# 유클리드로 분모 최소공배수 찾기
x,y=min(den1,den2),max(den1,den2)
while(x!=0):
    x,y=y%x,x
den=den1*den2/y
num=num1*(den/den1)+num2*(den/den2)
x,y=min(den,num),max(den,num)
while(x!=0):
    x,y=y%x,x
den/=y
num/=y
print(int(num),int(den))