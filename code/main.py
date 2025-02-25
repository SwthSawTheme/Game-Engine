from settings import *
from level import *
from pytmx.util_pygame import load_pygame

class Game:

    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption("Pirate World")

        self.tmx_maps = {0: load_pygame(r"../data/levels/omni.tmx")}
        self.current_stage = Level(self.tmx_maps[0])

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.current_stage.run()
            pygame.display.update()


if __name__ == "__main__":
    game  = Game()
    game.run()