from PIL import Image, ImageDraw, ImageFont

image = Image.open(r"IMAGE")

font_type = ImageFont.truetype('arial.ttf', 30)
font_type_2 = ImageFont.truetype('arialbd.ttf', 30)
font_type_3 = ImageFont.truetype('ariali.ttf', 30)

draw = ImageDraw.Draw(image)

draw.text(xy = (50, 50), text = "Text One", fill = (255,69,0), font = font_type)
draw.text(xy = (0, 0), text = "Text Two", fill = (255,69,0), font = font_type_2)
draw.text(xy = (100, 100), text = "Text Three", fill = (255,69,0), font = font_type_3)

image.show()