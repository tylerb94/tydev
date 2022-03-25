import pygame
import tydev
from tydev.gui.template import Template


class List(Template):

    def __init__(self, location, size):
        Template.__init__(self, location=location, size=size)

        self.background_color = (255, 255, 255)
        self.highlight_color = (130, 145, 255)
        self.objects = []
        self.scroll_amount = 0.0
        self.scroll_max = 0.0
        self.scroll_speed = 25.0
        self.selected = -1
        self.map = {}
        self.list_height = 0.0
        self.redraw = True
        self.object_images = []

        self.scrollbar_location = [0, 0]
        self.scrollbar_bounds = [0, 0]
        self.scrollbar_width = 10
        self.scrollbar_color = (120, 130, 230, 255)
        self.scrollbar_backcolor = (50, 50, 50, 120)

    def append(self, object):
        self.objects.append(object)
        self.redraw = True

    def clear(self):
        self.objects.clear()
        self.redraw = True

    def count(self):
        return len(self.objects)

    def draw(self):

        if self.redraw:

            self.redraw = False

            # Render all the objects in the list
            self.object_images = []
            for obj in self.objects:
                obj.draw()

                self.object_images.append(obj.image)

        self.image.fill(self.background_color)

        # Place each list object onto the list image
        y = -self.scroll_amount
        self.list_height = 0.0
        index = 0
        self.map.clear()
        for img in self.object_images:

            # Remap the y locations of each object
            self.map[str(y)] = index

            # Highlight image if selected
            if self.selected == index:
                height = img.get_height()
                width = self.image.get_width()
                pygame.draw.rect(self.image, self.highlight_color,
                                 (0, y, width, height))
            index += 1

            # Draw the image
            self.image.blit(img, (0, y))
            y += img.get_height()
            self.list_height += img.get_height()


        self.scroll_max = self.list_height - self.size[1]

        # Draw scrollbar
        if self.list_height > self.size[1]:

            x = self.image.get_width() - self.scrollbar_width
            y = 0
            w = self.scrollbar_width
            h = self.image.get_height()
            self.scrollbar_bounds = (x, h)
            pygame.draw.rect(self.image, self.scrollbar_backcolor, (int(x), int(y), int(w), int(h)), 0)


            h = (self.size[1] / self.list_height) * self.size[1]
            y = (self.size[1] - h + 1)  * (self.scroll_amount / self.scroll_max)
            pygame.draw.rect(self.image, self.scrollbar_color, (int(x), int(y), int(w), int(h)), 0)

    def move(self, amount):
        self.selected += amount

        if self.selected < 0:
            self.selected = 0
        elif self.selected >= len(self.objects):
            self.selected = len(self.objects) - 1

    def event(self, event, delta):

        if self.mouse_over():

            if event.type == pygame.MOUSEWHEEL:

                if self.list_height > self.size[1]:
                    self.scroll_amount -= event.y * self.scroll_speed

                    if self.scroll_amount > self.scroll_max:
                        self.scroll_amount = self.scroll_max
                    elif self.scroll_amount < 0:
                        self.scroll_amount = 0

            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                if event.button == 1 or event.button == 3:
                    if self.mouse_over():
                        mouse = self.get_relative_mouse()
                        y = mouse[1]
                        for index in self.map:
                            if y > float(index):
                                self.selected = self.map[index]

        elif event.type == pygame.KEYDOWN:
            if self.has_focus:
                if event.button == pygame.K_UP:
                    self.move(-1)
                elif event.button == pygame.K_DOWN:
                    self.move(-1)

            index = 0
            height = 0
            for obj in self.objects:

                y = self.location[1] + height - self.scroll_amount
                x = self.location[0]
                height += obj.image.get_height()
                obj.location = [x, y]
                obj.event(event, delta)

                index += 1

    def update(self, delta):

        for obj in self.objects:
            obj.update(delta)