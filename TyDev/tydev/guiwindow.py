import pygame
import queue
from tydev.window import Window

class GUIWindow(Window):
    def __init__(self, resolution, fullscreen, title, gui, icon=None):
        super().__init__(resolution, fullscreen, title, icon)
        self.elements = gui
        self.message_queue = queue.Queue()
        self.active_element = None
        self.back_color = (0, 0, 0)

    def add_element(self, name, element):
        self.elements[name] = element

    def remove_element(self, name):
        del self.elements[name]

    def get_element(self, name):
        return self.elements[name]

    def set_active_element(self, element):
        self.active_element = element

    def show_element(self, name):
        element = self.get_element(name)
        element.visible = True

    def hide_element(self, name):
        element = self.get_element(name)
        element.visible = False

    def handle_event(self, event, delta_time):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for element in self.elements.values():
                if element.rect.collidepoint(event.pos):
                    self.set_active_element(element)

        for key in self.elements:
            element = self.elements[key]
            if element == self.active_element:
                message = element.handle_event(event, delta_time, key)
                if message is not None:
                    self.message_queue.put(message)

    def update(self, delta_time):
        for element in self.elements.values():
            element.update(delta_time)
        while not self.message_queue.empty():
            message = self.message_queue.get()
            self.action(message)

    def draw(self):
        self.display.fill(self.back_color)
        for element in self.elements.values():
            element.draw(self.display)

    def action(self, message):
        pass
