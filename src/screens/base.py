from abc import ABC

from src.assets import load_sprite
from src.base import GameObject
from src.constants import (
    BACKGROUND_TOP_LEFT_COORD,
)
from src.display import Display
from src.notifications import NotificationSink


class GameScreen(GameObject, ABC):
    def __init__(
        self,
        notification_sink: NotificationSink,
        background_sprite_file_path: str,
    ) -> None:
        super().__init__(notification_sink)

        self._background_sprite = load_sprite(
            file_path=background_sprite_file_path,
            top_left_coord=BACKGROUND_TOP_LEFT_COORD,
        )

    def draw(self, display: Display) -> None:
        display.draw(self._background_sprite)
