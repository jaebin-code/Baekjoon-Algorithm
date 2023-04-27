def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
case=int(input())
for _ in range(case):
    k,n=map(int,input().split())
    print(factorial(n)//(factorial(k)*factorial(n-k)))