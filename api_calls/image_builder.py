import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


def get_images(items, killer, victim, time, gilda_killer, gilda_victim, ip_killer, ip_victim):
    dest = Image.new("RGB", (640, (len(items["killer"])*64) + 200), "brown")
    height = 0
    for item in items["killer"]:
        response = requests.get(f'https://gameinfo.albiononline.com/api/gameinfo/items/{item}').content
        img1 = Image.open(BytesIO(response))
        img1.thumbnail((64, 64))
        dest.paste(img1, (20, height + 150))
        height += 64

    height = 0

    for item in items["victim"]:
        response = requests.get(f'https://gameinfo.albiononline.com/api/gameinfo/items/{item}').content
        img1 = Image.open(BytesIO(response))
        img1.thumbnail((64, 64))
        dest.paste(img1, (480, height + 150))
        height += 64
    font = ImageFont.truetype("CollegiateBlackFLF.ttf",  20)
    img_draw = ImageDraw.Draw(dest)
    img_draw.text((20, 10), f'Killer: {killer}', fill='white', font=font)
    img_draw.text((380, 10), f'Victim: {victim}', fill='white', font=font)
    img_draw.text((110, 240), f'Server time: {time}', fill='white', font=font)
    img_draw.text((20, 50), f'Gilda: {gilda_killer}', fill='white', font=font)
    img_draw.text((380, 50), f'Gilda: {gilda_victim}', fill='white', font=font)
    img_draw.text((20, 90), f'IP: {ip_killer}', fill='white', font=font)
    img_draw.text((380, 90), f'IP: {ip_victim}', fill='white', font=font)
    arr = BytesIO()
    dest.save(arr, format='PNG')
    arr.seek(0)
    return arr
