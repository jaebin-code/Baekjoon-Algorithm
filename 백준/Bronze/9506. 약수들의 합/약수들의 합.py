num=0
while (num!=-1): 
    a=[1]
    num=int(input())
    if(num==-1):
        break
    for i in range(2,num//2):
        if(num%i==0):
            if(i not in a):
                a.append(i)
                if(i!=num//i):
                    a.append(num//i)
    a.sort()
    if(sum(a)==num):
        print(f"{num} = ",end='')
        for i in range(len(a)-1):
            print(f"{a[i]} + ",end='')
        print(a[-1])
    else:
        print(f"{num} is NOT perfect.")
