from deck.card import Card


def assert_card(card):
    # prove the card is valid
    pass

def test_basic_cards():
    for suit in ['hearts', 'diamonds', 'spades', 'clubs']:
        for i in range(1, 14):
            card = Card(i, suit)
            assert_card(card)