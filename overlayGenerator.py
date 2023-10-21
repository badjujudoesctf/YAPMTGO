__author__ = "Julien Badjuju Losier"
__copyright__ = "Copyright (C) 2023 Julien Losier"
__license__ = "GNU GPLv3"
__version__ = "1.0"

from PIL import Image, ImageDraw, ImageFont

# Size of your webcam feed
width, height = 1024, 576

# Path of the FontsBauhs93.ttf (Windows 11 22H2 has it by default)
fontsBauhs93 = r"C:\\Windows\\Fonts\\Bauhs93.ttf"

# Create a new image with RGBA channels
img = Image.new("RGBA", (width, height), (0, 0, 0, 0))

# Create a new drawing context
draw = ImageDraw.Draw(img)

# Define the size of the border
border_width = 10  ## user editable value <<<<<

# Draw four rectangles to make a border
draw.rectangle(
    [0, 0, border_width, height], fill=(0, 102, 255)
)  # Left border| fill is a user editable value <<<<<
draw.rectangle(
    [0, 0, width, border_width], fill=(204, 102, 255)
)  # Top border| fill is a user editable value <<<<<
draw.rectangle(
    [width - border_width, 0, width, height], fill=(255, 102, 153)
)  # Right| fill is a user editable value <<<<<

# Draw the rainbow at the bottom
rainbow_colors = [
    (153, 0, 51),
    (255, 153, 0),
    (255, 204, 0),
    (0, 153, 51),
    (0, 102, 255),
    (75, 0, 130),
    (204, 102, 255),
]
rainbow_width = int(1024 / len(rainbow_colors))
for i in range(len(rainbow_colors)):
    draw.rectangle(
        (i * rainbow_width, 556, (i + 1) * rainbow_width - 1, 576),
        fill=rainbow_colors[i],
    )

# Add a title | fill is a user editable value <<<<< | You can modify the font used too if you edit the variable first
font = ImageFont.truetype(fontsBauhs93, 50)
draw.text((width // 2 - 100, 10), "Your title here", fill=(153, 0, 51), font=font)

# Add a watermark at the bottom right corner | fill is a user editable value <<<<< | You can modify the font used too if you edit the variable first
font = ImageFont.truetype(fontsBauhs93, 20)
draw.text(
    (width - 576, height - 20), "Your watermark here", fill=(255, 255, 255), font=font
)

# Save the image to a file
img.save("overlay.png")
