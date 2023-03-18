from rps import (
    game_logo,
    screener,
    delimiter,
    show_board,
    GAME_OPTIONS,
    comp_player,
    win_checker,
    print_image, input_validator
)

if __name__ == '__main__':
    print("Hello, stranger")
    print("  Please, enter your name  ")
    delimiter()
    name = input_validator(input("Enter your name:\n"))
    score_board = {name: 0, "Computer": 0}
    delimiter()

    # Main menu
    while True:
        print(f"  Hello, {name}.  ")
        print("  What game would you like to play?  ")
        for k, v in enumerate(GAME_OPTIONS.values(), start=1):
            v = " ".join(v)
            print(f"{k} - {v}")
        print("Or any other key to quit.")

        delimiter()

    # Game starts

        game_type = int(input_validator(input("Game type is: \n")))
        if game_type in GAME_OPTIONS:
            delimiter()
            game_logo(game_type)
        else:
            delimiter()
            print("Thank you for playing")
            break

        while True:
            show_board(score_board)
            print('make your choice:')

            choices_available = {}
            n = 1
            # TODO: вынести в функцию
            # TODO: использовать enumerate
            # TODO: нормально назвать переменные
            for x in GAME_OPTIONS[game_type]:
                choices_available[n] = x
                return_value = f"{n} - {x}"
                print(return_value)
                n += 1

            try:
                # TODO: не надо так много заворачивать в try/except
                choice = int(input("and your choice is:  "))
                if 1 <= choice <= len(GAME_OPTIONS[game_type]):
                    comp_choice = comp_player(game_type)
                    x = win_checker(player1=choice, player2=comp_choice, game_type=game_type)
                    print(f"your choice was:")
                    print_image(choices_available[choice])
                    print(f"Computer chose:")
                    print_image(choices_available[comp_choice])

                    if x == 1:
                        print(screener(f"  Player{x} won!  "))
                        score_board[name] += 1
                    elif x == 0:
                        print(screener(f"  Tie!  "))
                        continue
                    else:
                        print(screener(f"  Player{x} won!  "))
                        score_board["Computer"] += 1

                else:
                    raise ValueError
            except ValueError:
                print("Going to main menu")
                break
