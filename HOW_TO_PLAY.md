# Welcome Welcome You GUY

You're are about to start playing at `VIDEO POKER`

It's like regular poker, except it's not. In Video poker, you receive five cards,
and you can change 0 to 5 one time. After that your hand is analysed and reward
is given, or not.

## Hand Combination
The different combination of cards are (with payout and description):

 - ROYAL FLUSH (110): A Straight flush starting at 10 to ace.
 - STRAIGHT FLUSH (40): Five cards of sequential rank and same suit
 - 4 of a kind (25): Four cards of same rank
 - Full House (8): A Three of a kind and a pair
 - Flush (5): Five cards of same suit
 - Straight (4): Five cards of sequential rank
 - 3 of a kind (3): Three cards of same rank
 - Two Pair (2): Two pairs of two cards of same rank
 
## Game Turn:
A turn is handled in 3 simple step:

 - You place your bet (an integer)
 - You receive your cards (5)
 - You decide which cards to replace (0 to 5)
 - You receive your payout.
 
## What if I don't have any more money
The bank is a merciful god, and will give you money, but be careful, there is 
a penalty to it. For every 50 pezz it costs you 65 on your total
 
## Goal of the game
Have the more total money $$$$$$$ with as little refill as possible on your total

## API ENDPOINTS
Everything for the api is at `http://MY-IP:5000/video_poker/api`

### `/team/generation/<string:team_name>` `GET`
First call to be done, this will give you your token

### `/team/<string:token>` `GET`
Will give you all the info for your team:

 - balance
 - turn
 - step in turn
 - refill
 - total

### `/refill/<string:token>` `GET`
Will give you 50 pezz but will take 65 from your total

### `/game/<string:token>` `POST`
 
 - When step is 0: You need to pass in parameters your bet, from 0 to your balance
 
 `curl -d "bet=50" http://127.0.0.1:5000/video_poker/api/game/<string:token>`
 
 This will return you your hand in the format of a list of cards, a card is compose by his
 index, is rank and is suit.
 
 - When step is 1: You need to pass a string representing which card you want to replace,
 if you want to replace the 1 and the 3 you send `exchange=01`
 
 `curl -d "exchange=0123" http://127.0.0.1:5000/video_poker/api/game/<string:token>`
 
 This will return you your new balance, your final hand, the payout and the result
 
 
## Representation
The rank goes from 2 to 14:

 - 2: 2
 - 3: 3
 - 4: 4
 - 5: 5
 - 6: 6
 - 7: 7
 - 8: 8
 - 9: 9
 - 10: 10
 - 11: Jack
 - 12: Queen
 - 13: King
 - 14: Ace


 
