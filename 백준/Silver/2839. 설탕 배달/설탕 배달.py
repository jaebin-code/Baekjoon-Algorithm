a=int(input())
if a<5:
    if a==3:
        print(1)
    else:
        print(-1)
        
else:
    max5=a//5
    remain=a%5
    if remain==0:
        print(max5)
    else:
        b=remain//3
        c=remain%3
        if c==0:
            print(max5+b)
        else:
            while(max5>0):
                max5=max5-1
                remain=remain+5
                if remain%3==0:
                    print(max5 + remain//3)
                    k=max5 + remain//3
                    break
                else:
                    k=0
                    continue
            if k == 0:
                print(-1)