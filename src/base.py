from abc import ABC, abstractmethod

from src.display import Display
from src.interactions import Interaction
from src.notifications import Notification, NotificationSink


class GameObject(ABC):
    def __init__(self, notification_sink: NotificationSink) -> None:
        self._notification_sink = notification_sink

    @abstractmethod
    def draw(self, display: Display) -> None:
        pass

    @abstractmethod
    def handle_interaction(self, interaction: Interaction) -> None:
        pass

    @abstractmethod
    def update(self, delta_ms: float) -> None:
        pass

    @abstractmethod
    def handle_notification(self, notification: Notification) -> None:
        pass
