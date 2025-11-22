import time
from functools import wraps

def logExecutionTime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return result, start, end
    return wrapper