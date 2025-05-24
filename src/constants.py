from dataclasses import dataclass
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
@dataclass(frozen=True)
class CharacterData:
    folder_name: str
    portrait_top_left_coord: Tuple[int, int]
    idle_total_frames: int


CHARACTER_SELECTION_PORTRAITS: Final[List[CharacterData]] = [
    CharacterData("johnny", (42, 54), 7),
    CharacterData("kano", (109, 54), 7),
    CharacterData("raiden", (109, 136), 10),
    CharacterData("liukang", (176, 136), 8),
    CharacterData("scorpion", (243, 136), 7),
    CharacterData("subzero", (243, 54), 12),
    CharacterData("sonya", (310, 54), 7),
]

PORTRAIT_ANIMATION_SPEED: Final[float] = 1.5

BOX_ANIMATION_TOTAL_FRAMES: Final[int] = 2
BOX_ANIMATION_FPS: Final[int] = 10

IDLE_ANIMATION_BOTTOM_LEFT_COORD: Final[Tuple[int, int]] = (-30, 70)
IDLE_ANIMATION_FPS: Final[int] = 10

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
