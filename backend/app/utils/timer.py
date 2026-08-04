#timing metrics
import time
from functools import wraps
from app.utils.logger import logger

LATENCY_METRICS={} #stores the time values.

def measure_time(operation_name):
    def decorator(function):
        @wraps(function)
        def wrapper(*args,**kwargs):
            start_time=time.perf_counter()
            result=function(*args,**kwargs)
            end_time=time.perf_counter()
            elapsed=round(end_time-start_time,4)
            LATENCY_METRICS[operation_name]=elapsed
            logger.info(f"{operation_name}:{elapsed} seconds")
            return result
        return wrapper
    return decorator

def get_latency_metrics():
    return LATENCY_METRICS

def reset_latency_metrics():
    LATENCY_METRICS.clear()