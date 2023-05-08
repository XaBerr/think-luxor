from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import pandas as pd
import textwrap

# Open an Image


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


def draw_multiple_line_text(img, xy, text, font, fill):
    draw = ImageDraw.Draw(img)
    image_width, image_height = img.size
    y_text = xy[1]
    lines = textwrap.wrap(text, width=40)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text),
                  line, font=font, fill=fill)
        y_text += line_height


def print_card(img, name, type, project_points=None, grade=None, effect_description=None, action_cost=None, action_description=None, action_steal_points=None, text_color=color):
    draw = ImageDraw.Draw(img)
    draw.text((effect_row, padding), name, font=text, fill=text_color)

    if not pd.isna(project_points):
        draw.text((width - padding - font_size * 2, padding), str(int(project_points)), font=text, fill=text_color)

    draw.text((effect_row, padding + new_line), type, font=text, fill=text_color)

    if not pd.isna(grade):
        draw.text((effect_row, padding + 2 * new_line), grade, font=text, fill=text_color)

    if not pd.isna(effect_description):
        draw_multiple_line_text(img, (effect_row, effect_line), "Effect", font=text, fill=text_color)
        draw_multiple_line_text(img, (effect_row, effect_line + new_line), effect_description, font=text, fill=text_color)
    if not pd.isna(action_description):
        draw_multiple_line_text(img, (effect_row, action_line + new_line), action_description, font=text, fill=text_color)
    if not pd.isna(action_cost):
        draw.text((effect_row, action_line), "Action", font=text, fill=text_color)
        draw.text((effect_row + 100, action_line), action_cost, font=text, fill=text_color)
        if pd.api.types.is_number(action_steal_points):
            draw.text((width - effect_row - font_size * 2, action_line), str(int(action_steal_points)), font=text, fill=text_color)
        else:
            draw.text((width - effect_row - font_size * 2, action_line), action_steal_points, font=text, fill=text_color)


# MAIN
# Import database
df = pd.read_csv('database.csv')

for index, row in df.iterrows():
    # img = Image.open('template/blank-template.png')
    # drawings
    if row["type"] == "coin":
        img = Image.open('template/coin-template.png')
        print_card(img=img, name=row["public name"], type=row["type"], text_color=(0, 0, 0))
    if row["type"] in ("(F) FPGA", "(P) PAT", "(U) Pure", "(Q) QRNG", "(S) Source", "(W) Weak"):
        if row["grade"] == "phd":
            img = Image.open('template/phd-template.png')
        else:
            img = Image.open('template/post-template.png')
        print_card(img=img, name=row["public name"], type=row["type"], effect_description=row["effect"],
                   project_points=row["project points"], grade=row["grade"], action_cost=row["action cost"], action_description=row["action"], action_steal_points=row["steal points"],
                   text_color=(0, 0, 0))
    if row["type"] == "professor":
        img = Image.open('template/prof-template.png')
        print_card(img=img, name=row["public name"], type=row["type"], effect_description=row["effect"], text_color=(90, 0, 0))
    if row["type"] == "item":
        img = Image.open('template/item-template.png')
        print_card(img=img, name=row["public name"], type=row["type"], effect_description=row["effect"], text_color=(0, 90, 0))
    if row["type"] == "lab":
        img = Image.open('template/lab-template.png')
        print_card(img=img, name=row["public name"], type=row["type"], effect_description=row["effect"], text_color=(0, 90, 90))
    # print("cards/TL-S001-ID{:03d}.png".format(row["id"]))
    img.save("cards/TL-S001-ID{:03d}.png".format(row["id"]))

# img.show()
# card name - set - card id
