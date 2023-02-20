import sys
import time
from random import randrange

from colorama import init

init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected

from pyfiglet import figlet_format

GAME_OPTIONS = {
        1: (
            "Rock!",
            "Paper!",
            "Scissors!"
        ),
        2: (
            "Rock!",
            "Paper!",
            "Scissors!",
            "Spock!",
            "Lizard!",
        ),
        3: (
            "Rock!",
            "Paper!",
            "Scissors!",
            "Fire!",
            "Water!",
        )

    }



def input_validator(text):
    if type(text) != str():
        raise ValueError
    if len(text) == 0:
        raise ValueError
def print_image(text):

    # TODO: писать "based on" со ссылкой на гитхаб не надо, видно же что используется функция из библиотеки ✅
    """
       :param str
       :return: None
       """
    # TODO: возвращать результат print не нужно ✅
    print(figlet_format(str(text), font='graceful'))



# TODO: дефолтное значение тут не нужно ✅
def game_logo(game_type):
    # TODO: Неописательное описание
    """
       Simple logo creator
       :param game_type: one of three game types
       # TODO: Ну, на самом деле эта функция ничего не возвращает, поэтому :return: тут не нужен ✅
       :return: None
    """
# TODO: функция делает очень много ненужного ✅
    if game_type in GAME_OPTIONS:
        [print_image(x) for x in GAME_OPTIONS[game_type]]
    else:
        raise ValueError



def show_board(score_board):

    delimiter()
    for k, v in score_board.items():
        # TODO: табуляция ломает скорборд ✅
        print(screener(f"  {k}  --------  {v}  "))
    delimiter()







# TODO: параметр screen_limit не нужен, он нигде не используется ✅
def screener(data):

    """
    # TODO: any type of data это конечно неправда
    :param data: string data
    :param screen_limit: the width of the screen so every line will look consistently. Default value = 40
    :return: type: str()
    """
        # TODO: функция с багами
    # TODO: вся функция заменяется на одну строку
    # return f"{data:-^{width}}"
    margin = str("-" * int((screen_limit - len(data) / 2)))
    # TODO: ???
    time.sleep(0.01)
    if len(data) <= screen_limit:
        string = (margin + str(data) + margin)
    else:
        string = margin + str(data[:screen_limit]) + margin

    return string


def comp_player(game_type):
    """
    :param game_type: allows to choose the variants like:
    1 - Classical RPS
    2 - Rock-Paper-Scissors-Spock-Lizard
    3 - Rock-Paper-Scissors-Fire-Water
    :return: random value (1-5) depending on the game type
    """

    reply = None
    # TODO: вместо условий и неявной зависимости лучше было бы передавать в функцию список опций
    # TODO: передавать в эту функцию количество опций и заменить дереве if-else на один вызов
    if game_type == 1:
        reply = randrange(1, 4, 1)

    # TODO: баг, крашится при выборе 2-го типа игры
    elif game_type == 2 | 3:
        reply = randrange(1, 6, 1)
    else:
        print(screener(f"Wrong data type! Choose 1-3"))
    return reply


def win_checker(player1, player2, game_type):
    """
    # TODO: вот тут очень пригодилось бы описание алгоритма
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
    try:
              # TODO: вынести scoreboard в словарь как с GAME_OPTIONS
        # TODO: кстати, а почему это называется scoreboard?
        if game_type == 1:
            # 1-Rock, 2-Paper, 3-Scissors in rows and columns
            # rock,paper,scissors
            scoreboard = [(0, 1, 2),  # rock
                          (2, 0, 1),  # paper
                          (1, 2, 0)  # scissors
                          ]
        elif game_type == 2:
            # rock,paper,scissors,spock,lizard
            scoreboard = [(0, 1, 2, 1, 2),  # rock
                          (2, 0, 1, 2, 1),  # paper
                          (1, 2, 0, 1, 2),  # scissors
                          (2, 1, 2, 0, 1),  # spock
                          (1, 2, 1, 2, 0)  # lizard
                          ]
        elif game_type == 3:
            # rock,paper,scissors,fire,  water
            scoreboard = [(0, 1, 2, 1, 2),  # rock
                          (2, 0, 1, 1, 2),  # paper
                          (1, 2, 0, 1, 2),  # scissors
                          (2, 2, 2, 0, 1),  # fire
                          (1, 1, 1, 2, 0)  # Water
                          ]
        else:
            print(f"Wrong game type! you've entered {game_type}")
            return None
        result = scoreboard[player2 - 1][player1 - 1]
    except IndexError:
        reply = f"Value is out of range, player1 = {player1} or player2 = {player2}"
        print(reply)
        result = None
    return result


def delimiter():
        for x in range(3):
            print(screener("  "))
        return
