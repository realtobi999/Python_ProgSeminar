import os
import random
import time
import keyboard
import iridis

BOARD_WIDTH = 20
BOARD_HEIGHT = 10
PLAYER_SYMBOL = "O"
FOOD_SYMBOL = f"{iridis.Color.RED.value}X{iridis.Color.RESET.value}"
PLAYER_POS = (6, 2)
FOOD_POS = (7, 7)
SCORE = 0
DELAY = 0.1
GAME_OVER = False


def generate_screen():
    """
    Generates an empty game screen with the defined board dimensions.

    :return: A 2D list representing the game screen with empty spaces.
    """
    return [[" " for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]


def render_screen(screen):
    """
    Renders the current state of the game screen, including the player and food positions.

    :param screen: A 2D list representing the game screen.
    :return: None
    """
    print("X" + "-" * BOARD_WIDTH + "X")
    for y, row in enumerate(screen):
        line = "|"
        for x, _ in enumerate(row):
            px, py = PLAYER_POS
            fx, fy = FOOD_POS
            if (x, y) == (px, py):
                line += PLAYER_SYMBOL
            elif (x, y) == (fx, fy):
                line += FOOD_SYMBOL
            else:
                line += " "
        print(line + "|")
    print("X" + "-" * BOARD_WIDTH + "X")


def generate_food(screen):
    """
    Generates a new food position on the game screen and updates its location.

    :param screen: A 2D list representing the game screen.
    :return: None
    """
    global FOOD_POS

    screen[FOOD_POS[1]][FOOD_POS[0]] = " "
    FOOD_POS = (random.randint(0, BOARD_WIDTH - 1), random.randint(0, BOARD_HEIGHT - 1))
    screen[FOOD_POS[1]][FOOD_POS[0]] = FOOD_SYMBOL


def move_player(screen, direction):
    """
    Moves the player in the specified direction on the game screen.

    :param screen: A 2D list representing the game screen.
    :param direction: The direction to move the player ('up', 'down', 'left', 'right').
    :return: None
    """
    global PLAYER_POS

    screen[PLAYER_POS[1]][PLAYER_POS[0]] = " "
    px, py = PLAYER_POS

    if direction == "up":
        py -= 1
    elif direction == "down":
        py += 1
    elif direction == "left":
        px -= 1
    elif direction == "right":
        px += 1

    if py < 0 or py > BOARD_HEIGHT - 1:
        py = PLAYER_POS[1]
    elif px < 0 or px > BOARD_WIDTH - 1:
        px = PLAYER_POS[0]

    PLAYER_POS = (px, py)
    screen[py][px] = PLAYER_SYMBOL


def run_game():
    """
    Runs the main game loop, handling screen rendering, player movement, and game logic.

    :return: None
    """
    global GAME_OVER, SCORE

    screen = generate_screen()
    screen[PLAYER_POS[1]][PLAYER_POS[0]] = PLAYER_SYMBOL
    screen[FOOD_POS[1]][FOOD_POS[0]] = FOOD_SYMBOL

    while not GAME_OVER:
        time.sleep(DELAY)
        os.system("clear" if os.name == "posix" else "cls")
        print("Použijte klávesy W, A, S, D pro pohyb. Stiskněte E pro ukončení.")
        render_screen(screen)
        if keyboard.is_pressed("w"):
            move_player(screen, "up")
        if keyboard.is_pressed("s"):
            move_player(screen, "down")
        if keyboard.is_pressed("a"):
            move_player(screen, "left")
        if keyboard.is_pressed("d"):
            move_player(screen, "right")
        if keyboard.is_pressed("e"):
            GAME_OVER = True
        if PLAYER_POS == FOOD_POS:
            generate_food(screen)
            SCORE += 1
        print(f"Skóre: {SCORE}")


if __name__ == "__main__":
    run_game()
