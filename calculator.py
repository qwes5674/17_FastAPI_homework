from fastapi import HTTPException

def calculate(num1: int, num2: int, operator: str) -> int:
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '%':
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        return num1 % num2
    else:
        raise HTTPException(status_code=400, detail="Invalid operator")