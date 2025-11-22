import time, logging
logger = logging.getLogger(__name__)
from functools import wraps


def logExecutionTime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        logger.info("Startime: %r, endtime: %r and execution time: %r ", 
                    start,end, (end-start))
        
        return result, start, end
    return wrapper