import pygame
from timeit import timeit as time
from pygame.locals import *


class Window:

    def __init__(self, resolution, fullscreen, window_title, window_icon_location=None):

        # Geometry
        self.resolution = resolution
        self.fullscreen = fullscreen

        # Window
        self.window_title = window_title
        self.window_icon_location = window_icon_location
        self.window_icon = None

        # Graphics
        self.image = pygame.Surface(self.resolution)
        self.window_color = (100, 100, 100)
        self.display = None

        # computer
        self.delta = 0.0
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.exit = False

        # Open the display
        self.display = pygame.display.set_mode(self.resolution)
        if self.fullscreen:
            pygame.display.toggle_fullscreen()

        # Load window icon if path is set
        if self.window_icon_location is not None:
            self.window_icon = pygame.image.load(window_icon_location).convert()
            pygame.display.set_caption(self.window_title, self.window_icon)
        else:
            pygame.display.set_caption(self.window_title)

        self.message = ""

    def get_msg(self):
        msg = self.message
        self.message = ""
        return msg

    def run_once(self, run_count=1):

        self.delta = time()

        for n in range(run_count):

            self.delta = time()
            for event in pygame.event.get():
                self.event(event, self.delta)

        self.update(self.delta)
        self.draw()

    def run(self):

        while not self.exit:

            self.delta = time()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.quit()
                    pygame.quit()
                    quit()

                else:
                    self.event(event, self.delta)

            self.update(self.delta)

            # Check QUIT flag
            if self.exit:
                self.quit()
                pygame.quit()
                quit()

            self.draw()

            pygame.Surface.blit(self.display, self.image, (0, 0))
            pygame.display.update()
            self.clock.tick(self.fps)

    def event(self, event, delta):
        pass

    def update(self, delta):
        pass

    def draw(self):
        pass

    def quit(self):
        pass
