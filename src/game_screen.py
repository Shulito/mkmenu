from abc import ABC, abstractmethod
from os import path

import pygame.sprite

from src.assets import load_image
from src.constants import (
    BLINK_SPEED,
    MAIN_MENU_BACKGROUND_TOP_LEFT_COORD,
    MAIN_MENU_BLINK_TOP_LEFT_COORD,
    MAIN_MENU_FOLDER_PATH,
)
from src.display import Display
from src.interactions import Interaction
from src.interfaces import GameObject


class GameScreen(GameObject, ABC):
    @abstractmethod
    def next_game_screen(self) -> "GameScreen":
        pass


class MainMenuScreen(GameScreen):
    def __init__(self) -> None:
        self._background_sprite = pygame.sprite.Sprite()
        self._background_sprite.image = load_image(
            file_path=path.join(MAIN_MENU_FOLDER_PATH, "background.png"),
            has_transparency=False,
        )
        self._background_sprite.rect = self._background_sprite.image.get_rect(
            topleft=MAIN_MENU_BACKGROUND_TOP_LEFT_COORD
        )

        self._blink_sprite = pygame.sprite.Sprite()
        self._blink_sprite.image = load_image(
            file_path=path.join(MAIN_MENU_FOLDER_PATH, "blink.png"),
            has_transparency=True,
        )
        self._blink_sprite.rect = self._blink_sprite.image.get_rect(
            topleft=MAIN_MENU_BLINK_TOP_LEFT_COORD
        )

        self._blink_direction = -1
        self._blink_percentage = 1.0

    def handle_interaction(self, interaction: Interaction) -> None:
        pass

    def update(self, delta_ms: float) -> None:
        self._blink_percentage += BLINK_SPEED * self._blink_direction * delta_ms

        if self._blink_percentage < 0.0:
            self._blink_percentage = 0.0
            self._blink_direction = 1
        elif self._blink_percentage > 1.0:
            self._blink_percentage = 1.0
            self._blink_direction = -1

        self._blink_sprite.image.set_alpha(  # type: ignore
            int(pygame.math.lerp(0, 255, self._blink_percentage))
        )

    def draw(self, display: Display) -> None:
        display.draw(self._background_sprite)
        display.draw(self._blink_sprite)

    def next_game_screen(self) -> GameScreen:
        return self


class CharacterSelectionScreen(GameScreen):
    def handle_interaction(self, interaction: Interaction) -> None:
        pass

    def update(self, delta_ms: float) -> None:
        pass

    def draw(self, display: Display) -> None:
        pass

    def next_game_screen(self) -> GameScreen:
        return self
