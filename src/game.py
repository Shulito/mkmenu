import pygame

from src.constants import FPS
from src.display import Display
from src.game_screen import GameScreen, MainMenuScreen
from src.interactions import Action, get_interactions


class Game:
    def __init__(self) -> None:
        pygame.init()

        self._clock: pygame.time.Clock = pygame.time.Clock()

        self._display: Display = Display()
        self._game_screen: GameScreen = MainMenuScreen()

    def __del__(self) -> None:
        pygame.quit()

    def run(self) -> None:
        running = True

        while running:
            delta_ms = self._clock.tick(FPS) / 1000

            for interaction in get_interactions():
                if interaction.action == Action.QUIT:
                    running = False
                    break

                self._display.handle_interaction(interaction)
                self._game_screen.handle_interaction(interaction)

            if not running:
                break

            self._game_screen = self._game_screen.next_game_screen()
            self._game_screen.update(delta_ms)
            self._game_screen.draw(self._display)
            self._display.update()
