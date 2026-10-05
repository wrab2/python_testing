#! python
import pytest
from unittest.mock import Mock
from service import CalculatorService

@pytest.fixture
def mock_history():
    return Mock()

@pytest.fixture
def service(mock_history):
    return CalculatorService(history=mock_history)

def test_calculate_does_not_call_add_record_on_divide_by_zero(service, mock_history):
    with pytest.raises(ValueError):
        service.calculate("/", 5, 0)
    mock_history.add_record.assert_not_called()

def test_calculate_propagates_history_error(service, mock_history):
    mock_history.add_record.side_effect = RuntimeError("DB locked")
    with pytest.raises(RuntimeError, match="DB locked"):
        service.calculate("+", 1, 1)

def test_last_result_returns_value_from_history(service, mock_history):
    mock_history.get_last.return_value = {"operation": "+", "a": 1, "b": 2, "result": 3}
    assert service.last_result() == 3

@pytest.mark.parametrize("operation, a, b, expected", [
    ("+", 2, 3, 5),
    ("-", 10, 4, 6),
    ("*", 3, 7, 21),
    ("/", 8, 2, 4),
    ("^", 2, 5, 32),
])

def test_calculate_parametrized_with_mock(service, mock_history, operation, a, b, expected):
    result = service.calculate(operation, a, b)
    assert result == pytest.approx(expected)
    mock_history.add_record.assert_called_once_with(operation, a, b, pytest.approx(expected))

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])   