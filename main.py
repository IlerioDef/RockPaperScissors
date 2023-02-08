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

win_checker(player1,player2,game_type):
if game_type == 1:


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = comp_player(game_type=7)
    print(x)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

