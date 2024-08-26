from PIL import Image, ImageDraw, ImageFont
import random

colors = [
    ("Red", (255, 0, 0)),
    ("Orange", (255, 165, 0)),
    ("Yellow", (255, 255, 0)),
    ("Green", (0, 255, 0)),
    ("Teal", (0, 255, 255)),
    ("Blue", (0, 0, 255)),
    ("Violet", (134, 1, 175)),
]

# create an image large enough to fit three words
width = 900
height = 100
image = Image.new("RGB", (width, height))

# fill black
image.putdata([(0, 0, 0)] * (width * height))

# pick three colors
picked = random.sample(colors, 3)
picked_words = [color[0] for color in picked]
# remove what we picked from the pool
for color in picked:
    colors = [c for c in colors if c != color]
assert(len(colors) == 4)

# repeat
picked = random.sample(colors, 3)
picked_colors = [color[1] for color in picked]
for color in picked:
    colors = [c for c in colors if c != color]

assert(len(colors) == 1)

# draw the words
draw = ImageDraw.Draw(image)
for i in range(3):
    word = picked_words[i]
    color = picked_colors[i]
    x = i * width // 3
    font_size = 70
    font = ImageFont.truetype("arialbd.ttf", font_size)
    draw.text((x, 5), word, font=font, fill=color)

# show the image
image.show()
