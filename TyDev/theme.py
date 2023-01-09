class Button:
    def __init__(self):
        self.bg_color = (54, 69, 79)
        self.font_color = (220, 230, 240)
        self.hover_color = (54, 69, 79)
        self.active_color = (33, 48, 58)

        self.font_size = 16

class Label:
    def __init__(self):
        self.font_color = (220, 230, 240)
        self.font_size = 18

class LineEdit:

    def __init__(self):

        self.font_size = 18
        self.font_color = (0, 0, 0)
        self.bg_color = (255, 255, 255)
        self.selected_color = (60, 60, 200)

## ---------------------------------------

class Theme:

    def __init__(self):
        self.button = Button()
        self.label = Label()
        self.line_edit = LineEdit()