import os

import pygame

from src.constants import (
    DISPLAY_BACKGROUND_COLOR,
    GAME_TITLE,
    INITIAL_DISPLAY_SIZE_INDEX,
    INTERNAL_SCREEN_SIZE,
    SDL_VIDEO_CENTERED_ENV_VAR,
    SDL_VIDEO_CENTERED_TRUE,
    SUPPORTED_RESOLUTIONS,
)
from src.interactions import Action, Interaction


class Display:
    def __init__(self) -> None:
        pygame.display.set_caption(GAME_TITLE)
        os.environ[SDL_VIDEO_CENTERED_ENV_VAR] = SDL_VIDEO_CENTERED_TRUE

        self._display_size_idx = INITIAL_DISPLAY_SIZE_INDEX
        self._screen = pygame.Surface(INTERNAL_SCREEN_SIZE)
        self._change_display()

    def _change_display(self) -> None:
        self._display = pygame.display.set_mode(
            SUPPORTED_RESOLUTIONS[self._display_size_idx]
        )

    def handle_interaction(self, interaction: Interaction) -> None:
        if (
            interaction.action == Action.INCREASE_DISPLAY_SIZE
            and interaction.just_pressed
            and self._display_size_idx < len(SUPPORTED_RESOLUTIONS) - 1
        ):
            self._display_size_idx += 1
            self._change_display()
        elif (
            interaction.action == Action.DECREASE_DISPLAY_SIZE
            and interaction.just_pressed
            and self._display_size_idx > 0
        ):
            self._display_size_idx -= 1
            self._change_display()

    def update(self) -> None:
        self._display.fill(DISPLAY_BACKGROUND_COLOR)
        pygame.transform.scale(
            self._screen, SUPPORTED_RESOLUTIONS[self._display_size_idx], self._display
        )
        pygame.display.flip()

    def draw(self, sprite: pygame.sprite.Sprite) -> None:
        self._screen.blit(sprite.image, sprite.rect)  # type: ignore
