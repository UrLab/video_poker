import pytest
from deck.deck import Deck
from exception.exceptions import HandFullException
from poker.hand import Hand


def test_hand_picking():
    deck = Deck()
    original_size = len(deck)
    hand = Hand()
    card = deck.deal()
    hand.receive(card)
    assert deck.dealed[0] == hand[0]
    assert len(hand) == 1
    assert len(deck) == original_size - 1


def test_hand_cannot_be_greater_than_5():
    deck = Deck()
    hand = Hand()
    with pytest.raises(HandFullException):
        for i in range(10):
            hand.receive(deck.deal())