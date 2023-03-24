while True:
    a,b,c=map(int, input().split())
    list1=[a,b,c]
    list1.sort()
    if(a==0 and b==0 and c==0):
        break
    elif(list1[2]>=(list1[1]+list1[0])):
        print("Invalid")
    elif(a==b==c):
        print("Equilateral")
    elif(a==b or a==c or b==c):
        print("Isosceles")
    else:
        print("Scalene")