#! python
import pytest

from history import History
from service import CalculatorService


@pytest.fixture
def history():
    return History()


@pytest.fixture
def service(history):
    return CalculatorService(history=history)


def test_service_uses_calculator_and_history(service, history):
    result = service.calculate("+", 2, 3)
    assert result == 5
    assert history.count() == 1
    assert history.get_last()["result"] == 5


def test_multiple_operations_accumulate_in_history(service, history):
    service.calculate("+", 1, 2)
    service.calculate("*", 3, 4)
    service.calculate("-", 10, 5)
    assert history.count() == 3
    assert [r["result"] for r in history.get_all()] == [3, 12, 5]


def test_last_result_returns_latest(service):
    service.calculate("+", 1, 1)
    service.calculate("*", 5, 5)
    assert service.last_result() == 25


def test_last_result_empty_history(service):
    assert service.last_result() is None


def test_clear_history_resets_state(service, history):
    service.calculate("+", 1, 1)
    service.calculate("-", 5, 2)
    service.clear_history()
    assert history.count() == 0
    assert service.last_result() is None


def test_divide_by_zero_does_not_save_to_history(service, history):
    with pytest.raises(ValueError):
        service.calculate("/", 5, 0)
    assert history.count() == 0


def test_unknown_operation_raises(service, history):
    with pytest.raises(ValueError, match="Неизвестная операция"):
        service.calculate("%", 1, 1)
    assert history.count() == 0


def test_service_with_custom_history():
    custom = History()
    svc = CalculatorService(history=custom)
    svc.calculate("^", 2, 3)
    assert custom.count() == 1
    assert custom.get_last()["operation"] == "^"


@pytest.mark.parametrize("operation, a, b, expected", [
    ("+", 2, 3, 5),
    ("-", 10, 4, 6),
    ("*", 3, 7, 21),
    ("/", 8, 2, 4),
    ("^", 2, 5, 32),
])
def test_full_pipeline_parametrized(service, history, operation, a, b, expected):
    result = service.calculate(operation, a, b)
    assert result == pytest.approx(expected)
    assert history.count() == 1
    record = history.get_last()
    assert record["operation"] == operation
    assert record["a"] == a
    assert record["b"] == b
    assert record["result"] == pytest.approx(expected)


def test_history_isolated_between_services(history):
    svc1 = CalculatorService(history=history)
    svc2 = CalculatorService(history=History())
    svc1.calculate("+", 1, 1)
    svc2.calculate("+", 2, 2)
    assert svc1.history.count() == 1
    assert svc2.history.count() == 1
    assert svc1.last_result() == 2
    assert svc2.last_result() == 4

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])   