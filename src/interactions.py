from dataclasses import dataclass
from enum import Enum
from typing import Dict, Final, Set

import pygame
from pygame.key import ScancodeWrapper


class Action(Enum):
    QUIT = 0
    INCREASE_DISPLAY_SIZE = 1
    DECREASE_DISPLAY_SIZE = 2
    MENU_ACCEPT = 3


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
}


def _add_interactions(
    interactions: Set[Interaction],
    keys: ScancodeWrapper,
    being_pressed: bool = False,
    just_pressed: bool = False,
    just_released: bool = False,
) -> None:
    for key in KEY_TO_ACTION_MAPPING.keys():
        if keys[key]:
            interactions.add(
                Interaction(
                    action=KEY_TO_ACTION_MAPPING[key],
                    being_pressed=being_pressed,
                    just_pressed=just_pressed,
                    just_released=just_released,
                )
            )


def get_interactions() -> Set[Interaction]:
    interactions = set()

    for event in pygame.event.get():
        if event.type in EVENT_TO_ACTION_MAPPING:
            interactions.add(Interaction(action=EVENT_TO_ACTION_MAPPING[event.type]))

    _add_interactions(
        interactions=interactions,
        keys=pygame.key.get_pressed(),
        being_pressed=True,
    )

    _add_interactions(
        interactions=interactions,
        keys=pygame.key.get_just_pressed(),
        just_pressed=True,
    )

    _add_interactions(
        interactions=interactions,
        keys=pygame.key.get_just_released(),
        just_released=True,
    )

    return interactions
