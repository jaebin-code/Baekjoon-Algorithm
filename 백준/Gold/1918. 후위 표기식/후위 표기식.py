infix = list(input())
resultWord = ""
stack = []

def get_precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    return 0

for i in infix:
    if i.isalpha():
        resultWord += i
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            resultWord += stack.pop()
        stack.pop()  # Remove the opening parenthesis from the stack
    else:
        while stack and get_precedence(stack[-1]) >= get_precedence(i):
            resultWord += stack.pop()
        stack.append(i)

while stack:
    resultWord += stack.pop()

print(resultWord)
