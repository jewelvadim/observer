from typing import List

from abstract import Subject, Observer


class Doorbell(Subject):
    _apartments: List[Observer]
    _ring: int

    def __init__(self) -> None:
        super().__init__()

        self._apartments = []

    def _notify(self) -> None:
        for apartment in self._apartments:
            apartment.react(self._ring)

    def attach(self, observer: Observer) -> None:
        self._apartments.append(observer)

    def detach(self, observer: Observer) -> None:
        self._apartments.remove(observer)

    def ring(self, apartment_number: int) -> None:
        self._ring = apartment_number

        self._notify()


class Apartment(Observer):
    _apartment_number: int

    def __init__(self, apartment_number) -> None:
        super().__init__()

        self._apartment_number = apartment_number

    def react(self, apartment_number: int) -> None:

        if self._apartment_number == apartment_number:
            print(f'{self._apartment_number}: Welcome')

        else:
            print(f'{self._apartment_number}: Not me!')
