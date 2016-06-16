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


def test_invalid_rank_rejected():
    with pytest.raises(ValueError):
        Card(0, 'club')
        Card(14, 'club')


def test_invalid_suit_rejected():
    with pytest.raises(ValueError):
        Card(1, 'nonheart')
        Card(1, 'hearts')
        Card(1, 'hear')


def test_invalid_rank_set_rejected():
    card = Card(1, 'heart')
    with pytest.raises(ValueError):
        card.set_rank(14)


def test_invalid_suit_set_rejected():
    card = Card(1, 'heart')
    with pytest.raises(ValueError):
        card.set_suit('he')
