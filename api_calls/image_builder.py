import requests
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO


def get_images(items, killer, victim, time, gilda_killer, gilda_victim, ip_killer, ip_victim):
    dest = Image.new("RGB", (384, (len(items["killer"])*64) + 60), "brown")
    height = 0
    for item in items["killer"]:
        response = requests.get(f'https://gameinfo.albiononline.com/api/gameinfo/items/{item}').content
        img1 = Image.open(BytesIO(response))
        img1.thumbnail((64, 64))
        dest.paste(img1, (20, height + 40))
        height += 64

    height = 0

    for item in items["victim"]:
        response = requests.get(f'https://gameinfo.albiononline.com/api/gameinfo/items/{item}').content
        img1 = Image.open(BytesIO(response))
        img1.thumbnail((64, 64))
        dest.paste(img1, (274, height + 40))
        height += 64

    img_draw = ImageDraw.Draw(dest)
    img_draw.text((20, 0), f'Killer: {killer}', fill='white')
    img_draw.text((274, 0), f'Victim: {victim}', fill='white')
    img_draw.text((94, 80), f'Server time: {time}', fill='white')
    img_draw.text((20, 10), f'Gilda: {gilda_killer}', fill='white')
    img_draw.text((274, 10), f'Gilda: {gilda_victim}', fill='white')
    img_draw.text((20, 20), f'IP: {ip_killer}', fill='white')
    img_draw.text((274, 20), f'IP: {ip_victim}', fill='white')
    return dest
