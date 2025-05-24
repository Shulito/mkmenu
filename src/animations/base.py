from abc import ABC, abstractmethod

from pygame import FRect, Rect

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
    def rect(self) -> FRect | Rect | None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass
