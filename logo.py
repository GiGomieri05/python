from PIL import Image, ImageDraw, ImageFont

# Define image size and background color
width, height = 400, 200
background_color = (255, 255, 255)
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)

# Define colors and font
orange_color = (255, 165, 0)
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font_size = 40
font = ImageFont.truetype(font_path, font_size)

# Draw a simple medal
medal_radius = 30
medal_center = (70, height // 2)
draw.ellipse((medal_center[0] - medal_radius, medal_center[1] - medal_radius, medal_center[0] + medal_radius, medal_center[1] + medal_radius), fill=orange_color)

# Draw the text "medalhei"
text = "medalhei"
text_position = (140, height // 2 - font_size // 2)
draw.text(text_position, text, font=font, fill=orange_color)

# Save the image
image_path = "/mnt/data/medalhei_logo.png"
image.save(image_path)

image.show()
image_path
