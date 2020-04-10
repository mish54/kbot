import requests
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

items = {"killer": ['T5_MAIN_RAPIER_MORGANA@1', 'T5_OFF_HORN_KEEPER@1', 'T4_HEAD_LEATHER_MORGANA@2', 'T4_ARMOR_LEATHER_MORGANA@3', 'T5_SHOES_LEATHER_SET2@1', 'T4_CAPEITEM_UNDEAD', 'T3_MOUNT_HORSE', 'T6_POTION_COOLDOWN', 'T7_MEAL_OMELETTE'],
         "victim": ['T5_MAIN_RAPIER_MORGANA@1', 'T5_OFF_HORN_KEEPER@1', 'T5_HEAD_LEATHER_MORGANA@2', 'T7_ARMOR_LEATHER_MORGANA@3', 'T6_SHOES_LEATHER_SET2@1', 'T4_CAPEITEM_UNDEAD', 'T3_MOUNT_HORSE', 'T6_POTION_COOLDOWN', 'T7_MEAL_OMELETTE']
         }


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
    img_draw.text((130, 240), f'Server time: {time}', fill='white', font=font)
    img_draw.text((20, 50), f'Gilda: {gilda_killer}', fill='white', font=font)
    img_draw.text((380, 50), f'Gilda: {gilda_victim}', fill='white', font=font)
    img_draw.text((20, 90), f'IP: {ip_killer}', fill='white', font=font)
    img_draw.text((380, 90), f'IP: {ip_victim}', fill='white', font=font)
    dest.save("imageee.png")



get_images(items, "jouda", "druhej jouda", "24.4.2020 11:20", "Moc a Slava", "Kriplove", "1000", "10")
