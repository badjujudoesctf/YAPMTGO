from PIL import Image, ImageDraw, ImageFont

# Create a new image with the specified size and background color
image = Image.new("RGB", (1024, 576), (0, 0, 255))

# Create a new drawing context
draw = ImageDraw.Draw(image)

# Draw a rectangle with the specified fill color
draw.rectangle((0, 0, 1024, 576), fill=(128, 0, 128))

# Set the font size and type
font = ImageFont.truetype("arial.ttf", 36)

# Draw text on the image
draw.text((10, 10), "Hello World!", font=font, fill=(255, 192, 203))

# Save the image to a file
image.save("overlayNextGeneration.png")