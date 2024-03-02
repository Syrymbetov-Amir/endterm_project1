import pygame
from collections import deque

class LiveStockGraph:
    def __init__(self, stock_simulator, screen, rect):
        self.stock_simulator = stock_simulator
        self.screen = screen
        self.rect = rect
        self.price_history = deque(maxlen=100)
        self.line_color = (0, 0, 255)
        self.font = pygame.font.Font(None, 25)  # Set font for text

    def update(self):
        self.price_history.append(self.stock_simulator.get_price())

    def draw(self):
        graph_surface = pygame.Surface((self.rect.width, self.rect.height))
        graph_surface.fill((255, 255, 255))  # Fill background with white

        # Plot the price history
        if len(self.price_history) > 1:
            scaled_points = self._scaled_points()
            pygame.draw.lines(graph_surface, self.line_color, False, scaled_points, 2)

        # Add text
        text_surface = self.font.render("Live Price", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(self.rect.width // 2, 20))
        graph_surface.blit(text_surface, text_rect)

        # Blit graph onto screen
        self.screen.blit(graph_surface, self.rect.topleft)

    def _scaled_points(self):
        # Scale price history to fit within the graph rectangle
        max_price = max(self.price_history)
        min_price = min(self.price_history)
        scaled_points = []
        for i, price in enumerate(self.price_history):
            x = i * self.rect.width / len(self.price_history)  # Scale x-coordinate dynamically
            y = self.rect.height - (price - min_price) / (max_price - min_price) * self.rect.height
            scaled_points.append((x, y))
        return scaled_points
