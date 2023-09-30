bracket=list(input())
stack = []
cnt = 0

for i in range(len(bracket)):
    if bracket[i] == "(":
        stack.append("(")
    else:
        if bracket[i-1] == "(":
            stack.pop()
            cnt += len(stack)
        else:
            cnt += 1
            stack.pop()

print(cnt)
