from typing import List, Tuple

import pygame.sprite
from pygame import FRect, Rect

from src.animations.base import Animation
from src.assets import load_image
from src.display import Display


class SpritesheetAnimation(Animation):
    def __init__(
        self,
        file_path: str,
        total_frames: int,
        fps: int,
        coord: Tuple[int, int] = (0, 0),
        has_transparency: bool = True,
    ) -> None:
        super().__init__()

        if total_frames <= 0:
            raise ValueError(f"total_frames has to be positive integer")
        if fps <= 0:
            raise ValueError(f"fps has to be positive integer")

        sprite_sheet = load_image(
            file_path=file_path, has_transparency=has_transparency
        )

        frame_width: int = sprite_sheet.width // total_frames
        self._images: List[pygame.Surface] = []

        for index in range(total_frames):
            self._images.append(
                sprite_sheet.subsurface(
                    pygame.Rect(
                        index * frame_width, 0, frame_width, sprite_sheet.height
                    )
                )
            )

        self._current_frame = 0
        self._deltas_per_frame = 1 / fps
        self._accumulated_deltas = 0.0

        self._sprite = pygame.sprite.Sprite()
        self._sprite.image = self._images[self._current_frame]
        self._sprite.rect = self._sprite.image.get_rect(topleft=coord)

    @property
    def rect(self) -> FRect | Rect | None:
        return self._sprite.rect

    def reset(self) -> None:
        self._current_frame = 0
        self._accumulated_deltas = 0.0
        self._sprite.image = self._images[self._current_frame]

    def draw(self, display: Display) -> None:
        display.draw(self._sprite)

    def update(self, delta: float) -> None:
        self._accumulated_deltas += delta

        if self._accumulated_deltas >= self._deltas_per_frame:
            self._current_frame = (self._current_frame + 1) % len(self._images)
            self._sprite.image = self._images[self._current_frame]
            self._accumulated_deltas = 0.0
