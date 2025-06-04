def strict(func):
    def wrapper(*args, **kwargs):
        for arg_name, arg_value in zip(func.__code__.co_varnames, args):
            expected_type = func.__annotations__[arg_name]
            if not isinstance(arg_value, expected_type):
                raise TypeError(
                    f"Аргумент '{arg_name}' не соответствует типу")
        return func(*args, **kwargs)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError
