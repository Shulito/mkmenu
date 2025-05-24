from os import path

from src.constants import CHARACTER_SELECTION_FOLDER_PATH, CHARACTER_SELECTION_PORTRAITS
from src.display import Display
from src.interactions import Action, Interaction
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

        self._selected_character_idx = 0
        self._portraits[self._selected_character_idx].select()

    def _move_selected_character(self, value: int) -> None:
        self._portraits[self._selected_character_idx].deselect()
        self._selected_character_idx = (self._selected_character_idx + value) % len(
            self._portraits
        )
        self._portraits[self._selected_character_idx].select()

    def handle_interaction(self, interaction: Interaction) -> None:
        if interaction.action == Action.MENU_RIGHT and interaction.just_pressed:
            self._move_selected_character(1)
        elif interaction.action == Action.MENU_LEFT and interaction.just_pressed:
            self._move_selected_character(-1)

    def update(self, delta_ms: float) -> None:
        self._portraits[self._selected_character_idx].update(delta_ms)

    def draw(self, display: Display) -> None:
        super().draw(display)

        for portrait in self._portraits:
            portrait.draw(display)

    def handle_notification(self, notification: Notification) -> None:
        return
