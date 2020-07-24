import random
from operator import itemgetter


def get_high_score(input_scores):
    en_list = list(enumerate(input_scores, 1))
    return max(en_list, key=itemgetter(1))


class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __str__(self):
        return f'{self.value} of {self.color}'


colors = ['heart', 'diamond', 'spades', 'clubs']

deck = [Card(value, color) for value in range(1, 14) for color in colors]
random.shuffle(deck)


while True:
    try:
        player_count = int(input('Enter the amount of players: '))
        break
    except ValueError:
        print('Please enter a valid value')


scores = []
current_card = 0
while True:
    for i in range(player_count):
        scores.append(0)
        while True:
            input_i = input(f'Player {i + 1} please enter PASS or HIT: ')
            if input_i == 'PASS':
                print(f'Player {i+1}s score is: {scores[i]}')
                break
            elif input_i == 'HIT':
                value = deck[current_card].value
                scores[i] += value
                current_card += 1
                if scores[i] > 21:
                    scores[i] = 0
                    print(f'Player {i + 1} has burned in flames! Score set to 0!')
                else:
                    print(f'Current score: {scores[i]}')
            else:
                continue

    best_score = get_high_score(input_scores=scores)
    print(f'Player {best_score[0]} is the winner with a score of {best_score[1]}')
    break
