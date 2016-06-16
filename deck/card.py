

class Card(object):
    def __init__(self, rank, suit):
        self._test_card_validity(rank, suit)
        self.rank = rank
        self.suit = suit

    @staticmethod
    def _test_card_validity(rank, suit):
        if rank < 1 or rank > 13:
            raise ValueError
        if suit not in ['heart', 'diamond', 'spade', 'club']:
            raise ValueError

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def set_rank(self, rank):
        self._test_card_validity(rank, self.suit)
        self.rank = rank

    def set_suit(self, suit):
        self._test_card_validity(self.rank, suit)
        self.suit = suit
