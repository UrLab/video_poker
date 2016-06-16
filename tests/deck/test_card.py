import pytest
from deck.card import Card


def test_cards_creation():
    for suit in ['heart', 'diamond', 'spade', 'club']:
        for rank in range(1, 14):
            card = Card(rank, suit)
            assert rank == card.get_rank()
            assert suit == card.get_suit()


def test_card_rank_setting():
    card = Card(1, 'heart')
    card.set_rank(2)
    assert 2 == card.get_rank()


def test_card_suit_setting():
    card = Card(1, 'heart')
    card.set_suit('club')
    assert 'club' == card.get_suit()
