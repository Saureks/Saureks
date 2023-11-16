import os.path
import datetime
import pytest

from src.decorators import log


@pytest.mark.parametrize(
    "arg_1, arg_2, expexted_result", [(1, 0, " foo error: ZeroDivisionError. Inputs: (1, 0), {}"), (1, 2, " foo ok")]
)
def test_log_decorator_1(arg_1, arg_2, expexted_result):
    filename = "test.txt"
    if os.path.exists(filename):
        os.remove(filename)

    @log(filename)
    def foo(x: int, y: int) -> float:
        return x / y

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    foo(arg_1, arg_2)

    with open(filename) as file:
        log_mess = file.read().strip()

    expected_log = now + expexted_result

    assert log_mess == expected_log
