from poker.scoring import is_royal_flush, is_4_deuces, is_wild_royal, \
    is_5_of_a_kind, is_straight_flush, is_4_of_a_kind, is_full_house, \
    is_flush, is_straight, is_3_of_a_kind

SCORES = [
    {
        'name': 'Royal Flush',
        'ranking': 0,
        'payout': 800,
        'tester': is_royal_flush
    },
    {
        'name': '4 deuces',
        'ranking': 1,
        'payout': 200,
        'tester': is_4_deuces
    },
    {
        'name': 'Wild Royal',
        'ranking': 2,
        'payout': 25,
        'tester': is_wild_royal
    },
    {
        'name': '5-of-a-kind',
        'ranking': 3,
        'payout': 15,
        'tester': is_5_of_a_kind
    },
    {
        'name': 'Straight Flush',
        'ranking': 4,
        'payout': 9,
        'tester': is_straight_flush
    },
    {
        'name': '4-of-a-kind',
        'ranking': 5,
        'payout': 5,
        'tester': is_4_of_a_kind
    },
    {
        'name': 'Full House',
        'ranking': 6,
        'payout': 3,
        'tester': is_full_house
    },
    {
        'name': 'Flush',
        'ranking': 7,
        'payout': 2,
        'tester': is_flush
    },
    {
        'name': 'Straight',
        'ranking': 7,
        'payout': 2,
        'tester': is_straight
    },
    {
        'name': '3-of-a-kind',
        'ranking': 8,
        'payout': 1,
        'tester': is_3_of_a_kind
    },
]
