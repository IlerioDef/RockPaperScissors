from rps import(
    game_logo,
    screener,
    delimiter,
    show_board,
    game_options,
    comp_player,
    win_checker,
    print_image
)

from rich import print


if __name__ == '__main__':
    print(screener("  Hello, stranger.  "))
    print(screener("  Please, enter your name  "))
    delimiter()
    # TODO: можно ввести пустое значение
    name = input("Enter your name:\n")
    score_board = {name: 0, "Computer": 0}
    delimiter()
    while True:
        print(screener(f"  Hello, {name}.  "))
        delimiter()
        print(screener("  What game would you like to play?  "))
        print(screener("  1 - Classical RPS  ---"))
        print(screener("  2 - RPS-Spock-Lizard  "))
        print(screener("  3 - RPS-Fire-Water  --"))
        print(screener("  other - to quit  -----"))
        # TODO: позасрал все своими принтами!
        delimiter()
        # TODO: нет валидации ввода
        game_type = int(input("Game type is: \n"))
        if game_type in {1, 2, 3}:
            delimiter()
            game_logo(game_type)
        else:
            delimiter()
            break
            print(screener("Thank you for playing"))

        while True:

            show_board(score_board)

            print(screener('make your choice:'))

            choices_available = {}
            n = 1
            # TODO: вынести в функцию
            # TODO: использовать enumerate
            # TODO: нормально назвать переменные
            for x in game_options[game_type]:
                choices_available[n] = x
                return_value = f" {n} - {x}  "
                print(screener(return_value))
                n += 1

            try:
                # TODO: не надо так много заворачивать в try/except
                choice = int(input("and your choice is:  "))
                if 1 <= choice <= len(game_options[game_type]):
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
                # TODO: я сначала подумал, что это про уровни в игре какие-то :)
                print("Going one level up!")
                break
