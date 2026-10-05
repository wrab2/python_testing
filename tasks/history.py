#! python
class History:
    def __init__(self):
        self._records = []

    def add_record(self, operation, a, b, result):
        self._records.append({
            "operation": operation,
            "a": a,
            "b": b,
            "result": result,
        })

    def get_all(self):
        return list(self._records)

    def get_last(self):
        return self._records[-1] if self._records else None

    def clear(self):
        self._records.clear()

    def count(self):
        return len(self._records)