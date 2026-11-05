# I made this as an exercise for Data Structures class but in the end, i had to get AI to assist me a little.
# We were informed a question about prefix/postfix notation would be asked on the exam so by the time you're reading this, i might've got cooked.

expression = input("enter expression: ")
output = []
stack = []

precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

i = 0
while i < len(expression):
    char = expression[i]

    if char.isdigit():
        num = ""
        while i < len(expression) and expression[i].isdigit():
            num += expression[i]
            i += 1
        output.append(num)
        continue

    elif char in precedence:
        while stack and stack[-1] != "(" and precedence.get(stack[-1], 0) >= precedence[char]:
            output.append(stack.pop())
        stack.append(char)

    elif char == "(":
        stack.append(char)

    elif char == ")":
        while stack and stack[-1] != "(":
            output.append(stack.pop())
        if stack and stack[-1] == "(":
            stack.pop()

    i += 1

while stack:
    output.append(stack.pop())

postfix = " ".join(output)
print(postfix)