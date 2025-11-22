import time, logging
logger = logging.getLogger(__name__)
from functools import wraps

def logExecutionTime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        duration =end-start

        logger.info(f"Execution time: {duration * 1000:.3f} ms")
        
        return result, start, end
    return wrapper