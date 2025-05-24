from typing import Tuple

import pygame


def load_image(file_path: str, has_transparency: bool = True) -> pygame.Surface:
    surface = pygame.image.load(file_path)

    if has_transparency:
        return surface.convert_alpha()
    return surface


def load_sprite(
    file_path: str,
    top_left_coord: Tuple[int, int],
    has_transparency: bool = True,
) -> pygame.sprite.Sprite:
    sprite = pygame.sprite.Sprite()

    sprite.image = load_image(
        file_path=file_path,
        has_transparency=has_transparency,
    )
    sprite.rect = sprite.image.get_rect(topleft=top_left_coord)

    return sprite
