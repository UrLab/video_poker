

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit

    def set_rank(self, rank):
        self.rank = rank

    def set_suit(self, suit):
        self.suit = suit
