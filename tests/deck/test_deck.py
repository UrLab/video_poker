from deck.deck import Deck


def test_deck_has_52_cards():
    deck = Deck()
    assert len(deck) == 52


def test_deck_has_unique_cards():
    deck = Deck()
    i = 0
    while i < len(deck):
        j = 0
        while j < len(deck):
            if i != j:
                assert deck[i] != deck[j]
            j += 1
        i += 1


def test_new_deck_is_ordered():
    deck = Deck()
    assert deck.is_ordered()


def test_shuffed_deck_is_not_ordered():
    deck = Deck()
    deck.shuffle()
    assert not deck.is_ordered()


def test_deal_card():
    deck = Deck()
    original_size = len(deck)
    card = deck.deal()
    assert len(deck) == original_size - 1
    assert deck.dealed[0] == card


def test_replaced_card():
    deck = Deck()
    original_size = len(deck)
    card = deck.deal()
    new_card = deck.replace(card)
    assert len(deck) == original_size - 2
    assert len(deck.dealed) == 1
    assert len(deck.burned) == 1
    assert card != new_card
    assert deck.dealed[0] == new_card
    assert deck.burned[0] == card


def test_replace_card_remain_at_same_place():
    deck = Deck()
    card1 = deck.deal()
    card2 = deck.deal()
    card3 = deck.deal()
    new_card = deck.replace(card2)
    assert new_card != card2
    assert card1 == deck.dealed[0]
    assert new_card == deck.dealed[1]
    assert card3 == deck.dealed[2]


def test_deck_burned_dealed_are_correct_size():
    deck = Deck()
    original_size = len(deck)
    card1 = deck.deal()
    card2 = deck.deal()
    deck.replace(card1)
    deck.replace(card2)
    assert len(deck) == 48
    assert len(deck) + deck.burned_size() + deck.dealed_size() == original_size


def test_discard_card():
    deck = Deck()
    original_size = len(deck)
    card1 = deck.deal()
    card2 = deck.deal()
    card3 = deck.deal()
    deck.discard(card2)
    assert len(deck) == original_size - 3
    assert len(deck.burned) == 1
    assert len(deck.dealed) == 2
    assert deck.dealed[0] == card1
    assert deck.dealed[1] == card3
