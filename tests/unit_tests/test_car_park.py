import pytest

from hello_world.car_park import CarPark
from hello_world.exception.NoneActionable import NoneActionable


def create_car_park_client(capacity: int):
    return CarPark(capacity)


def test_car_park_action_park():
    data = [('PARK', 1011), ('PARK', 1111)]
    expected = [('PARK', 1011), ('PARK', 1111)]
    client = create_car_park_client(4)
    client.doActions(data)
    actuals = client.all_slots()
    assert actuals == expected


def test_car_park_action_park_full():
    actions = [('PARK', 1011), ('PARK', 1211), ('PARK', 1911), ('PARK', 1101)]
    expected = [('PARK', 1011), ('PARK', 1211), ('PARK', 1911)]
    client = create_car_park_client(3)
    client.doActions(actions)
    actuals = client.all_slots()
    assert actuals == expected


def test_car_park_none_actionable():
    client = create_car_park_client(3)
    with pytest.raises(NoneActionable):
        client.doActions([])


def test_depart():
    client = create_car_park_client(3)
    actions = [('PARK', 1011), ('PARK', 1211), ('PARK', 1911), ('PARK', 1101), ('DEPART')]
    client.doActions(actions)
    assert client.doActions(actions) == None
