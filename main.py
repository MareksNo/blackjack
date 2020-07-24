import random
from functools import total_ordering


@total_ordering
class Player:
    def __init__(self, score, name):
        self.score = score
        self.playing = True
        self.name = name

    def player_is_valid(self, other):

        return hasattr(other, 'score')

    def __gt__(self, other):
        if not self.player_is_valid(other=other):
            return NotImplemented

        return self.score > other.score

    def __eq__(self, other):
        if not self.player_is_valid(other=other):
            return NotImplemented

        return self.score == other.score

    def score_valid(self):
        if self.score > 21:
            print(f'You have burned {self.score} points!')
            self.score = 0
            return False
        return True

    def inc_score(self, inc_value):
        self.score += inc_value
        if self.score > 21:
            print(f'You have burned {self.score} points!')
            self.score = 0
            self.playing = False


class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __str__(self):
        return f'{self.value} of {self.color}'


class Game:
    def __init__(self, p_count, players):
        self.current_card = 0
        self.player_count = p_count
        self.players = players


colors = ['heart', 'diamond', 'spades', 'clubs']

deck = [Card(value, color) for value in range(1, 14) for color in colors]
random.shuffle(deck)


while True:
    player_list = []
    try:
        input_count = int(input('Enter the amount of players: '))

        for player in range(input_count):
            input_name = input(f'Please enter the name for player {player + 1}: ')
            player_list.append(Player(score=0, name=input_name))

        game = Game(p_count=input_count, players=player_list)

        break

    except ValueError:
        print('Please enter a valid value')


def game_start(players, current_card):

    for n in range(len(players)):
        player_turn(player_p=players[n], current_card=current_card)
        current_card = game.current_card

    best_player = sorted(player_list, reverse=True)[0]

    print(f'{best_player.name} is the winner with a score of {best_player.score}')

    for player2 in sorted(player_list, reverse=True):
        print(f'{player2.name} - {player2.score}')


def player_turn(player_p, current_card):

    player_input = input(f'{player_p.name} please enter PASS or HIT: ')

    if player_input == 'PASS':
        return print(f'{player_p.name}\'s score is: {player_p.score}')
    elif player_input == 'HIT':

        value = deck[game.current_card].value
        game.current_card += 1
        player_p.inc_score(value)

        if not player_p.playing:
            return None

        else:
            print(f'Current score: {player_p.score}')
            player_turn(player_p, current_card)

    else:
        player_turn(player_p=player_p, current_card=current_card)


game_start(players=player_list, current_card=game.current_card)
