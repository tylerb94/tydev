import pygame
from tydev.gui.template import Template
from pygame import Surface as surf
from pygame import font, SRCALPHA

class Label(Template):

    def __init__(self, location=None, text=""):
        Template.__init__(self, location)

        # Geometry info
        self.auto_size = False
        if location is None:
            location = [0, 0]
            self.auto_size = True

        # Display info
        self.text = text
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)

        # Render first image
        self.draw()

    def draw(self):

        # Build the font, render the text
        _text = self.text_render()

        # Autosize                                      # Get the current size of label
        if self.auto_size:                              # If autosize is on
            _rect = self.size
            r = _text.get_rect()                        # Get size of rendered text
            _rect = [_text.get_width(),                 # Save size in label size
                     _text.get_height()]
            self.size = _rect

        # Label will be same size as
        # rendered text. Adjust as needed

        # Create the label image
        self.image = surf(self.size, SRCALPHA)           # Create surface with label's new size
        if self.background_color:                   # Fill background if color is set
            self.image.fill(self.background_color)

        # Put text render on label image
        self.image.blit(_text, (0, 0))