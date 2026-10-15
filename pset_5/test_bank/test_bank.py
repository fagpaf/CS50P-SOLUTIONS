from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0


def test_init_h():
    assert value("HEY!") == 20
    assert value("Hi") == 20


def test_not_h():
    assert value("What's") == 100
