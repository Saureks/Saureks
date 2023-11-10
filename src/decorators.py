import datetime
import functools
from typing import Callable


def log(filename: str = None) -> Callable:
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

    def decorator(func: Callable) -> Callable:
        log_file = None
        if filename:
            log_file = open(filename, 'a')

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                message = f"{current_time} {func.__name__} ok\n"
                if log_file:
                    log_file.write(message)
                else:
                    print(message)
                return result
            except Exception as e:
                error_type = type(e).__name__
                input_values = f"Inputs: {args}, {kwargs}\n"
                error_message = f"{current_time} {func.__name__} error: {error_type}. {input_values}"
                if log_file:
                    log_file.write(error_message)
                else:
                    print(error_message)
                raise
            finally:
                if log_file:
                    log_file.close()

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
