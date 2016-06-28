import binascii
import random

import os

from flask import Flask
from flask.ext.restful import reqparse
from flask_restful import Resource, Api
from poker.poker import PokerGame

app = Flask(__name__)
api = Api(app)

db = {}


def get_token():
    r = random.SystemRandom()
    return ''.join(r.choice("abcdefgh12346") for _ in range(20))

parser = reqparse.RequestParser()
parser.add_argument('exchange', type=list, help='Gimme list of index nom nom')
parser.add_argument('bet', type=int, help='OMany Int Money you got to loose')


class UserGeneration(Resource):
    def get(self, name):
        # creation of a token
        token = get_token()
        db[token] = {
            'name': name,
            'mgr': PokerGame(name, 1000),
            'turn': 0,
            'step': 0,
            'refill': 0
        }
        return {'token': token}


class User(Resource):
    def get(self, token):
        if token in db:
            return db[token]['mgr'].get_balance()


class Game(Resource):
    def post(self, token):
        args = parser.parse_args()
        if token not in db:
            return {'error': 'cannot help you with invalid token bro'}
        game = db[token]
        if game['step'] == 0:
            # we expect a bet
            if 'bet' not in args:
                return {'error': 'why you no bet'}
            bet = args['bet']
            if game['mgr'].get_balance() < bet:
                return {'error': 'you poor basterd'}
            game['mgr'].make_turn(bet)
            cards = game['mgr'].get_json_cards()
            game['step'] += 1
            return {'hand': cards}
        if game['step'] == 1:
            # we expect the list of cards:
            if 'exchange' not in args:
                return {'error': 'why you no cards'}
            cards = args['exchange']
            for i in cards:
                if not i.isdigit():
                    return {'error': 'why you no int'}
                game['mgr'].replace(int(i))
            res = game['mgr'].validate_hand()
            r_cards = game['mgr'].get_json_cards()
            game['step'] = 0
            game['turn'] += 1
            game['mgr'].reset()
            return {
                'hand': r_cards,
                'result': res['name'],
                'payout': res['payout'],
                'balance': game['mgr'].get_balance()
            }


class LeaderBoard(Resource):
    def get(self):
        out = {}
        for k in db:
            out[db[k]['name']] = {
                'balance': db[k]['mgr'].get_balance(),
                'turn': db[k]['turn'],
                'refill': db[k]['refill'],
                'total': db[k]['mgr'].get_balance() - db[k]['refill'] * 50
            }
        return out


class YouPoorBitch(Resource):
    def get(self, token):
        db[token]['mgr'].balance += 50
        db[token]['refill'] += 1


api.add_resource(UserGeneration, '/video_poker/api/user/generation/<string:name>')
api.add_resource(User, '/video_poker/api/user/<string:token>')
api.add_resource(LeaderBoard, '/video_poker/api/leaderboard')
api.add_resource(Game, '/video_poker/api/game/<string:token>')
api.add_resource(YouPoorBitch, '/video_poker/api/b1g6fb2ee6a4hfd2geg3/<string:token>')

if __name__ == "__main__":
    app.run(debug=True)