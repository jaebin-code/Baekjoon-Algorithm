for _ in range(int(input())):
    num=int(input())
    list1=[25,10,5,1]
    for i in list1:
        print(num//i,end=' ')
        num%=i
    print()