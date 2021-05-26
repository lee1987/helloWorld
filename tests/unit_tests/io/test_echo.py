from hello_world.io.echo import Echo


def test_echo(caplog):
    expected = "hello world"
    a = Echo(expected)
    a.echo()
    actual = caplog.records
    assert len(actual) == 1

    assert actual[0].message == expected