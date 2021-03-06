import pytest
from deck.card import Card


def test_cards_creation():
    for suit in ['heart', 'diamond', 'spade', 'club']:
        for rank in range(2, 15):
            card = Card(rank, suit)
            assert rank == card.get_rank()
            assert suit == card.get_suit()


def test_card_rank_setting():
    card = Card(3, 'heart')
    card.set_rank(2)
    assert 2 == card.get_rank()


def test_card_suit_setting():
    card = Card(2, 'heart')
    card.set_suit('club')
    assert 'club' == card.get_suit()


def test_invalid_rank_rejected():
    with pytest.raises(ValueError):
        Card(1, 'club')
        Card(16, 'club')


def test_invalid_suit_rejected():
    with pytest.raises(ValueError):
        Card(2, 'nonheart')
        Card(2, 'hearts')
        Card(2, 'hear')


def test_invalid_rank_set_rejected():
    card = Card(2, 'heart')
    with pytest.raises(ValueError):
        card.set_rank(16)


def test_invalid_suit_set_rejected():
    card = Card(2, 'heart')
    with pytest.raises(ValueError):
        card.set_suit('he')


def test_card_equality():
    card0 = Card(2, 'heart')
    card1 = Card(2, 'heart')
    card2 = Card(2, 'club')
    card3 = Card(3, 'heart')
    card4 = Card(3, 'club')

    assert card0 == card1
    assert card0 != card2
    assert card0 != card3
    assert card0 != card4
