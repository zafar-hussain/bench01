"""
     _summary_

    _extended_summary_
    """
from typing import Callable


def fibonacci(n: int) -> int:
    """
    fibonacci _summary_

    _extended_summary_

    Args:
        n (int): _description_

    Returns:
        int: _description_
    """
    if n < 3:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def test_fibonacci_simple_3(benchmark: Callable) -> None:
    """
    test_fibonacci_simple_3 _summary_

    _extended_summary_

    Args:
        benchmark (_type_): _description_
    """
    assert benchmark(fibonacci, 4) == 3


# if __name__ == "__main__":
#     print(fibonacci(20))
