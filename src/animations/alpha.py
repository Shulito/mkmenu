import pygame.sprite

from src.animations.base import Animation
from src.constants import ALPHA_MAX_VALUE, ALPHA_MIN_VALUE
from src.display import Display


class AlphaAnimation(Animation):
    def __init__(self, sprite: pygame.sprite.Sprite, speed: float) -> None:
        super().__init__()

        self._sprite = sprite
        self._speed = speed

        self._alpha_direction = -1
        self._alpha_percentage = 1.0

    def draw(self, display: Display) -> None:
        display.draw(self._sprite)

    def update(self, delta: float) -> None:
        if not self.running:
            return

        self._alpha_percentage += self._speed * self._alpha_direction * delta

        if self._alpha_percentage <= 0.0:
            self._alpha_percentage = 0.0
            self._alpha_direction = 1
        elif self._alpha_percentage >= 1.0:
            self._alpha_percentage = 1.0
            self._alpha_direction = -1

        self._sprite.image.set_alpha(  # type: ignore
            int(
                pygame.math.lerp(
                    ALPHA_MIN_VALUE, ALPHA_MAX_VALUE, self._alpha_percentage
                )
            )
        )

    def reset(self) -> None:
        self._alpha_direction = -1
        self._alpha_percentage = 1.0
        self._sprite.image.set_alpha(ALPHA_MAX_VALUE)  # type: ignore
