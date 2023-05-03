from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import pandas as pd

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


def print_card(image, name, type, project_points=None, grade=None, effect_description=None, action_cost=None, action_description=None, action_steal_points=None, color=color):
    image.text((effect_row, padding), name, font=text, fill=color)

    if not pd.isna(project_points):
        image.text((width - padding - font_size * 2, padding), str(int(project_points)), font=text, fill=color)

    image.text((effect_row, padding + new_line), type, font=text, fill=color)

    if not pd.isna(grade):
        image.text((effect_row, padding + 2 * new_line), grade, font=text, fill=color)

    if not pd.isna(effect_description):
        image.text((effect_row, effect_line), "Effect", font=text, fill=color)
        image.text((effect_row, effect_line + new_line), effect_description, font=text, fill=color)
    if not pd.isna(action_description):
        image.text((effect_row, action_line), "Action", font=text, fill=color)
        image.text((effect_row + 100, action_line), action_cost, font=text, fill=color)
        image.text((effect_row, action_line + new_line), action_description, font=text, fill=color)
        if pd.api.types.is_number(action_steal_points):
            image.text((width - effect_row - font_size * 2, action_line), str(int(action_steal_points)), font=text, fill=color)
        else:
            image.text((width - effect_row - font_size * 2, action_line), action_steal_points, font=text, fill=color)


# MAIN
# Import database
df = pd.read_csv('database.csv')

for index, row in df.iterrows():
    img = Image.open('template/blank-template.png')
    image = ImageDraw.Draw(img)
    # drawings
    if row["type"] == "coin":
        print_card(image=image, name=row["public name"], type=row["type"], color=(0, 0, 0))
    if row["type"] in ("(F) FPGA", "(P) PAT", "(U) Pure", "(Q) QRNG", "(S) Source", "(W) Weak"):
        print_card(image=image, name=row["public name"], type=row["type"], effect_description=row["effect"],
                   project_points=row["project points"], grade=row["grade"], action_cost=row["action cost"], action_description=row["action"], action_steal_points=row["steal points"],
                   color=(0, 0, 0))
    if row["type"] == "professor":
        print_card(image=image, name=row["public name"], type=row["type"], effect_description=row["effect"], color=(50, 0, 0))
    if row["type"] == "item":
        print_card(image=image, name=row["public name"], type=row["type"], effect_description=row["effect"], color=(0, 50, 0))
    if row["type"] == "lab":
        print_card(image=image, name=row["public name"], type=row["type"], effect_description=row["effect"], color=(0, 50, 50))
    # print("cards/TL-S001-ID{:03d}.png".format(row["id"]))
    img.save("cards/TL-S001-ID{:03d}.png".format(row["id"]))

# img.show()
# card name - set - card id
