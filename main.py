from rps import (
    game_logo,
    delimiter,
    show_board,
    GAME_OPTIONS,
    comp_player,
    win_checker,
    print_image, input_validator
)
from rich import print as rprint

if __name__ == '__main__':
    rprint("Hello, stranger")
    rprint("  Please, enter your name  ")
    delimiter()
    name = input_validator(input("Enter your name:\n"))
    score_board = {name: 0, "Computer": 0}
    delimiter()

    # Main menu
    while True:
        rprint(f"  Hello, {name}.  ")
        rprint("  What game would you like to play?  ")
        for k, v in enumerate(GAME_OPTIONS.values(), start=1):
            v = " ".join(v)
            rprint(f"{k} - {v}")
        rprint("Or any other key to quit.")

        delimiter()

    # Game starts

        game_type = int(input_validator(input("Game type is: \n")))
        if game_type in GAME_OPTIONS:
            delimiter()
            game_logo(game_type)
        else:
            delimiter()
            rprint("Thank you for playing")
            break

        while True:
            show_board(score_board)
            rprint('make your choice:')

            choices_available = {}
            counter = 1
            # TODO: вынести в функцию
            # TODO: использовать enumerate
            for option in GAME_OPTIONS[game_type]:
                choices_available[counter] = option
                return_value = f"{counter} - {option}"
                rprint(return_value)
                counter += 1

            try:
                # TODO: не надо так много заворачивать в try/except
                choice = int(input("and your choice is:  "))
                if 1 <= choice <= len(GAME_OPTIONS[game_type]):
                    comp_choice = comp_player(game_type)
                    x = win_checker(player1=choice, player2=comp_choice, game_type=game_type)
                    rprint(f"your choice was:")
                    print_image(choices_available[choice])
                    rprint(f"Computer chose:")
                    print_image(choices_available[comp_choice])

                    if x == 1:
                        rprint(f"  Player{x} won!  ")
                        score_board[name] += 1
                    elif x == 0:
                        rprint(f"  Tie!  ")
                        continue
                    else:
                        rprint(f"  Player{x} won!  ")
                        score_board["Computer"] += 1

                else:
                    raise ValueError
            except ValueError:
                rprint("Going to main menu")
                break
