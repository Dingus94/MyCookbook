from PIL import Image, ImageFont, ImageDraw, ImageOps

text = 'TEST'
font = ImageFont.truetype(r'C:\Windows\Fonts\Arialbd.ttf', 50)
width, height = font.getsize(text)

image1 = Image.open(r'C:\Users\Thoma\OneDrive\Pictures\testimage.jpg')  # Using own image

image2 = Image.new('RGBA', (width, height), (0, 0, 0, 255))
draw2 = ImageDraw.Draw(image2)
draw2.text((0, 0), text=text, font=font, fill=(162, 64, 63), align='center')

image2 = image2.rotate(4.4, expand=1)

px, py = 200, 500
sx, sy = image2.size
image1.paste(image2, (px, py, px + sx, py + sy), image2)

# Pasting a rotated image with mask
# size = (256, 256)
# mask = Image.new('L', size, 0)
# draw = ImageDraw.Draw(mask)
# draw.ellipse((0, 0) + size, fill=255)
# offset = 150, 222
# im = Image.open(r'C:\Users\Thoma\OneDrive\Pictures\testimage2.jpeg')
#
# output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
# output.putalpha(mask)
#
# image1.paste(output, offset, mask)
#
image1.show()
