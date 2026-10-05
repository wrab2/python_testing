#! python
import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("ошибка")
    return a / b

def power(a, b):
    return math.pow(a, b)

def calculator():
    print("операции: +, -, *, /, ^")
    print("для выхода введите 'q'")

    while True:
        op = input("\nвведите операцию (+, -, *, /, ^) или 'q': ").strip()

        if op == 'q':
            break

        if op not in ('+', '-', '*', '/', '^'):
            print("Неверная операция. Попробуйте снова.")
            continue

        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: нужно ввести число.")
            continue

        if op == '+':
            result = add(a, b)
        elif op == '-':
            result = subtract(a, b)
        elif op == '*':
            result = multiply(a, b)
        elif op == '/':
            result = divide(a, b)        
        elif op == '^':
            result = power(a, b)

        print(f"Результат: {result}")

if __name__ == "__main__":
    calculator()