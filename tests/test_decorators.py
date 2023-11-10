from src.decorators import log


@log(filename="test_log.txt")
def add(x, y):
    return x + y


def test_log_decorator_1():
    assert add(3, 5) == 8
