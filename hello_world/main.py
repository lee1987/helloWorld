import logging
import sys
import time

from prometheus_client import CollectorRegistry, Counter, push_to_gateway


def process_request(c: Counter):
    """A dummy function that takes some time."""
    c.inc(1)  # Increment by 1
    time.sleep(1)


def logger():
    logger = logging.getLogger('helloWorld')
    handlers = [logging.StreamHandler(sys.stdout)]

    logging.basicConfig(
        format='%(asctime)s %(levelname)s %(module)s:%(funcName)s %(message)s',
        handlers=handlers
    )
    logger.setLevel(logging.DEBUG)
    return logger


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    logger = logger()
    logger.info('test')

    registry = CollectorRegistry()

    # Start a Counter
    c = Counter('this_is_a_metric', 'An example counter', registry=registry)

    # Generate some requests.
    while True:
        process_request(c)
        push_to_gateway('pushgateway:9091', job='job1', registry=registry)
