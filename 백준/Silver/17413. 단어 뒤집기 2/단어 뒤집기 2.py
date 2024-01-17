word = list(input())
lastWord = ""
stack = []

flag = 0

for i in range(len(word)):
    if flag == 0:
        if(word[i] == "<"):
            flag = 1
            for _ in range(len(stack)):
                lastWord += stack.pop()
            lastWord += "<"
        elif(word[i] == " "):
            for _ in range(len(stack)):
                lastWord += stack.pop()
            lastWord += " "
        else:
            stack.append(word[i])
    else:
        lastWord += word[i]
        if word[i] == ">":
            flag = 0

for _ in range(len(stack)):
    lastWord += stack.pop()
print(lastWord)