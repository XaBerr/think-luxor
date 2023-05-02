from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Open an Image
img = Image.open('template/blank-template.png')
I1 = ImageDraw.Draw(img)

# parameters
height = 1037
width = 754

font_size = 30
interline = 5
padding = 30
color = (255, 0, 0)
text = ImageFont.truetype('Roboto-Regular.ttf', 30)
new_line = font_size + interline
effect_row = 90
effect_line = 470
action_line = 700

# drawings
I1.text((effect_row, padding), "Name", font=text, fill=color)
I1.text((width - padding - font_size * 2, padding), "99", font=text, fill=color)
I1.text((effect_row, padding + new_line), "Type", font=text, fill=color)
I1.text((effect_row, padding + 2 * new_line), "Grade", font=text, fill=color)
I1.text((effect_row, effect_line), "Effect", font=text, fill=color)
I1.text((effect_row, effect_line + new_line), "aaaaaaaaa", font=text, fill=color)

I1.text((effect_row, action_line), "Action", font=text, fill=color)
I1.text((effect_row + 100, action_line), "(W) (L)", font=text, fill=color)
I1.text((effect_row, action_line + new_line), "aaaaaaaaa", font=text, fill=color)
I1.text((width - effect_row - font_size * 2, action_line), "99", font=text, fill=color)

img.show()
# img.save("cards/test.png")
