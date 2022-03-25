from pygame import Surface as surf
from pygame import font, SRCALPHA
import pygame

class Template:

    def __init__(self, location=None, size=None):

        # Geometry info
        if location is None: location = [0, 0]
        if size is None: size = [1, 1]
        self.location = location
        self.size = size
        self.image = surf(self.size, pygame.SRCALPHA)
        self.background_color = None

        # Font info
        self.font_color = (0, 0, 0)
        self.font_name = 'FreeSans'
        self.font_size = 20
        self.font_bold = False
        self.font_italic = False
        self.font_antialias = True

        # Background into
        self.id = ''
        self.has_focus = False
        self.has_focus_new = False

        # Event Messages
        self.event_messages = {
            pygame.MOUSEBUTTONDOWN: 'mouse_click',
            pygame.MOUSEBUTTONUP: 'mouse_release',
            pygame.MOUSEMOTION: 'mouse_move',
            pygame.MOUSEWHEEL: 'mouse_scroll',
            pygame.KEYDOWN: 'key_press',
            pygame.KEYUP: 'key_release',
        }

    def get_focus(self):
        if self.has_focus and self.has_focus_new:
            self.has_focus_new = False
        return self.has_focus

    def text_render(self, text=None):

        if text is None:
            text = self.text

        # Build the font, render the text
        font.init()
        _font = font.SysFont(self.font_name, self.font_size, self.font_bold, self.font_italic, None)
        return _font.render(text, self.font_antialias, self.font_color, None)

    def get_relative_mouse(self):
        m = pygame.mouse.get_pos()
        return m[0] - self.location[0], m[1] - self.location[1]

    def mouse_over(self):

        m = pygame.mouse.get_pos()
        l = self.location

        if l[0] <= m[0] <= l[0] + self.size[0]:
            if l[1] <= m[1] <= l[1] + self.size[1]:
                return True
        return False

    def width(self):
        return self.size[0]

    def height(self):
        return self.size[1]

    def get_size(self):
        return (self.width(), self.height())

    def event(self, event, delta):
        pass

    def draw(self):
        pass

    def update(self, delta):
        pass