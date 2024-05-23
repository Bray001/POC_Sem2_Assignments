grid = [
    ["-", "-", "-"]
    ["-", "-", "-"]
    ["-", "-", "-"]
]

def print_grid():
    for number in  range (grid.count()):
        print(grid[number][0], end="")
        print( "|", end="")
        print(grid[number][1], end="")
        print("|", end="")
        print(grid[number][2])
        if(number != 2):
            print("*****")
        


def game_intro():
    print('Welcome to TIC-TAC-TOE!!')


def game_loop():

    game_intro()


    while(True):
        print_grid()
        user_request = input("Enter STOP to end the game, or anything else to continue.")
        if user_request.__eq__("STOP"):
            break
        print("Loop running!")

    print("Game Over")

game_loop()