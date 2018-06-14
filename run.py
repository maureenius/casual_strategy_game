from game import Game

import random

def main(env_name):
    SAVE_PATH = "./save/" + env_name
    MAP_SIZE = 30
    NUM_CAMP = 10
    
    main_game = Game(MAP_SIZE, NUM_CAMP)

    while not main_game.isFinished():
        main_game.process()
        main_game.draw()
    
    print("最強陣営：" + str(main_game.who_is_strongest()))

if __name__ == "__main__":
    env_name = "tactics"
    main(env_name)