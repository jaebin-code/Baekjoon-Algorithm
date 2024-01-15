def solution(s):
    stack = []
    stack.append(s[0])
    for i in range(1,len(s)):
        if(s[i] == ")"):
            if(len(stack) == 0):
                return False
            stack.pop()
        else:
            stack.append("(")
    if(len(stack) == 0):
        return True
    return False