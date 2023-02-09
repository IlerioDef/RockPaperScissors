import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

def print_image(text):
       result = cprint(figlet_format(text, font='graceful'),
       'yellow', 'on_red', attrs=['bold'])
       return result

rock_image = print_image("Rock!")
paper_image = print_image("Paper!")
scissors_image = print_image("Scissors!")
lizard_image = print_image("Lizard!")
spock_image = print_image("Spock!")
fire_image = print_image("Fire!")
water_image = print_image("Water!")



