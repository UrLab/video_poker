from poker.scoring import is_royal_flush, is_straight_flush, is_4_of_a_kind, \
    is_full_house, is_flush, is_straight, is_3_of_a_kind, is_two_pair, \
    is_nothing


SCORES = [
    {
        'name': 'Royal Flush',
        'ranking': 0,
        'payout': 110,
        'tester': is_royal_flush
    },
    {
        'name': 'Straight Flush',
        'ranking': 1,
        'payout': 40,
        'tester': is_straight_flush
    },
    {
        'name': '4-of-a-kind',
        'ranking': 2,
        'payout': 25,
        'tester': is_4_of_a_kind
    },
    {
        'name': 'Full House',
        'ranking': 3,
        'payout': 8,
        'tester': is_full_house
    },
    {
        'name': 'Flush',
        'ranking': 4,
        'payout': 5,
        'tester': is_flush
    },
    {
        'name': 'Straight',
        'ranking': 5,
        'payout': 4,
        'tester': is_straight
    },
    {
        'name': '3-of-a-kind',
        'ranking': 6,
        'payout': 3,
        'tester': is_3_of_a_kind
    },
    {
        'name': 'two pair',
        'ranking': 7,
        'payout': 2,
        'tester': is_two_pair
    },
    {
        'name': 'nothing',
        'ranking': 8,
        'payout': 0,
        'tester': is_nothing
    }
]
