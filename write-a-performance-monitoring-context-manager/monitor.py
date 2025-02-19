from collections import Counter
from contextlib import contextmanager
from datetime import date
from time import time

OPERATION_THRESHOLD_IN_SECONDS = 2.2
ALERT_THRESHOLD = 3
ALERT_MSG = 'ALERT: suffering performance hit today'

violations = Counter()


def get_today():
    """Making it easier to test/mock"""
    return date.today()


@contextmanager
def timeit():
    """"
    Complete the timeit context manager implementing mentioned timing in seconds (duration).
    Keep track of performance violations which we define as duration >= 2.2 (OPERATION_THRESHOLD_IN_SECONDS).
    If there are >= 3 (ALERT_THRESHOLD) violations the same day, print ALERT: suffering performance hit today (ALERT_MSG).
    """
    start = time()
    yield
    end = time()
    duration = end - start
    alerts = 0
    if duration > OPERATION_THRESHOLD_IN_SECONDS:
        alerts += 1
        print("error")