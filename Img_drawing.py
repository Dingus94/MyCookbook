from PIL import Image, ImageDraw, ImageFont

image = Image.open(r"C:\Users\Thoma\OneDrive\Pictures\hornyjail.png")

font_type = ImageFont.truetype('arialbd.ttf', 60)

draw = ImageDraw.Draw(image)

draw.text(xy = (975, 650), text = "My Cool Bot", fill = (0,0,0), font = font_type)

image.show()