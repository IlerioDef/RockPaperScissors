import sys
##test
from colorama import init

init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
from pyfiglet import figlet_format


def print_image(text):
    """
       Based on https://github.com/pwaller/pyfiglet

       :param text: if not string, - converts value to string and processes it into ASCII-art.
       :return: ASCII-art printed text
       """
    result = print(figlet_format(str(text), font='graceful'))
    return result


def game_logo(game_type=1):
    """
       Simple logo creator
       :param game_type: one of three game types
       :return: print iteration on the game type
    """
    game_logo = {
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
    for k,v in game_logo.items():
           try:
                  if game_type == k:
                         return [print_image(x) for x in v]

           except:
                  return [print_image(x) for x in game_logo[1]]






# rock_image = print_image("Rock!")
# paper_image = print_image("Paper!")
# scissors_image = print_image("Scissors!")
# lizard_image = print_image("Lizard!")
# spock_image = print_image("Spock!")
# fire_image = print_image("Fire!")
# water_image = print_image("Water!")

game_logo(3)
