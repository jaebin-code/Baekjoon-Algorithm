import sys
input=sys.stdin.readline

n=int(input().rstrip())
prime=[False,False]+[True]*(n-1)
primes=[]
for i in range(2,int(n**0.5)+1):
    if prime[i]:
        for j in range(2*i,n+1,i):
            prime[j]=False
for i in range(n+1):
    if prime[i] == True:
        primes.append(i)
cnt=0
idx1=0
idx2=0
num=0
leng=len(primes)
while True:
    if num==n:
        cnt+=1
    if num>n:
        num-=primes[idx1]
        idx1+=1
    elif idx2==leng:
        break
    else:
        num+=primes[idx2]
        idx2+=1
print(cnt)