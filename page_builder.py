from PIL import Image
import math


image_ref = Image.open('cards/TL-S001-ID001.png')
card_size = image_ref.size

current_page = 0
last_card = 12
for ii in range(1, last_card + 1):
    in_page_position = (ii - 1) % 9
    if in_page_position == 0:
        new_image = Image.new('RGB', (card_size[0] * 3, card_size[1] * 3), (250, 250, 250))

    image1 = Image.open('cards/TL-S001-ID{:03d}.png'.format(ii))
    new_image.paste(image1, (card_size[0] * (in_page_position % 3), card_size[1] * math.floor(in_page_position / 3)))

    if in_page_position == 8 or ii == (last_card):
        current_page = current_page + 1
        new_image.save("pages/page-{:04d}.png".format(current_page))
        # new_image = Image.new('RGB', (card_size[0] * 3, card_size[1] * 3), (250, 250, 250))
