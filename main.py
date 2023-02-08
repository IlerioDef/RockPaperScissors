# This is a sample Python script.

def screener(data, screen_limit=35):
    if len(data) <= screen_limit:
        string = (str(data)+"_"*(screen_limit-len(data)))
    else:
        string = str(data[:15])

    return string



# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
