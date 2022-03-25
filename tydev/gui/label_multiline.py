import tydev.gui
from tydev.gui.template import Template
import pygame


class LabelMultiline(Template):

    def __init__(self, text, location=None, size=None):
        Template.__init__(self, size, location)
        self.text = text

    def draw(self):
        lines = self.text.split("\n")
        y = 0
        image_list = []
        self.size = [0, 0]
        for line in lines:
            line = tydev.gui.Label(text=line)
            line.draw()
            image_list.append((line.image, y))
            y += line.image.get_height()
            if line.image.get_width() > self.size[0]:
                self.size[0] = line.image.get_width()
            self.size[1] += line.image.get_height()

        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        if self.background_color is not None:
            self.image.fill(self.background_color)
        for line in image_list:
            self.image.blit(line[0], (0, line[1]))

