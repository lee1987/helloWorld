from hello_world.exception.CarParkFullException import CarParkFullException
from hello_world.exception.NoneActionable import NoneActionable


class CarPark(object):
    def __init__(self, capacity: int):
        self._slots = []
        self._capacity = capacity
        self._latest_depart = ()

    def doActions(self, actions: list = None) -> tuple:
        """
        given a list of actions to act

        :param actions:
        :return: last action
        :raise NoneActionable if None action given
        """
        if not actions:
            raise NoneActionable

        for action in actions:
            if action == 'SMALLEST':
                return ''
            elif action == ('DEPART'):
                self.depart(action)
            elif type(action) is tuple and action[0] == 'PARK':
                try:
                    self.park(action)
                except CarParkFullException:
                    pass

        return actions.pop()

    def park(self, car: tuple):
        """
        Park the car

        :param car:
        :raises: CarParkFullException
        """
        if self._capacity != len(self._slots):
            self._slots.append(car)
        else:
            raise CarParkFullException

    def depart(self, car: tuple):
        """
        Car depart

        :param car:
        :return:
        """
        self._latest_depart = car
        self._slots.remove(car)

    def in_car_park(self, car: tuple) -> bool:
        return car in self._slots

    def all_slots(self):
        return self._slots
