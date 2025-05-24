import pygame


def load_image(file_path: str, has_transparency: bool = True) -> pygame.Surface:
    surface = pygame.image.load(file_path)

    if has_transparency:
        return surface.convert_alpha()
    return surface
