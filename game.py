import TTT_env
from TTT_env import Board

def main():

    while True:

        table = Board()

        while not table.game_over() or not table.end:

            table.render()

        if table.end:
            break

if __name__ == '__main__':
    main()