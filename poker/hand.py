from exception.exceptions import HandFullException


class Hand(object):
    def __init__(self):
        self.cards = []
        self.current_card = 0

    def receive(self, card):
        if len(self) == 5:
            raise HandFullException
        self.cards.append(card)

    def __len__(self):
        return len(self.cards)

    def __next__(self):
        if self.current_card >= len(self.cards):
            raise StopIteration
        else:
            self.current_card += 1
            return self.cards[self.current_card - 1]

    def __iter__(self):
        return self

    def __delitem__(self, key):
        self.cards.remove(key - 1)

    def __setitem__(self, key, value):
        self.cards.insert(key - 1, value)

    def __getitem__(self, key):
        return self.cards[key - 1]
