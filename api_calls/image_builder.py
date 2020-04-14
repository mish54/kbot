import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


def get_images(items, killer, victim, time, gilda_killer, gilda_victim, ip_killer, ip_victim, total_victim_killfame, message):
    dest = Image.open("./misc/gear.png")
    for item in items["Killer"]:
        try:
            response = requests.get(
                f'https://gameinfo.albiononline.com/api/gameinfo/items/{items["Killer"][item]["Type"]}'
            ).content
            img1 = Image.open(BytesIO(response))
            img1.thumbnail((64, 64))
        # TODO: This is a wrong approach (using try except catch for this), devise a way how to do it better
        except TypeError:
            img1 = "Blank"
        # TODO: This whole thing is a duplicity, move to separate function
        if img1 == "Blank":
            pass
        elif item == "Armor":
            dest.paste(img1, (153, 226))
        elif item == "MainHand":
            dest.paste(img1, (63, 241))
        elif item == "OffHand":
            dest.paste(img1, (243, 241))
        elif item == "Head":
            dest.paste(img1, (153, 146))
        elif item == "Shoes":
            dest.paste(img1, (153, 306))
        elif item == "Bag":
            dest.paste(img1, (53, 151))
        elif item == "Cape":
            dest.paste(img1, (253, 151))
        elif item == "Mount":
            dest.paste(img1, (153, 386))
        elif item == "Potion":
            dest.paste(img1, (253, 321))
        elif item == "Food":
            dest.paste(img1, (53, 321))

    for item in items["Victim"]:
        try:
            response = requests.get(
                f'https://gameinfo.albiononline.com/api/gameinfo/items/{items["Victim"][item]["Type"]}'
            ).content
            img1 = Image.open(BytesIO(response))
            img1.thumbnail((64, 64))
        except TypeError:
            img1 = "Blank"

        if img1 == "Blank":
            pass
        elif item == "Armor":
            dest.paste(img1, (828, 226))
        elif item == "MainHand":
            dest.paste(img1, (738, 241))
        elif item == "OffHand":
            dest.paste(img1, (918, 241))
        elif item == "Head":
            dest.paste(img1, (828, 146))
        elif item == "Shoes":
            dest.paste(img1, (828, 306))
        elif item == "Bag":
            dest.paste(img1, (728, 151))
        elif item == "Cape":
            dest.paste(img1, (928, 151))
        elif item == "Mount":
            dest.paste(img1, (828, 386))
        elif item == "Potion":
            dest.paste(img1, (928, 321))
        elif item == "Food":
            dest.paste(img1, (728, 321))
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
