from os import path

from src.animations import AlphaAnimation
from src.assets import load_sprite
from src.constants import (
    BLINK_SPEED,
    CHARACTER_SELECTION_SCREEN_NAME,
    EXTRA_DATA_SCREEN_NAME,
    MAIN_MENU_BLINK_TOP_LEFT_COORD,
    MAIN_MENU_FOLDER_PATH,
)
from src.display import Display
from src.interactions import Action, Interaction
from src.notifications import Notification, NotificationSink, NotificationType
from src.screens.base import GameScreen


class MainMenuScreen(GameScreen):
    def __init__(self, notification_sink: NotificationSink) -> None:
        super().__init__(
            notification_sink=notification_sink,
            background_sprite_file_path=path.join(
                MAIN_MENU_FOLDER_PATH, "background.png"
            ),
        )

        self._blink_animation = AlphaAnimation(
            sprite=load_sprite(
                file_path=path.join(MAIN_MENU_FOLDER_PATH, "blink.png"),
                top_left_coord=MAIN_MENU_BLINK_TOP_LEFT_COORD,
            ),
            speed=BLINK_SPEED,
        )
        self._blink_animation.running = True

    def handle_interaction(self, interaction: Interaction) -> None:
        if interaction.action == Action.MENU_ACCEPT and interaction.just_pressed:
            self._notification_sink.write(
                Notification(
                    type=NotificationType.CHANGE_SCREEN,
                    extra_data={
                        EXTRA_DATA_SCREEN_NAME: CHARACTER_SELECTION_SCREEN_NAME
                    },
                )
            )

    def update(self, delta: float) -> None:
        self._blink_animation.update(delta)

    def draw(self, display: Display) -> None:
        super().draw(display)
        self._blink_animation.draw(display)

    def handle_notification(self, notification: Notification) -> None:
        return
