from hello_world.io.echo import Echo


def test_echo():
    expected = "hello world"
    a = Echo(expected)
    assert a.echo() == expected