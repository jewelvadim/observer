from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def react(self, *args, **kwargs) -> None:
        pass


class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def _notify(self) -> None:
        pass
