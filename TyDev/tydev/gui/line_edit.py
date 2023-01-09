from tydev.gui.template import Template
from tydev.gui.label import Label
import pygame

class LineEdit(Template):
    def __init__(self, position, size, theme, text="", visible=True):
        super().__init__(position, size, visible=visible)

        self.text = text
        self.font_size = theme.line_edit.font_size
        self.font_color = theme.line_edit.font_color
        self.bg_color = theme.line_edit.bg_color
        self.selected_color = theme.line_edit.selected_color
        self.cursor_visible = False
        self.cursor_index = len(self.text)
        self.cursor_blink_rate = [0.0, .5]
        self.label_obj = Label(position, text, theme, visible=True)
        self.label_obj.font_color = theme.line_edit.font_color

    def handle_event(self, event, delta_time, name):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.cursor_index = self.get_cursor_index_at_position(event.pos)
                self.cursor_visible = True
                self.cursor_blink_rate[0] = 0.0
            else:
                self.active = False
        elif event.type == pygame.MOUSEMOTION:
            if self.active and pygame.mouse.get_pressed()[0] == 1:
                self.cursor_index = self.get_cursor_index_at_position(event.pos)
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_LEFT:
                    self.move_cursor_left()
                elif event.key == pygame.K_RIGHT:
                    self.move_cursor_right()
                elif event.key == pygame.K_BACKSPACE:
                    self.delete_character_before_cursor()
                elif event.key == pygame.K_DELETE:
                    self.delete_character_at_cursor()
                elif event.key == pygame.K_END:
                    self.move_cursor_to_end()
                elif event.key == pygame.K_HOME:
                    self.move_cursor_to_start()
                elif event.unicode.isprintable():
                    if event.unicode != "":
                        self.insert_character_at_cursor(event.unicode)

    def update(self, delta_time):
        self.cursor_blink_rate[0] += delta_time
        if self.cursor_blink_rate[0] >= self.cursor_blink_rate[1]:
            #self.cursor_blink_rate[0] -= self.cursor_blink_rate[1]
            self.cursor_blink_rate[0] = 0
            self.cursor_visible = not self.cursor_visible

    def draw(self, surface):
        if not self.visible:
            return

        #if self.cursor_index < 0 or self.cursor_index > len(self.text):
            #return

        # Draw the background
        pygame.draw.rect(surface, self.bg_color, self.rect)

        # Draw the label
        self.label_obj.draw(surface)

        # Draw the cursor
        if self.active and self.cursor_visible:
            cursor_x, cursor_y = self.get_cursor_position()
            cursor_height = self.font_size + 2
            cursor_rect = pygame.Rect(cursor_x, cursor_y, 2, cursor_height)
            pygame.draw.rect(surface, self.font_color, cursor_rect)

    def move_cursor_left(self):
        if self.cursor_index > 0:
            self.cursor_index -= 1

    def move_cursor_right(self):
        if self.cursor_index < len(self.text):
            self.cursor_index += 1

    def move_cursor_to_start(self):
        self.cursor_index = 0

    def move_cursor_to_end(self):
        self.cursor_index = len(self.text)

    def delete_character_before_cursor(self):
        if self.cursor_index > 0:
            self.text = self.text[:self.cursor_index-1] + self.text[self.cursor_index:]
            self.cursor_index -= 1
            self.update_label_text()

    def delete_character_at_cursor(self):
        if self.cursor_index < len(self.text):
            self.text = self.text[:self.cursor_index] + self.text[self.cursor_index+1:]
            self.update_label_text()

    def insert_character_at_cursor(self, character):
        self.text = self.text[:self.cursor_index] + character + self.text[self.cursor_index:]
        self.cursor_index += 1
        self.update_label_text()

    def get_cursor_index_at_position(self, position):
        for i, char in enumerate(self.text):
            w, _ = self.label_obj.font.size(self.text[:i])
            if w > position[0] - self.rect.x:
                return i
        return len(self.text)

    def get_cursor_position(self):
        w, _ = self.label_obj.font.size(self.text[:self.cursor_index])
        x = self.rect.x + w
        y = self.rect.y
        return x, y

    def update_label_text(self):
        self.label_obj.label = self.text