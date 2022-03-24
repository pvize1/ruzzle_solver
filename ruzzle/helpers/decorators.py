import functools
from time import time


def timer(func):
    """This function shows the execution time of the function object passed"""

    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print("")
        print(f"TIMER: function {func.__name__!r} executed in {(t2 - t1):.4f}s")
        return result

    return inner_func


def count_calls(func):
    """This function keeps count of number of times a function is called"""

    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        inner_func.calls += 1
        print(f"COUNT_CALLS: call {inner_func.calls} to {func.__name__!r}")
        return func(*args, **kwargs)

    inner_func.calls = 0
    return inner_func


def debug(func):
    """Print the function signature and return value"""

    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"DEBUG: calling {func.__name__!r}({signature})")
        value = func(*args, **kwargs)
        print(f"DEBUG: {func.__name__!r} returned {value!r}")
        return value

    return inner_func


def exception_handler(func):
    """Handles exceptions in a more compact method"""

    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except TypeError:
            print(f"EXCEPTION_HANDLER: {func.__name__} only takes numerical arguments")

    return inner_func


def trace(func):
    """Similar to debug, but simpler - from Python Tricks the Book"""

    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        print(f"TRACE: calling {func.__name__}() with {args}, {kwargs}")
        original_result = func(*args, **kwargs)
        print(f"TRACE: {func.__name__}() returned {original_result!r}")
        return original_result

    return inner_func
