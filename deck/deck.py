import random

from deck.card import Card
SUIT = ['heart', 'diamond', 'spade', 'club']


class Deck(object):
    def __init__(self):
        self.cards = []
        self.burned = []
        self.dealed = []
        self.current_card = 0
        self.init_cards()

    def init_cards(self):
        for suit in SUIT:
            for rank in range(2, 15):
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards, random.random)

    def is_ordered(self):
        ordered = True
        i = 0
        while ordered and i < len(SUIT):
            j = 2
            while ordered and j < 15:
                card = self[i * 13 + j - 1]
                if card.get_rank() != j or card.get_suit() != SUIT[i]:
                    ordered = False
                j += 1
            i += 1
        return ordered

    def deal(self):
        card = self.cards.pop()
        self.dealed.append(card)
        return card

    def replace(self, card):
        new_card = self.cards.pop()
        place = self.dealed.index(card)
        self.dealed[place] = new_card
        self.burned.append(card)
        return new_card

    def discard(self, card):
        self.dealed.remove(card)
        self.burned.append(card)

    def burned_size(self):
        return len(self.burned)

    def dealed_size(self):
        return len(self.dealed)

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
