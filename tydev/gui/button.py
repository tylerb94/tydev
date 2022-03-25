from tydev.gui.template import Template
from pygame import Surface as surf
from pygame import font, SRCALPHA
import pygame

class Button(Template):

    def __init__(self, location=None, text=""):
        Template.__init__(self, location)

        # Geometry info
        if location is None: location = [0, 0]
        self.auto_size = True

        # Display info
        self.text = text
        self.icon = None

        # Background info
        self.id = 'button'
        self.pressed = False

        # Render first image
        self.draw()

        # Colors
        self.background_color = (180, 180, 180)
        self.background_color_hover = (90, 90, 90)
        self.background_color_press = (0, 0, 0)

    def draw(self):

        # Build the font, render the text
        _text = self.text_render()

        # Autosize
        _rect = self.size                           # Get the current size of label
        if self.auto_size:                          # If autosize is on
            r = _text.get_rect()                        # Get size of rendered text
            _rect = [r[2], r[3]]                        # Save size in label size
        self.size = _rect

        # Label will be same size as...
        # rendered text. Adjust as needed

        # Create the label image
        self.image = surf(self.size, SRCALPHA)           # Create surface with label's new size
        if self.background_color:                   # Fill background if color is set

            if self.has_focus:
                self.image.fill(self.background_color_hover)
            else:
                self.image.fill(self.background_color)

            if self.pressed:
                self.image.fill(self.background_color_press)

        # Put text render on label image
        self.image.blit(_text, (0, 0))

    def update(self, delta):
        if not self.mouse_over():
            self.has_focus = False

    def event(self, event, delta):

        if self.mouse_over():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.pressed = True

            elif self.pressed and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.pressed = False
        else:
            self.pressed = False