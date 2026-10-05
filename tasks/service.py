#! python
from calculator import add, subtract, multiply, divide, power
from history import History


class CalculatorService:
    OPERATIONS = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "^": power,
    }

    def __init__(self, history=None):
        self.history = history if history is not None else History()

    def calculate(self, operation, a, b):
        if operation not in self.OPERATIONS:
            raise ValueError(f"Неизвестная операция: {operation}")
        result = self.OPERATIONS[operation](a, b)
        self.history.add_record(operation, a, b, result)
        return result

    def last_result(self):
        record = self.history.get_last()
        return record["result"] if record else None

    def clear_history(self):
        self.history.clear()