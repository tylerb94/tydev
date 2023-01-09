import pygame.font
from tydev.gui import Button, Label, LineEdit
import theme

pygame.font.init()
t = theme.Theme()

gui = {
    "button_1": Button((10, 10), (55, 30), "Click Me", t),
    "button_2": Button((100, 100), (55, 30), "Click Me", t),
    "label_1": Label((30, 150), "Label", t),
    "line_edit": LineEdit((100, 50), (100, 25), t, text="The")

}
