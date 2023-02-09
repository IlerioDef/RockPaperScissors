import sys

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

rock_image = print_image("Rock!")
paper_image = print_image("Paper!")
scissors_image = print_image("Scissors!")
lizard_image = print_image("Lizard!")
spock_image = print_image("Spock!")
fire_image = print_image("Fire!")
water_image = print_image("Water!")






# rock_image = print_image("Rock!")
# paper_image = print_image("Paper!")
# scissors_image = print_image("Scissors!")
# lizard_image = print_image("Lizard!")
# spock_image = print_image("Spock!")
# fire_image = print_image("Fire!")
# water_image = print_image("Water!")

game_logo(3)
