import pygame
from tydev.gui.template import Template

class Label(Template):
    def __init__(self, position, label, theme, visible=True):
        super().__init__(position, (0, 0), visible)  # The size of the label is determined by the text
        self.label = label
        self.font_size = theme.label.font_size
        self.font_color = theme.label.font_color
        self.font = pygame.font.Font(None, self.font_size)  # Load default font

    def handle_event(self, event, delta_time, name):
        pass  # Labels do not handle events

    def update(self, delta_time):
        pass  # Labels do not need updates

    def draw(self, surface):
        if not self.visible:
            return  # Don't draw the element if it is not visible

        # Render the label text
        text = self.font.render(self.label, True, self.font_color)
        text_rect = text.get_rect(topleft=self.position)  # Position the text based on the label position
        surface.blit(text, text_rect)

