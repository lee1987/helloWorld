import time

from prometheus_client import CollectorRegistry, Counter, push_to_gateway

from hello_world.io.echo import Echo


def process_request(c: Counter):
    """A dummy function that takes some time."""
    c.inc(1)  # Increment by 1
    time.sleep(1)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    echo = Echo('hello world')
    echo.echo()

    registry = CollectorRegistry()

    # Start a Counter
    c = Counter('this_is_a_metric', 'An hello world counter', registry=registry)

    # Generate some requests.
    while True:
        process_request(c)
        push_to_gateway('pushgateway:9091', job='job1', registry=registry)
