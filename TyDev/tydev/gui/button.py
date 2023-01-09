import pygame
from tydev.gui.label import Label
from tydev.gui.template import Template

class Button(Template):
    def __init__(self, position, size, label, theme, visible=True):
        super().__init__(position, size, visible=visible)

        self.label = label
        self.font_size = theme.button.font_size
        self.font_color = theme.button.font_color
        self.bg_color = theme.button.bg_color
        self.hover_color = theme.button.hover_color
        self.active_color = theme.button.active_color
        self.mouse_over = False
        self.active = False
        self.label_obj = Label(position, label, theme, visible=True)
        self.center_label()

    def center_label(self):
        label_width, label_height = self.label_obj.font.size(self.label)
        label_x = self.rect.x + (self.rect.width - label_width) // 2
        label_y = self.rect.y + (self.rect.height - label_height) // 2
        self.label_obj.position = (label_x, label_y)

    def handle_event(self, event, delta_time, name):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
                return name + " clicked"
        elif event.type == pygame.MOUSEBUTTONUP:
            self.active = False
            if self.rect.collidepoint(event.pos):
                return name + " released"
        elif event.type == pygame.MOUSEMOTION:
            self.mouse_over = self.rect.collidepoint(event.pos)

    def update(self, delta_time):
        pass

    def draw(self, surface):
        if not self.visible:
            return

        if self.active:
            color = self.active_color
        elif self.mouse_over:
            color = self.hover_color
        else:
            color = self.bg_color

        pygame.draw.rect(surface, color, self.rect)
        self.label_obj.draw(surface)
