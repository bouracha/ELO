import numpy as np
import pandas as pd
from datetime import datetime

def update(rating1, rating2, score):
    K = 100

    score1 = score
    score2 = 1 - score

    ratingDifference = np.abs(rating1 - rating2)

    probabilityOfWeakerPlayerWinning = (1.0 / (1.0 + (10 ** ((ratingDifference * 1.0/ 400)))))

    probabilityOfStrongerPlayerWinning = 1 - probabilityOfWeakerPlayerWinning

    if (rating1 > rating2):
        prob_of_1_winning = probabilityOfStrongerPlayerWinning
        prob_of_2_winning = probabilityOfWeakerPlayerWinning
    else:
        prob_of_1_winning = probabilityOfWeakerPlayerWinning
        prob_of_2_winning = probabilityOfStrongerPlayerWinning

    print("Probability of White winning: {:.5f}".format(prob_of_1_winning))
    rating_change1 = (score1 - prob_of_1_winning)*K
    rating_change2 = (score2 - prob_of_2_winning)*K

    if np.abs(rating_change1) < 1:
        rating_change1 = rating_change1/np.abs(rating_change1)
    if np.abs(rating_change2) < 1:
        rating_change2 = rating_change2/np.abs(rating_change2)

    newRating1 = rating1 + rating_change1
    newRating2 = rating2 + rating_change2

    return round(newRating1), round(newRating2)



def write_new_rating(player, new_rating, opponent, result, game='chess', colour='white'):
    now = datetime.now()
    df = pd.DataFrame(np.array(np.expand_dims((new_rating, opponent, result, colour, now), axis=0)))
    with open(str(game)+'/'+str(player)+'.csv', 'a') as f:
        df.to_csv(f, header=False, index=False)


def read_ratings(player1, player2, game='chess'):
    data1 = pd.read_csv(str(game)+'/'+str(player1) + ".csv")
    data2 = pd.read_csv(str(game)+'/'+str(player2) + ".csv")

    rating1 = np.array(data1['rating'])
    rating2 = np.array(data2['rating'])

    return rating1, rating2

def make_new_player(player_name='default', game='chess'):
    head = np.array(['rating', 'opponent', 'result', 'colour', 'timestamp'])
    df = pd.DataFrame(np.array(np.expand_dims((1200.0, 'no opponent', 0, 'no colour', 'beginning of time'), axis=0)))
    df.to_csv(str(game)+'/'+str(player_name) + '.csv', header=head, index=False)