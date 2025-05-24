from src.base import GameObject
from src.constants import (
    CHARACTER_SELECTION_SCREEN_NAME,
    EXTRA_DATA_SCREEN_NAME,
    MAIN_MENU_SCREEN_NAME,
)
from src.display import Display
from src.interactions import Interaction
from src.notifications import Notification, NotificationSink, NotificationType
from src.screens.base import GameScreen
from src.screens.character_selection import CharacterSelectionScreen
from src.screens.main_menu import MainMenuScreen


class ScreenManager(GameObject):
    def __init__(self, notification_sink: NotificationSink) -> None:
        super().__init__(notification_sink)

        self._game_screen: GameScreen = MainMenuScreen(self._notification_sink)

    def _change_screen(self, screen_name: str) -> None:
        if screen_name == MAIN_MENU_SCREEN_NAME:
            self._game_screen = MainMenuScreen(self._notification_sink)
        elif screen_name == CHARACTER_SELECTION_SCREEN_NAME:
            self._game_screen = CharacterSelectionScreen(self._notification_sink)

    def draw(self, display: Display) -> None:
        self._game_screen.draw(display)

    def handle_interaction(self, interaction: Interaction) -> None:
        self._game_screen.handle_interaction(interaction)

    def update(self, delta: float) -> None:
        self._game_screen.update(delta)

    def handle_notification(self, notification: Notification) -> None:
        if notification.type == NotificationType.CHANGE_SCREEN:
            self._change_screen(notification.extra_data[EXTRA_DATA_SCREEN_NAME])
        else:
            self._game_screen.handle_notification(notification)
