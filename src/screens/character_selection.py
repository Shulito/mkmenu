from os import path

from src.constants import CHARACTER_SELECTION_FOLDER_PATH, CHARACTER_SELECTION_PORTRAITS
from src.display import Display
from src.interactions import Interaction
from src.notifications import Notification, NotificationSink
from src.screens.base import GameScreen
from src.screens.portrait import CharacterPortrait


class CharacterSelectionScreen(GameScreen):
    def __init__(self, notification_sink: NotificationSink) -> None:
        super().__init__(
            notification_sink=notification_sink,
            background_sprite_file_path=path.join(
                CHARACTER_SELECTION_FOLDER_PATH, "background.png"
            ),
        )

        self._portraits = [
            CharacterPortrait(
                notification_sink=notification_sink,
                file_path=path.join(
                    CHARACTER_SELECTION_FOLDER_PATH, character_name, "portrait.png"
                ),
                top_left_coord=(top_left_x, top_left_y),
            )
            for top_left_x, top_left_y, character_name in CHARACTER_SELECTION_PORTRAITS
        ]

    def handle_interaction(self, interaction: Interaction) -> None:
        return

    def update(self, delta_ms: float) -> None:
        return

    def draw(self, display: Display) -> None:
        super().draw(display)

        for portrait in self._portraits:
            portrait.draw(display)

    def handle_notification(self, notification: Notification) -> None:
        return
