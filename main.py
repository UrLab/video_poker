from poker.poker import PokerGame

if __name__ == "__main__":
    game = PokerGame("lois", 100)
    while True:
        game.reset()
        print("New turn, your balance is %d" % game.get_balance())
        bet = input("what do you want to bet: ")
        game.make_turn(int(bet))
        print("here is your hand")
        game.show_hand()
        print(game.test_hand()['name'])
        print("Which card do you want to change?")
        print("mark their number separated by , and just enter if nothing")
        choice = input()
        choices = choice.split(',')
        for c in choices:
            try:
                int(c)
                game.replace(c)
            except:
                pass
        print("Here is your hand:")
        game.show_hand()
        res = game.validate_hand()
        print("You got: %s and are rewared %d" % (res["name"], res["payout"]))