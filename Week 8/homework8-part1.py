import random

ROWS = 10
COLS = 10


def create_grid():
    return [[random.choice([0, 1]) for _ in range(COLS)] for _ in range(ROWS)]


def display_grid(grid):
    print("\nGeneration:")
    for row in grid:
        print(" ".join("█" if cell == 1 else "." for cell in row))
    print()


def count_neighbors(grid, row, col):
    directions = [-1, 0, 1]
    count = 0

    for dr in directions:
        for dc in directions:
            if dr == 0 and dc == 0:
                continue

            r, c = row + dr, col + dc

            if 0 <= r < ROWS and 0 <= c < COLS:
                count += grid[r][c]

    return count


def next_generation(grid):
    new_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    for i in range(ROWS):
        for j in range(COLS):
            neighbors = count_neighbors(grid, i, j)

            if grid[i][j] == 1:
                if neighbors < 2:
                    new_grid[i][j] = 0  # underpopulation
                elif neighbors in [2, 3]:
                    new_grid[i][j] = 1  # survives
                else:
                    new_grid[i][j] = 0  # overpopulation
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1  # reproduction

    return new_grid


def game_of_life():
    grid = create_grid()

    while True:
        display_grid(grid)

        choice = input("Continue? (y/n): ").lower()
        if choice != "y":
            print("Game stopped.")
            break

        grid = next_generation(grid)


if __name__ == "__main__":
    game_of_life()