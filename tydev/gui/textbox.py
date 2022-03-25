import pygame
import tydev.colors
from tydev.gui.template import Template


class Textbox(Template):

    def __init__(self, location, size):
        Template.__init__(self, location, size)
        self.redraw = True

        self.text = "1234567890"
        self.rendered_letters = []
        self.cursor_pos = 0
        self.displace = 0
        self.render_text_img_size = [1, 1]
        self.cursor_width = 1

        self.letter_map = {
            # "A": (x, y),
        }

    def event(self, event, delta):

        # If left clicking on the textbox
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.mouse_over():
                if self.get_focus():

                    # Get local mouse position
                    mx = self.get_relative_mouse()[0] + self.displace

                    # If there are rendered letters
                    if len(self.rendered_letters) > 0:

                        # Check if mouse is over each letter
                        for index in range(len(self.rendered_letters) - 1):

                            # Get the X location of the left and right side of rendered letter
                            left = self.letter_map[self.text[index]][0]
                            right = self.letter_map[self.text[index]][0] + self.rendered_letters[index].get_width()

                            # If mouse is over letter
                            if left <= mx <= right:

                                # move the cursor to index
                                self.cursor_pos = index + 1\
                                                  * int(abs(left - mx) <= abs(right - mx))

    def update(self, delta):
        pass

    def draw(self):

        # If the text has changed, re-render all the letters, one at a time.
        if self.redraw:

            index = 0

            # Store the letters X position (width), and the Y position (0).
            # Add up the widths of all the letters, keep track of tallest letter.
            for letter in self.text:

                # Render and add to rendered letters list
                self.rendered_letters.append(self.text_render(text=letter))

                # Track the locations to place the letter
                self.letter_map[self.text[index]] = (self.render_text_img_size[0], 0)
                letter = self.rendered_letters[-1]
                # Img width
                self.render_text_img_size[0] += letter.get_width() + self.cursor_width
                # Img height
                if self.render_text_img_size[1] < letter.get_height():
                    self.render_text_img_size[1] = letter.get_height()
                index += 1

            # Don't rerender the letters again unless they change
            self.redraw = False

        # Create image to hold rendered letters.
        img = pygame.Surface(self.render_text_img_size, pygame.SRCALPHA)
        self.image = pygame.Surface(self.render_text_img_size)
        self.image.fill(self.background_color)

        # Draw each letter onto the img, and the cursor
        index = 0
        for letter in self.letter_map:

            # Draw letter
            i = self.rendered_letters[index]    # Rendered letter image
            l = self.letter_map[letter]         # Letter location
            img.blit(i, l)

            if index == self.cursor_pos:

                # Details to draw cursor line
                # cursor_x_pos = l[0] + i.get_width() + (self.cursor_width / 2)
                cursor_x_pos = l[0] - (self.cursor_width)
                cursor_height = i.get_height()

                # Draw cursor line
                pygame.draw.line(img,
                                 tydev.colors.limegreen,
                                 (cursor_x_pos, 0),
                                 (cursor_x_pos, cursor_height),
                                 self.cursor_width)

            index += 1

        # Draw the cursor again. If the cursor is at the end, it won't draw because the cursor_pos
        # will be 1 greater than the length of the list of rendered letters.
        # Running it one more time outside the loop will draw ie.
        if index == self.cursor_pos:

            # Details to draw cursor line
            # cursor_x_pos = l[0] + i.get_width() + (self.cursor_width / 2)
            cursor_x_pos = l[0] + (self.cursor_width / 2)
            cursor_height = i.get_height()

            # Draw cursor line
            pygame.draw.line(img,
                             tydev.colors.limegreen,
                             (cursor_x_pos, 0),
                             (cursor_x_pos, cursor_height),
                             self.cursor_width)

        self.image.blit(img, (0, 0))