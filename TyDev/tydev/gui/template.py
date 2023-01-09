import pygame

class Template:
    def __init__(self, position, size, visible=True):
        self.position = position  # Position of the element (x, y)
        self.size = size  # Size of the element (width, height)
        self.visible = visible  # Whether the element is visible or not
        self.active = False
        self._rect = None  # Add an attribute to store the rect

    @property
    def rect(self):
        if self._rect is None:
            # Create a rect based on the position and size attributes
            self._rect = pygame.Rect(self.position, self.size)
        return self._rect

    def handle_event(self, event, delta_time, name):
        """Handle events from the event queue."""
        pass

    def update(self, delta_time):
        """Update the element state."""
        pass

    def draw(self, surface):
        """Draw the element to the given surface."""
        if not self.visible:
            return  # Don't draw the element if it is not visible

        # Draw the element here
        # You can use self.position and self.size to determine the position and size of the element
        pass
