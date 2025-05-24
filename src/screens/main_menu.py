from os import path

import pygame

from src.assets import load_sprite
from src.constants import (
    ALPHA_MAX_VALUE,
    ALPHA_MIN_VALUE,
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

        self._blink_sprite = load_sprite(
            file_path=path.join(MAIN_MENU_FOLDER_PATH, "blink.png"),
            top_left_coord=MAIN_MENU_BLINK_TOP_LEFT_COORD,
        )

        self._blink_direction = -1
        self._blink_percentage = 1.0

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

    def update(self, delta_ms: float) -> None:
        self._blink_percentage += BLINK_SPEED * self._blink_direction * delta_ms

        if self._blink_percentage <= 0.0:
            self._blink_percentage = 0.0
            self._blink_direction = 1
        elif self._blink_percentage >= 1.0:
            self._blink_percentage = 1.0
            self._blink_direction = -1

        self._blink_sprite.image.set_alpha(  # type: ignore
            int(
                pygame.math.lerp(
                    ALPHA_MIN_VALUE, ALPHA_MAX_VALUE, self._blink_percentage
                )
            )
        )

    def draw(self, display: Display) -> None:
        super().draw(display)
        display.draw(self._blink_sprite)

    def handle_notification(self, notification: Notification) -> None:
        return
