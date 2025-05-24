from typing import Tuple

from src.assets import load_sprite
from src.base import GameObject
from src.display import Display
from src.interactions import Interaction
from src.notifications import Notification, NotificationSink


class CharacterPortrait(GameObject):
    def __init__(
        self,
        notification_sink: NotificationSink,
        file_path: str,
        top_left_coord: Tuple[int, int],
    ) -> None:
        super().__init__(notification_sink)

        self._portrait_sprite = load_sprite(
            file_path=file_path, top_left_coord=top_left_coord, has_transparency=False
        )

    def draw(self, display: Display) -> None:
        display.draw(self._portrait_sprite)

    def handle_interaction(self, interaction: Interaction) -> None:
        return

    def update(self, delta_ms: float) -> None:
        return

    def handle_notification(self, notification: Notification) -> None:
        return
