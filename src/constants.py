from os import path
from typing import Final, List, Tuple

# General constants
GAME_TITLE: Final[str] = "MK1 Menu"
FPS: Final[int] = 60

# Display constants
SUPPORTED_RESOLUTIONS: Final[List[Tuple[int, int]]] = [
    (416, 270),
    (832, 540),
    (1664, 1080),
]

INITIAL_DISPLAY_SIZE_INDEX: Final[int] = 1
DISPLAY_BACKGROUND_COLOR: Final[Tuple[int, int, int]] = (0, 0, 0)

INTERNAL_SCREEN_SIZE: Final[Tuple[int, int]] = SUPPORTED_RESOLUTIONS[0]

SDL_VIDEO_CENTERED_ENV_VAR: Final[str] = "SDL_VIDEO_CENTERED"
SDL_VIDEO_CENTERED_TRUE: Final[str] = "1"

# Main Menu constants
MAIN_MENU_BACKGROUND_TOP_LEFT_COORD: Final[Tuple[int, int]] = (0, 0)
MAIN_MENU_BLINK_TOP_LEFT_COORD: Final[Tuple[int, int]] = (159, 225)

BLINK_SPEED: Final[int] = 3

# Character Selection constants
CHARACTER_SELECTION_BACKGROUND_TOP_LEFT_COORD: Final[Tuple[int, int]] = (0, 0)

# Content constants
ASSETS_FOLDER_PATH: Final[str] = path.abspath(
    path.join(path.dirname(__file__), "..", "assets")
)
MAIN_MENU_FOLDER_PATH: Final[str] = path.join(ASSETS_FOLDER_PATH, "main_menu")
CHARACTER_SELECTION_FOLDER_PATH: Final[str] = path.join(
    ASSETS_FOLDER_PATH, "character_selection"
)
