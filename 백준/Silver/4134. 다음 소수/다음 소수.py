def isPrime(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if(x%i==0):
            return False
    return True

for _ in range(int(input())):
    num=int(input())
    while True:
        if(isPrime(num)==True):
            print(num)
            break
        num+=1