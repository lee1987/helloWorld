import logging
import sys


class Echo(object):
    """
    echo stm
    """

    def __init__(self, text: str):
        self._text = text
        self._logger = logging.getLogger('helloWorld')
        handlers = [logging.StreamHandler(sys.stdout)]

        logging.basicConfig(
            format='%(asctime)s %(levelname)s %(module)s:%(funcName)s %(message)s',
            handlers=handlers
        )
        self._logger.setLevel(logging.DEBUG)

    def echo(self) -> str:
        return self._logger.info(self._text)
