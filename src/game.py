import pygame

from src.constants import FPS
from src.display import Display
from src.interactions import Action, get_interactions
from src.notifications import NotificationSink
from src.screens import ScreenManager


class Game:
    def __init__(self) -> None:
        pygame.init()

        self._clock = pygame.time.Clock()

        self._display = Display()
        self._notification_sink = NotificationSink()
        self._screen_manager = ScreenManager(self._notification_sink)

    def __del__(self) -> None:
        pygame.quit()

    def run(self) -> None:
        running = True

        while running:
            delta = self._clock.tick(FPS) / 1000

            for interaction in get_interactions():
                if interaction.action == Action.QUIT:
                    running = False
                    break

                self._display.handle_interaction(interaction)
                self._screen_manager.handle_interaction(interaction)

            if not running:
                break

            for notification in self._notification_sink.read_all():
                self._screen_manager.handle_notification(notification)

            self._screen_manager.update(delta)
            self._screen_manager.draw(self._display)
            self._display.update()
