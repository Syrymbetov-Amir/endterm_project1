import numpy as np


class StockSimulator:
    def __init__(self, stock_name: str, initial_price: float, image_url: str, drift=0.015, volatility=0.2):
        # Geometric Brownian Motion (GBM) algorithm
        self.stock_name = stock_name
        self.image_url = image_url

        self._price = initial_price
        self._drift = drift
        self._volatility = volatility

        self._price_sequence = [initial_price]

    def generate_next_price(self):
        increment = self._drift + self._volatility * np.random.normal()
        self._price *= (1 + increment)
        self._price_sequence.append(self._price)

    def get_price(self) -> float:
        return round(self._price, 2)

    def get_price_sequence(self):
        return self._price_sequence
