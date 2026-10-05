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
    from service import CalculatorService
    calc = CalculatorService()
    print("операции: +, -, *, /, ^")
    print("выход: 'q', история: 'h' ")

    while True:
        op = input("\nвведите операцию (+, -, *, /, ^), выход: 'q', история: 'h': ").strip()

        if op == 'q':
            break

        if op == 'h':
            records = calc.history.get_all()
            if not records:
                print("история пуста")
            else:
                for i, r in enumerate(records, 1):
                    print(f"{i}. {r['a']} {r['operation']} {r['b']} = {r['result']}")
            continue

        if op == 'c':
            calc.clear_history()
            print("история очищена")
            continue

        if op not in ('+', '-', '*', '/', '^'):
            print("Неверная операция. Попробуйте снова.")
            continue

        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: нужно ввести число.")
            continue

        result = calc.calculate(op, a, b)

        print(f"Результат: {result}")

if __name__ == "__main__":
    calculator()