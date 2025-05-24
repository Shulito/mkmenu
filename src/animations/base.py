from abc import ABC, abstractmethod
from typing import Tuple

from src.base import Drawable, Updatable


class Animation(Drawable, Updatable, ABC):
    def __init__(self) -> None:
        self._running = False

    @property
    def running(self) -> bool:
        return self._running

    @running.setter
    def running(self, value: bool) -> None:
        self._running = value

    @property
    @abstractmethod
    def center(self) -> Tuple[int, int]:
        pass

    @center.setter
    @abstractmethod
    def center(self, value: Tuple[int, int]) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass
