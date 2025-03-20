import os
import random
import time
import numpy as np

# Get the size of the terminal window.;
CONSOLE_WIDTH, CONSOLE_HEIGHT = os.get_terminal_size()

# Subtract 1 from both dimensions to avoid issues with boundary rendering:
# - Many terminals wrap text to the next  line  if  you  print  exactly  at  the
#   rightmost column.
# - Printing to the very bottom row can sometimes cause unexpected scrolling  or
#   flicker.
# Reducing the width and height by 1 ensures we  stay  within  safe  boundaries,
# leading to smoother rendering and preventing visual glitches at the edges.
CONSOLE_WIDTH -= 1
CONSOLE_HEIGHT -= 1

ALIVE_CELL_SYMBOL = "●"
ALIVE_CELL_COLOR = "\033[32m"
DEAD_CELL_SYMBOL = " "
DEAD_CELL_COLOR = ""

GAME_CYCLE_THRESHOLD = 5
GAME_STARTING_DENSITY = 15


def count_neighbors(arr, y, x) -> int:
    count = 0
    height, width = arr.shape

    # All 8 directions (dy, dx).
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dy, dx in directions:
        nx = x + dx  # Row.
        ny = y + dy  # Height.

        # Check if the coordinates are within bounds.
        if not (0 <= ny < height and 0 <= nx < width):
            continue

        if arr[ny, nx] == 1:
            count += 1

    return count


if __name__ == "__main__":
    # Hides the cursor.
    print("\033[?25l", end="")

    screen = np.zeros((CONSOLE_HEIGHT, CONSOLE_WIDTH), dtype=int)
    screen_queue = []

    # Populate the screen.
    for y in range(CONSOLE_HEIGHT):
        for x in range(CONSOLE_WIDTH):
            if random.random() < GAME_STARTING_DENSITY / 100:
                screen[y, x] = 1

    while True:
        # Render screen
        os.system("cls" if os.name == "nt" else "clear")
        for y in range(CONSOLE_HEIGHT):
            for x in range(CONSOLE_WIDTH):
                print(f"{ALIVE_CELL_COLOR}{ALIVE_CELL_SYMBOL}\033[0m" if screen[y, x] == 1 else f"{DEAD_CELL_COLOR}{DEAD_CELL_SYMBOL}\033[0m", end="")
            print()

        time.sleep(0.02)

        # Copy the current screen  to  calculate  the  next  generation  without
        # accidentally mixing old and new states during updates.
        next_screen = np.copy(screen)

        for y in range(CONSOLE_HEIGHT):
            for x in range(CONSOLE_WIDTH):
                alive = screen[y, x] == 1
                neighbors_count = count_neighbors(screen, y, x)
                if alive and neighbors_count < 2:
                    next_screen[y, x] = 0
                elif alive and neighbors_count in (2, 3):
                    next_screen[y, x] = 1
                elif alive and neighbors_count > 3:
                    next_screen[y, x] = 0
                elif not alive and neighbors_count == 3:
                    next_screen[y, x] = 1

        # If the current screen is identical to the next screen, no changes  are
        # happening, so the game has reached a stable state  ("GAME  OVER").  If
        # the current screen matches any of  the  previous  screens  stored,  it
        # means the pattern has entered a loop so the game ends.
        if np.array_equal(screen, next_screen):
            print("GAME OVER!")
            break
        elif any(np.array_equal(screen, history_screen) for history_screen in screen_queue):
            print("GAME OVER!")
            break

        if len(screen_queue) <= GAME_CYCLE_THRESHOLD:
            screen_queue.append(screen)
        else:
            _ = screen_queue.pop(0)

        # Assign the screen
        screen = next_screen
