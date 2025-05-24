from os import path
from typing import Final, List, Tuple

# General constants
GAME_TITLE: Final[str] = "MK1 Menu"
FPS: Final[int] = 60

BACKGROUND_TOP_LEFT_COORD: Final[Tuple[int, int]] = (0, 0)

ALPHA_MIN_VALUE: Final[int] = 0
ALPHA_MAX_VALUE: Final[int] = 255

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

# Screen constants
MAIN_MENU_SCREEN_NAME: Final[str] = "MAIN_MENU"
CHARACTER_SELECTION_SCREEN_NAME: Final[str] = "CHARACTER_SELECTION"

# Main Menu constants
MAIN_MENU_BLINK_TOP_LEFT_COORD: Final[Tuple[int, int]] = (159, 225)
BLINK_SPEED: Final[int] = 3

# Character Selection constants
CHARACTER_SELECTION_PORTRAITS: Final[List[Tuple[int, int, str]]] = [
    (42, 54, "johnny"),
    (109, 54, "kano"),
    (109, 136, "raiden"),
    (176, 136, "liukang"),
    (243, 136, "scorpion"),
    (243, 54, "subzero"),
    (310, 54, "sonya"),
]

PORTRAIT_ANIMATION_SPEED: Final[float] = 1.5

# Notification constants
EXTRA_DATA_SCREEN_NAME: Final[str] = "SCREEN_NAME"

# Content constants
ASSETS_FOLDER_PATH: Final[str] = path.abspath(
    path.join(path.dirname(__file__), "..", "assets")
)
MAIN_MENU_FOLDER_PATH: Final[str] = path.join(ASSETS_FOLDER_PATH, "main_menu")
CHARACTER_SELECTION_FOLDER_PATH: Final[str] = path.join(
    ASSETS_FOLDER_PATH, "character_selection"
)
