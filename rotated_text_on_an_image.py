from PIL import Image, ImageFont, ImageDraw

text = 'TEST'
font = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 50)
width, height = font.getsize(text)

# Create new image with commented code below

# image1 = Image.new('RGBA', (200, 150), (0, 128, 0, 92))
# draw1 = ImageDraw.Draw(image1)
# draw1.text((0, 0), text=text, font=font, fill=(255, 128, 0))


image1 = Image.open(r'C:\Users\Thoma\OneDrive\Pictures\blank.png')  # Using own image

image2 = Image.new('RGBA', (width, height), (0, 0, 128, 92))
draw2 = ImageDraw.Draw(image2)
draw2.text((0, 0), text=text, font=font, fill=(0, 255, 128))

image2 = image2.rotate(30, expand=1)

px, py = 200, 200
sx, sy = image2.size
image1.paste(image2, (px, py, px + sx, py + sy), image2)

image1.show()
