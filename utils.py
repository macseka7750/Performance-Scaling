import time
import functools
import logging

logger = logging.getLogger(__name__)

def time_execution(func):
    """
    Decorator that logs the execution time of a function.
    Essential for identifying bottlenecks in a scaling project.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        
        duration = (end_time - start_time) * 1000  # Convert to ms
        logger.info(f"PERFORMANCE: {func.__name__} took {duration:.2f}ms")
        
        return result
    return wrapper
