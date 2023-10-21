from PIL import Image, ImageDraw, ImageFont

# Size of your webcam feed
width, height = 1024, 576

# Create a new image with RGBA channels
img = Image.new('RGBA', (width, height), (0, 0, 0, 0))

# Create a draw object
draw = ImageDraw.Draw(img)

# Define the size of the border
border_width = 10

# Draw four rectangles to make a border
draw.rectangle([0, 0, width, border_width], fill=(255,0,0,128)) # Top border
draw.rectangle([0, height - border_width, width, height], fill=(255,0,0,128)) # Bottom border
draw.rectangle([0, 0, border_width, height], fill=(255,0,0,128)) # Left border
draw.rectangle([width - border_width, 0, width, height], fill=(255,0,0,128)) # Right border

# Add a title
font = ImageFont.truetype("arial.ttf", 50) # You may need to provide the full path to the font file in your system
draw.text((width//2 - 100, 10), "Badestjuju", fill=(255,255,255), font=font)

# Add a watermark at the bottom right corner
font = ImageFont.truetype("arial.ttf", 20)
draw.text((width - 200,height - 30), "Let's ", fill=(255,255,255), font=font)

# Save the image
img.save('overlay.png')