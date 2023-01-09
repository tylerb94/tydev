import pygame
import timeit

class Window:
    def __init__(self, resolution, fullscreen, title, icon=None):
        """
        Initialize the window with the given resolution, fullscreen setting,
        title, and icon.
        """
        # Set window properties
        self.resolution = resolution
        self.fullscreen = fullscreen
        self.title = title
        self.icon = icon
        self.display = None
        self.exit = False  # Flag to control game loop
        self.delta_time = 0.0  # Time elapsed since last frame
        self.fps = 60  # Target frame rate
        self.clock = pygame.time.Clock()  # FPS clock

        # Set up the display
        self.display = pygame.display.set_mode(self.resolution)
        if self.fullscreen:
            pygame.display.toggle_fullscreen()
        pygame.display.set_caption(self.title)
        if self.icon is not None:
            icon_image = pygame.image.load(self.icon).convert()
            pygame.display.set_caption(self.title, icon_image)

    def run(self):
        """Run the game loop until the exit flag is set to True."""
        while not self.exit:
            # Process events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
                else:
                    self.handle_event(event, self.delta_time)

            # Update game state and render to display
            self.update(self.delta_time)
            self.draw()
            pygame.display.update()

            # Limit frame rate
            self.delta_time = timeit.timeit()
            self.clock.tick(self.fps)

        # Clean up resources and exit
        pygame.quit()
        quit()

    def handle_event(self, event, delta_time):
        """Handle events from the event queue."""
        pass

    def update(self, delta_time):
        """Update the game state."""
        pass

    def draw(self):
        """Render the game to the display surface."""
        pass
