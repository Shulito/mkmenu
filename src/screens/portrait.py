from typing import Tuple

from pygame import FRect, Rect

from src.animations import AlphaAnimation
from src.assets import load_sprite
from src.base import GameObject
from src.constants import PORTRAIT_ANIMATION_SPEED
from src.display import Display
from src.interactions import Interaction
from src.notifications import Notification, NotificationSink


class CharacterPortrait(GameObject):
    def __init__(
        self,
        notification_sink: NotificationSink,
        file_path: str,
        top_left_coord: Tuple[int, int],
    ) -> None:
        super().__init__(notification_sink)

        self._portrait_animation = AlphaAnimation(
            sprite=load_sprite(
                file_path=file_path,
                top_left_coord=top_left_coord,
                has_transparency=False,
            ),
            speed=PORTRAIT_ANIMATION_SPEED,
        )

    @property
    def rect(self) -> FRect | Rect | None:
        return self._portrait_animation.rect

    def select(self) -> None:
        self._portrait_animation.running = True

    def deselect(self) -> None:
        self._portrait_animation.running = False
        self._portrait_animation.reset()

    def draw(self, display: Display) -> None:
        self._portrait_animation.draw(display)

    def handle_interaction(self, interaction: Interaction) -> None:
        return

    def update(self, delta: float) -> None:
        self._portrait_animation.update(delta)

    def handle_notification(self, notification: Notification) -> None:
        return
