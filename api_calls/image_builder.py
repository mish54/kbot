import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


def get_images(items, killer, victim, time, gilda_killer, gilda_victim, ip_killer, ip_victim, total_victim_killfame, message):
    dest = Image.open("./misc/gear.png")
    height = 0
    for item in items["Killer"]:
        try:
            response = requests.get(
                f'https://gameinfo.albiononline.com/api/gameinfo/items/{items["Killer"][item]["Type"]}'
            ).content
            img1 = Image.open(BytesIO(response))
            img1.thumbnail((64, 64))
        except TypeError:
            pass

        if item == "Armor":
            dest.paste(img1, (153, 85 + 141))
        elif item == "MainHand":
            dest.paste(img1, (63, 100 + 141))
        elif item == "OffHand":
            dest.paste(img1, (243, 100 + 141))
        elif item == "Head":
            dest.paste(img1, (153, 5 + 141))
        elif item == "Shoes":
            dest.paste(img1, (153, 165 + 141))
        elif item == "Bag":
            dest.paste(img1, (53, 10 + 141))
        elif item == "Cape":
            dest.paste(img1, (253, 10 + 141))
        elif item == "Mount":
            dest.paste(img1, (153, 245 + 141))
        elif item == "Potion":
            dest.paste(img1, (253, 180 + 141))
        elif item == "Food":
            dest.paste(img1, (53, 180 + 141))

    for item in items["Victim"]:
        try:
            response = requests.get(
                f'https://gameinfo.albiononline.com/api/gameinfo/items/{items["Killer"][item]["Type"]}'
            ).content
            img1 = Image.open(BytesIO(response))
            img1.thumbnail((64, 64))
        except TypeError:
            pass

        if item == "Armor":
            dest.paste(img1, (150 + 678, 85 + 141))
        elif item == "MainHand":
            dest.paste(img1, (60 + 678, 100 + 141))
        elif item == "OffHand":
            dest.paste(img1, (240 + 678, 100 + 141))
        elif item == "Head":
            dest.paste(img1, (150 + 678, 5 + 141))
        elif item == "Shoes":
            dest.paste(img1, (150 + 678, 165 + 141))
        elif item == "Bag":
            dest.paste(img1, (50 + 678, 10 + 141))
        elif item == "Cape":
            dest.paste(img1, (250 + 678, 10 + 141))
        elif item == "Mount":
            dest.paste(img1, (150 + 678, 245 + 141))
        elif item == "Potion":
            dest.paste(img1, (250 + 678, 180 + 141))
        elif item == "Food":
            dest.paste(img1, (50 + 678, 180 + 141))
    font = ImageFont.truetype("./misc/CollegiateBlackFLF.ttf",  20)
    img_draw = ImageDraw.Draw(dest)
    img_draw.text((10, 10), f'Vrah: {killer}', fill='white', font=font)
    img_draw.text((778, 10), f'Obet: {victim}', fill='white', font=font)
    img_draw.text((300, 10), f'Cas (server): {time}', fill='white', font=font)
    img_draw.text((300, 50), f'Fame za zabiti: {total_victim_killfame}', fill='white', font=font)
    img_draw.text((300, 90), f'{message}', fill='white', font=font)
    img_draw.text((10, 50), f'Gilda: {gilda_killer}', fill='white', font=font)
    img_draw.text((778, 50), f'Gilda: {gilda_victim}', fill='white', font=font)
    img_draw.text((10, 90), f'IP: {ip_killer}', fill='white', font=font)
    img_draw.text((778, 90), f'IP: {ip_victim}', fill='white', font=font)
    arr = BytesIO()
    dest.save(arr, format='PNG')
    arr.seek(0)
    return arr
