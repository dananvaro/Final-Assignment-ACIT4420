import time, logging
logger = logging.getLogger(__name__)
from functools import wraps

def logExecutionTime(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        # Starts the timer before calling the function
        start = time.perf_counter()
        # Calls the funtion
        result = func(*args, **kwargs)
        # Ends the timer after function has ended
        end = time.perf_counter()
        
        duration =end-start

        # Logs execution time and formats it in ms
        logger.info(f"Execution time: {duration * 1000:.3f} ms")
        
        #returns result, start and end time
        return result, start, end
    return wrapper