import datetime
import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызова функции и ее результатов.

    Args:
    filename (str): Имя файла, куда будут записываться логи. Если не указан, логи будут выводиться в консоль.

    Returns:
    Обернутую функцию с логированием.

    Пример использования:
    @log(filename="mylog.txt")
    def example_function(x, y):
        return x + y

    example_function(1, 2)
    """

    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                log_message = f"{current_time} {func.__name__} ok\n"
            except Exception as e:
                log_message = f"{current_time} {func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                result = None
            if filename:
                with open(filename, "a") as file:
                    file.write(log_message)
            else:
                print(log_message)
            return result

        return inner

    return wrapper


@log()
def my_function(x, y):
    return x + y


print(my_function(1, 2))
