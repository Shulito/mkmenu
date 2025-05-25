from dataclasses import dataclass
from os import path
from typing import List

from src.animations import SpritesheetAnimation
from src.constants import (
    BOX_ANIMATION_FPS,
    BOX_ANIMATION_TOTAL_FRAMES,
    CHARACTER_SELECTION_FOLDER_PATH,
    CHARACTER_SELECTION_PORTRAITS,
    IDLE_ANIMATION_BOTTOM_LEFT_COORD,
    IDLE_ANIMATION_FPS,
)
from src.display import Display
from src.interactions import Action, Interaction
from src.notifications import Notification, NotificationSink
from src.screens.base import GameScreen
from src.screens.portrait import CharacterPortrait


@dataclass(frozen=True)
class PortraitAndIdle:
    portrait: CharacterPortrait
    idle_animation: SpritesheetAnimation


class CharacterSelectionScreen(GameScreen):
    def __init__(self, notification_sink: NotificationSink) -> None:
        super().__init__(
            notification_sink=notification_sink,
            background_sprite_file_path=path.join(
                CHARACTER_SELECTION_FOLDER_PATH, "background.png"
            ),
        )

        self._characters: List[PortraitAndIdle] = [
            PortraitAndIdle(
                CharacterPortrait(
                    notification_sink=notification_sink,
                    file_path=path.join(
                        CHARACTER_SELECTION_FOLDER_PATH,
                        character_data.folder_name,
                        "portrait.png",
                    ),
                    top_left_coord=character_data.portrait_top_left_coord,
                ),
                SpritesheetAnimation(
                    file_path=path.join(
                        CHARACTER_SELECTION_FOLDER_PATH,
                        character_data.folder_name,
                        "idle.png",
                    ),
                    total_frames=character_data.idle_total_frames,
                    fps=IDLE_ANIMATION_FPS,
                    coord=IDLE_ANIMATION_BOTTOM_LEFT_COORD,
                ),
            )
            for character_data in CHARACTER_SELECTION_PORTRAITS
        ]

        self._selection_box = SpritesheetAnimation(
            file_path=path.join(CHARACTER_SELECTION_FOLDER_PATH, "box.png"),
            total_frames=BOX_ANIMATION_TOTAL_FRAMES,
            fps=BOX_ANIMATION_FPS,
        )
        self._selection_box.running = True

        self._selected_character_idx = 0

        character = self._characters[self._selected_character_idx]
        character.portrait.select()
        character.idle_animation.running = True

        self._selection_box.rect.center = character.portrait.rect.center  # type: ignore

    def _move_selected_character(self, value: int) -> None:
        character = self._characters[self._selected_character_idx]
        character.portrait.deselect()
        character.idle_animation.running = False
        character.idle_animation.reset()

        self._selected_character_idx = (self._selected_character_idx + value) % len(
            self._characters
        )

        character = self._characters[self._selected_character_idx]
        character.portrait.select()
        character.idle_animation.running = True

        self._selection_box.rect.center = character.portrait.rect.center  # type: ignore

    def handle_interaction(self, interaction: Interaction) -> None:
        if interaction.action == Action.MENU_RIGHT and interaction.just_pressed:
            self._move_selected_character(1)
        elif interaction.action == Action.MENU_LEFT and interaction.just_pressed:
            self._move_selected_character(-1)

    def update(self, delta: float) -> None:
        character = self._characters[self._selected_character_idx]
        character.portrait.update(delta)
        character.idle_animation.update(delta)

        self._selection_box.update(delta)

    def draw(self, display: Display) -> None:
        super().draw(display)

        for character in self._characters:
            character.portrait.draw(display)

        self._selection_box.draw(display)
        self._characters[self._selected_character_idx].idle_animation.draw(display)

    def handle_notification(self, notification: Notification) -> None:
        return
