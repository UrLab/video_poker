from deck.deck import Deck
from poker.hand import Hand
from poker.scores import SCORES


class PokerGame(object):
    def __init__(self, user_name, balance):
        self.user = user_name
        self.balance = balance
        self.hand = None
        self.deck = None
        self.bet = 0
        self.reset()

    def get_balance(self):
        return self.balance

    def get_json_cards(self):
        c = []
        for i in range(len(self.hand.cards)):
            card = self.hand[i]
            c.append({
                'rank': card.get_rank(),
                'suit': card.get_suit(),
                'index': i
            })
        return c

    def make_turn(self, bet):
        self.bet = bet
        for i in range(5):
            self.deck.deal()
        self.hand.cards = self.deck.dealed

    def show_hand(self):
        for i in range(len(self.hand)):
            print("#%d:     %s" % (i, self.hand[i]))

    def test_hand(self):
        i = 0
        while i < len(SCORES):
            if SCORES[i]['tester'](self.hand):
                return SCORES[i]
            i += 1
        return SCORES[i]

    def validate_hand(self):
        score = self.test_hand()
        self.balance -= self.bet
        self.balance += score['payout'] * self.bet
        return score

    def replace(self, card):
        self.deck.replace(self.hand[int(card)])

    def reset(self):
        self.hand = Hand()
        self.deck = Deck()
        self.deck.shuffle()
        self.bet = 0
