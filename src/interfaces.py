from abc import ABC, abstractmethod

from src.display import Display
from src.interactions import Interaction


class Drawable(ABC):
    @abstractmethod
    def draw(self, display: Display) -> None:
        pass


class Interactable(ABC):
    @abstractmethod
    def handle_interaction(self, interaction: Interaction) -> None:
        pass


class Updatable(ABC):
    @abstractmethod
    def update(self, delta_ms: float) -> None:
        pass


class GameObject(Drawable, Interactable, Updatable, ABC):
    pass
