def calculate(expression: str) -> float:
    expression = expression.replace(" ", "")
    stack = []
    current_num = 0
    last_operator = "+"
    for i, char in enumerate(expression + "+"):
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        if not char.isdigit() or i == len(expression):
            if last_operator == "+":
                stack.append(current_num)
            elif last_operator == "-":
                stack.append(-current_num)
            elif last_operator == "*":
                stack.append(stack.pop() * current_num)
            elif last_operator == "/":
                stack.append(stack.pop() / current_num)
            last_operator = char
            current_num = 0
    return round(float(sum(stack)), 2)
