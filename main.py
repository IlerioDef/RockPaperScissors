# This is a sample Python script.

from rps import game_logo, screener, delimeter, show_board

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(screener("  Hello, stranger.  "))
    print(screener("  Please, enter your name  "))
    delimeter()
    name = input("Enter your name:\n")
    delimeter()
    print(screener(f"  Hello, {name}.  "))
    delimeter()
    print(screener("  What game would you like to play?  "))
    print(screener("  1 - Classical RPS  ---"))
    print(screener("  2 - RPS-Spock-Lizard  "))
    print(screener("  3 - RPS-Fire-Water  --"))
    delimeter()
    game_type = int(input("Game type is: \n"))
    try:
        if game_type in {1,2,3}:
            delimeter()
            game_logo(game_type)
        else:
            delimeter()
            print(screener("Wrong game type. Please choose between 1,2 and 3"))
    except:
        delimeter()
        print(screener("Wrong game type!"))
    delimeter()


    score_board = {name:0, "Computer":0}
    show_board(score_board)


