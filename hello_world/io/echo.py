class Echo(object):
    """
    echo stm
    """

    def __init__(self, text: str):
        self._text = text

    def echo(self) -> str:
        return self._text
