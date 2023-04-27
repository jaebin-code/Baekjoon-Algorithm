n,k=map(int,input().split())
dic={}
for _ in range(n):
    word=input()
    if len(word)<k:
        continue
    if word in dic:
        dic[word]+=1
    else:
        dic[word]=1
dic=dict(sorted(dic.items(),key = lambda x : (-x[1],-len(x[0]),x[0])))
for i in dic.keys():
    print(i)