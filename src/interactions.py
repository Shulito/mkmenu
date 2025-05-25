from dataclasses import dataclass
from enum import Enum
from typing import Dict, Final, Set

import pygame


class Action(Enum):
    QUIT = 0
    INCREASE_DISPLAY_SIZE = 1
    DECREASE_DISPLAY_SIZE = 2
    MENU_ACCEPT = 3
    MENU_LEFT = 4
    MENU_RIGHT = 5


@dataclass(frozen=True)
class Interaction:
    action: Action
    being_pressed: bool = False
    just_pressed: bool = False
    just_released: bool = False


EVENT_TO_ACTION_MAPPING: Final[Dict[int, Action]] = {
    pygame.QUIT: Action.QUIT,
}

KEY_TO_ACTION_MAPPING: Final[Dict[int, Action]] = {
    pygame.K_ESCAPE: Action.QUIT,
    pygame.K_PLUS: Action.INCREASE_DISPLAY_SIZE,
    pygame.K_KP_PLUS: Action.INCREASE_DISPLAY_SIZE,
    pygame.K_MINUS: Action.DECREASE_DISPLAY_SIZE,
    pygame.K_KP_MINUS: Action.DECREASE_DISPLAY_SIZE,
    pygame.K_RETURN: Action.MENU_ACCEPT,
    pygame.K_KP_ENTER: Action.MENU_ACCEPT,
    pygame.K_RIGHT: Action.MENU_RIGHT,
    pygame.K_d: Action.MENU_RIGHT,
    pygame.K_LEFT: Action.MENU_LEFT,
    pygame.K_a: Action.MENU_LEFT,
}


def get_interactions() -> Set[Interaction]:
    interactions = set()

    for event in pygame.event.get():
        if event.type in EVENT_TO_ACTION_MAPPING:
            interactions.add(Interaction(action=EVENT_TO_ACTION_MAPPING[event.type]))

    keys_being_pressed = pygame.key.get_pressed()
    keys_just_pressed = pygame.key.get_just_pressed()
    keys_just_released = pygame.key.get_just_released()

    for key in KEY_TO_ACTION_MAPPING.keys():
        if keys_being_pressed[key]:
            interactions.add(
                Interaction(
                    action=KEY_TO_ACTION_MAPPING[key],
                    being_pressed=True,
                )
            )
        if keys_just_pressed[key]:
            interactions.add(
                Interaction(
                    action=KEY_TO_ACTION_MAPPING[key],
                    just_pressed=True,
                )
            )
        if keys_just_released[key]:
            interactions.add(
                Interaction(
                    action=KEY_TO_ACTION_MAPPING[key],
                    just_released=True,
                )
            )

    return interactions
