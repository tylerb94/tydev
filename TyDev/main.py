from tydev.window import Window
from tydev.guiwindow import GUIWindow
from tydev.gui import button
import main_ui
import random


class Main(GUIWindow):

    def __init__(self):

        GUIWindow.__init__(self, (400, 300), False, "GUI Window", main_ui.gui)

    def action(self, message):
        print(message)

        if message == "button_1 clicked":
            self.back_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

Main().run()