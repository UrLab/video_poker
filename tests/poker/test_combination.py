from deck.card import Card
from poker.hand import Hand
from poker.scores import SCORES
from poker.scoring import is_royal_flush, is_straight_flush, is_4_of_a_kind, \
    is_full_house, is_flush, is_straight, is_3_of_a_kind, is_two_pair


def test_empty_hand_has_no_value():
    hand = Hand()
    for score in SCORES:
        assert not score['tester'](hand)


def test_royal_flush():
    hand = Hand()
    hand.receive(Card(14, 'heart'))
    hand.receive(Card(13, 'heart'))
    hand.receive(Card(12, 'heart'))
    hand.receive(Card(11, 'heart'))
    hand.receive(Card(10, 'heart'))
    assert is_royal_flush(hand)


def test_straight_flush():
    hand = Hand()
    hand.receive(Card(12, 'heart'))
    hand.receive(Card(11, 'heart'))
    hand.receive(Card(10, 'heart'))
    hand.receive(Card(9, 'heart'))
    hand.receive(Card(8, 'heart'))
    assert is_straight_flush(hand)


def test_4_of_a_kind():
    hand = Hand()
    hand.receive(Card(9, 'heart'))
    hand.receive(Card(9, 'club'))
    hand.receive(Card(9, 'spade'))
    hand.receive(Card(9, 'diamond'))
    hand.receive(Card(8, 'heart'))
    assert is_4_of_a_kind(hand)


def test_full_house():
    hand = Hand()
    hand.receive(Card(9, 'heart'))
    hand.receive(Card(9, 'club'))
    hand.receive(Card(9, 'spade'))
    hand.receive(Card(7, 'diamond'))
    hand.receive(Card(7, 'heart'))
    assert is_full_house(hand)


def test_3_of_a_kind_is_not_full_house():
    hand = Hand()
    hand.receive(Card(9, 'heart'))
    hand.receive(Card(9, 'club'))
    hand.receive(Card(9, 'spade'))
    hand.receive(Card(7, 'diamond'))
    hand.receive(Card(6, 'heart'))
    assert not is_full_house(hand)



def test_flush():
    hand = Hand()
    hand.receive(Card(12, 'heart'))
    hand.receive(Card(10, 'heart'))
    hand.receive(Card(8, 'heart'))
    hand.receive(Card(6, 'heart'))
    hand.receive(Card(4, 'heart'))
    assert is_flush(hand)


def tet_straight():
    hand = Hand()
    hand.receive(Card(12, 'heart'))
    hand.receive(Card(11, 'spade'))
    hand.receive(Card(10, 'club'))
    hand.receive(Card(9, 'diamond'))
    hand.receive(Card(8, 'heart'))
    assert is_straight(hand)


def test_straight_starting_with_ace():
    hand = Hand()
    hand.receive(Card(14, 'heart'))
    hand.receive(Card(2, 'spade'))
    hand.receive(Card(3, 'club'))
    hand.receive(Card(4, 'diamond'))
    hand.receive(Card(5, 'heart'))
    assert is_straight(hand)


def test_3_of_a_kind():
    hand = Hand()
    hand.receive(Card(9, 'heart'))
    hand.receive(Card(9, 'club'))
    hand.receive(Card(9, 'spade'))
    hand.receive(Card(7, 'diamond'))
    hand.receive(Card(8, 'heart'))
    assert is_3_of_a_kind(hand)


def test_is_two_pair():
    hand = Hand()
    hand.receive(Card(9, 'heart'))
    hand.receive(Card(7, 'club'))
    hand.receive(Card(9, 'spade'))
    hand.receive(Card(7, 'diamond'))
    hand.receive(Card(8, 'heart'))
    assert is_two_pair(hand)


def test_nothing_is_nothing():
    hand = Hand()
    hand.receive(Card(12, 'heart'))
    hand.receive(Card(10, 'club'))
    hand.receive(Card(8, 'diamond'))
    hand.receive(Card(6, 'spade'))
    hand.receive(Card(4, 'heart'))
    for score in SCORES:
        assert not score['tester'](hand)

