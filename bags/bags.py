from PIL import Image, ImageDraw
import random
import sys

CELL_EMPTY = 0
CELL_BLOCKED = 1
CELL_START = 2
CELL_GOAL = 3
CELL_BLOCK_RATE = 1.5 / 9 # based on examples

def gen_grid_data(grid_size):
    expected_num_blocks = grid_size * grid_size * CELL_BLOCK_RATE
    min_num_blocks = int(expected_num_blocks)
    max_num_blocks = min_num_blocks + 1
    if random.random() < 0.5:
        num_blocks = max_num_blocks
    else:
        num_blocks = min_num_blocks

    grid_data = []
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            row.append(CELL_EMPTY)
        grid_data.append(row)

    # Place blocks
    for _ in range(num_blocks):
        i = random.randint(0, grid_size - 1)
        j = random.randint(0, grid_size - 1)
        grid_data[i][j] = CELL_BLOCKED

    # Place start and goal
    goal_placed = False
    while not goal_placed:
        i = random.randint(0, grid_size - 1)
        j = random.randint(0, grid_size - 1)
        if grid_data[i][j] == CELL_EMPTY:
            grid_data[i][j] = CELL_GOAL
            goal_placed = True

    start_placed = False
    while not start_placed:
        i = random.randint(0, grid_size - 1)
        j = random.randint(0, grid_size - 1)
        if grid_data[i][j] == CELL_EMPTY:
            grid_data[i][j] = CELL_START
            start_placed = True
    
    return grid_data

PIXELS_PER_CELL = 140
BORDER_WIDTH_PIXELS = 8

def make_grid(grid_size):
    grid_data = gen_grid_data(grid_size)

    # Create a new image
    img = Image.new('RGB', (PIXELS_PER_CELL * grid_size, PIXELS_PER_CELL * grid_size), color = (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Fill in the cells
    for i in range(grid_size):
        for j in range(grid_size):
            if grid_data[i][j] == CELL_BLOCKED:
                fill = 'black'
            elif grid_data[i][j] == CELL_START:
                fill = 'blue'
            elif grid_data[i][j] == CELL_GOAL:
                fill = 'yellow'
            else:
                continue
            draw.rectangle((PIXELS_PER_CELL * j + BORDER_WIDTH_PIXELS, PIXELS_PER_CELL * i + BORDER_WIDTH_PIXELS, PIXELS_PER_CELL * (j + 1) - BORDER_WIDTH_PIXELS, PIXELS_PER_CELL * (i + 1) - BORDER_WIDTH_PIXELS), fill=fill)

    # Draw the borders
    for i in range(1, grid_size):
        draw.line((PIXELS_PER_CELL * i, 0, PIXELS_PER_CELL * i, PIXELS_PER_CELL * grid_size), fill='gray', width=BORDER_WIDTH_PIXELS)
        draw.line((0, PIXELS_PER_CELL * i, PIXELS_PER_CELL * grid_size, PIXELS_PER_CELL * i), fill='gray', width=BORDER_WIDTH_PIXELS)

    return img

IMG_GAP_PIXELS = 20

def draw_side_by_side(left_img, right_img):
    # Create a new image
    img = Image.new('RGB', (left_img.width + IMG_GAP_PIXELS + right_img.width, left_img.height), color = (0, 0, 0))

    # Paste the images side by side
    img.paste(left_img, (0, 0))
    img.paste(right_img, (left_img.width + IMG_GAP_PIXELS, 0))

    img.show()

if __name__ == '__main__':
    grid_size = 7 if len(sys.argv) < 2 else int(sys.argv[1])
    left_img = make_grid(grid_size)
    right_img = make_grid(grid_size)
    draw_side_by_side(left_img, right_img)
