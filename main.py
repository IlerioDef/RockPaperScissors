# This is a sample Python script.
from random import randrange


def screener(data, screen_limit=40):
    """
    :param data: any type of data that will be converted to string and returned
    :param screen_limit: the width of the screen so every line will look consistently. Default value = 40
    :return: type: str()
    """
    if len(data) <= screen_limit:
        string = (str(data)+"_"*(screen_limit-len(data)))
    else:
        string = str(data[:15])

    return string

def comp_player(game_type):
    """
    :param game_type: allows to choose the variants like:
    1 - Classical RPS
    2 - Rock-Paper-Scissors-Spock-Lizard
    3 - Rock-Paper-Scissors-Fire-Water
    :return: random value (1-5) depending on the game type
    """
    import random

    reply = None
    if game_type == 1:
        reply = randrange(1,4,1)
    elif game_type == 2 | 3:
        reply = randrange(1,6,1)
    else:
        print(screener(f"Wrong data type! Choose 1-3"))
    return reply

def win_checker(player1,player2,game_type):
    """

    :param player1: one of the positions (1-3 or 1-5)
    :param player2: one of the positions (1-3 or 1-5)
    :param game_type:
    1 - Classical RPS
    2 - Rock-Paper-Scissors-Spock-Lizard
    3 - Rock-Paper-Scissors-Fire-Water
    :return: 0 - tie,
    1 = player 1 wins,
     2 = player 2 wins
     None = if data is incorrect

    """

    if game_type == 1:
        ### 1-Rock, 2-Paper, 3-Scissors in rows and columns
                    #rock,paper,scissors
        scoreboard = [(0,   1,     2), #rock
                      (2,   0,     1), #paper
                      (1,   2,     0) #scissors
        ]
    elif game_type == 2:
                    #rock,paper,scissors,spock,lizard
        scoreboard = [(0,   1,      2,     1,     2), #rock
                      (2,   0,      1,     2,     1), #paper
                      (1,   2,      0,     1,     2), #scissors
                      (2,   1,      2,     0,     1), #spock
                      (1,   2,      1,     2,     0) #lizard
        ]
    elif game_type == 3:
                    #rock,paper,scissors,fire,  water
        scoreboard = [(0,   1,      2,     1,     2), #rock
                      (2,   0,      1,     1,     2), #paper
                      (1,   2,      0,     1,     2), #scissors
                      (2,   2,      2,     0,     1), #fire
                      (1,   1,      1,     2,     0) #Water
        ]
    else:
        print(f"Wrong game type! you've entered {game_type}")
        return None
    result = scoreboard[player2-1][player1-1]
    return result





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = comp_player(game_type=7)
    print(x)
    y = print(win_checker(game_type=1, player1=1, player2=3)) #player1 = paper,2, player2 = scissors, 3
    print(y)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

