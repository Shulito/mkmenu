from os import path

from src.constants import CHARACTER_SELECTION_FOLDER_PATH
from src.display import Display
from src.interactions import Interaction
from src.notifications import Notification, NotificationSink
from src.screens.base import GameScreen


class CharacterSelectionScreen(GameScreen):
    def __init__(self, notification_sink: NotificationSink) -> None:
        super().__init__(
            notification_sink=notification_sink,
            background_sprite_file_path=path.join(
                CHARACTER_SELECTION_FOLDER_PATH, "background.png"
            ),
        )

    def handle_interaction(self, interaction: Interaction) -> None:
        return

    def update(self, delta_ms: float) -> None:
        return

    def draw(self, display: Display) -> None:
        super().draw(display)

    def handle_notification(self, notification: Notification) -> None:
        return
