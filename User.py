from collections import defaultdict
from datetime import datetime
from typing import Literal

_credit_KT = Literal['small', 'medium', 'big']
CREDIT_VALUES: dict[_credit_KT, int] = {
    'small': 100,
    'medium': 1000,
    'big': 10000
}
INTEREST_RATE = 2
CREDIT_LIMIT = 10


class User:
    def __init__(self, user_id: int, name: str, start_balance: float):
        self.user_id = user_id
        self.name = name
        self.balance = start_balance
        self.stocks_count = defaultdict(lambda: 0)
        self.credits: dict[_credit_KT, int] = {
            "small": 0,
            "medium": 0,
            "big": 0
        }
        self._start_time = datetime.now()

    def get_play_time(self):
        time_difference = datetime.now() - self._start_time
        minutes_diff = time_difference.total_seconds() / 60

        return int(minutes_diff)

    def repay_credit(self, credit_type: _credit_KT) -> str:  # result
        val = CREDIT_VALUES[credit_type] * INTEREST_RATE
        if self.credits[credit_type] == 0:
            return "Credit has not been taken yet"

        elif val > self.balance:
            return "Not enough money"

        self.credits[credit_type] -= 1
        self.balance -= val
        return f"-1 {credit_type} credit"

    def take_credit(self, credit_type: _credit_KT) -> str:  # result
        if sum(self.credits.values()) == CREDIT_LIMIT:
            return "Credit limit hit"

        val = CREDIT_VALUES[credit_type]
        self.credits[credit_type] += 1
        self.balance += val
        return f"+1 {credit_type} credit"

    def calculate_total_credit_owed(self) -> float:
        res = 0
        for key, val in self.credits:
            res += CREDIT_VALUES[key] * val

        return res
