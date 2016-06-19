def is_royal_flush(hand):
    sorted_hand = hand.sorted()
    return is_straight(hand) \
           and is_flush(hand) \
           and sorted_hand[0].get_rank() == 10


def is_straight_flush(hand):
    return is_straight(hand) and is_flush(hand)


def is_4_of_a_kind(hand):
    if len(hand) < 4:
        return False
    i = 0
    while i < 5:
        if has_n_in_hand(hand, i, 4):
            return True
        i += 1
    return False


def is_full_house(hand):
    if is_3_of_a_kind(hand):
        sorted_hands = hand.sorted()
        first = sorted_hands[0]
        if has_n_in_hand(sorted_hands, 0, 3):
            # the brelan is in the first
            # so the pair must be in the hand
            return has_n_in_hand(sorted_hands, 4, 2)
        else:
            # the pair must be in the begining
            return has_n_in_hand(sorted_hands, 0, 2)
    return False


def is_flush(hand):
    if len(hand) != 5:
        return False
    cand = True
    i = 0
    suit = hand[i].get_suit()
    # a royal flush has all the same suit
    while cand and i < 5:
        if hand[i].get_suit() != suit:
            cand = False
        i += 1
    return cand


def is_straight(hand):
    if len(hand) != 5:
        return False
    # a straight has all different ranking


    i = 0
    while i < len(hand):
        j = 0
        while j < len(hand):
            if i != j:
                if hand[i].get_rank() == hand[j].get_rank():
                    return False
            j += 1
        i += 1

    sorted_hand = hand.sorted()
    correct = sorted_hand[0].get_rank() + 4 == sorted_hand[-1].get_rank()

    if not correct and sorted_hand[-1].get_rank() == 14:
        # if the biggest is a ace, we need to check if we don't have
        # 1 2 3 4 5
        correct = sorted_hand[0].get_rank() + 3 == sorted_hand[-2].get_rank()
    return correct


def is_3_of_a_kind(hand):
    if len(hand) < 3:
        return False
    i = 0
    while i < 5:
        if has_n_in_hand(hand, i, 3):
            return True
        i += 1
    return False


def is_two_pair(hand):
    if len(hand) != 5:
        return False
    # it can be on an ordered list
    # AABBC CAABB AACBB
    s_hands = hand.sorted()
    return has_n_in_hand(s_hands, 0, 2) and has_n_in_hand(s_hands, 2, 2) \
           or has_n_in_hand(s_hands, 1, 2) and has_n_in_hand(s_hands, 3, 2) \
           or has_n_in_hand(s_hands, 0, 2) and has_n_in_hand(s_hands, 3, 2)


def has_n_in_hand(hand, card_i, n):
    if len(hand) < n:
        return False
    j = 0
    same = 1
    while j < len(hand):
        if card_i != j:
            if hand[card_i].get_rank() == hand[j].get_rank():
                same += 1
        j += 1
    return same == n


def is_nothing(hand):
    return not (
        is_royal_flush(hand) or
        is_straight_flush(hand) or
        is_4_of_a_kind(hand) or
        is_full_house(hand) or
        is_flush(hand) or
        is_straight(hand) or
        is_3_of_a_kind(hand) or
        is_two_pair(hand)
    )
