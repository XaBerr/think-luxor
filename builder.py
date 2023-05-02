from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Open an Image
img = Image.open('template/blank-template.png')
I1 = ImageDraw.Draw(img)
myFont = ImageFont.truetype('Roboto-Regular.ttf', 65)
I1.text((28, 40), "nice Car", font=myFont, fill=(255, 0, 0))
img.show()
# img.save("cards/test.png")
