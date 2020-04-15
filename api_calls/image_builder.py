import requests
from PIL import Image, ImageDraw, ImageFont, ImageColor
from io import BytesIO
import os

def get_image(kill, event_type):
    """ Funkce pro vytvoreni obrazku jednoho killu. """

    def person_subimage(dest_img, person_list, offset_x, offset_y):
        """ Funkce pro vytvoreni zmenu obrazku pro jednu osobu. """
        for item in person_list["Equipment"]:
            try:
                response = requests.get(
                    f'https://gameinfo.albiononline.com/api/gameinfo/items/{person_list["Equipment"][item]["Type"]}?quality={person_list["Equipment"][item]["Quality"]}'
                ).content
                img1 = Image.open(BytesIO(response))
                img1.thumbnail((64, 64))
            # TODO: This is a wrong approach (using try except catch for this), devise a way how to do it better
            except TypeError:
                img1 = "Blank"

            if img1 == "Blank":
                pass
            elif item == "Armor":
                dest_img.paste(img1, (offset_x + 153, offset_y +  80))
            elif item == "MainHand":
                dest_img.paste(img1, (offset_x +  63, offset_y +  95))
            elif item == "OffHand":
                dest_img.paste(img1, (offset_x + 243, offset_y +  95))
            elif item == "Head":
                dest_img.paste(img1, (offset_x + 153, offset_y +   0))
            elif item == "Shoes":
                dest_img.paste(img1, (offset_x + 153, offset_y + 160))
            elif item == "Bag":
                dest_img.paste(img1, (offset_x +  53, offset_y +   5))
            elif item == "Cape":
                dest_img.paste(img1, (offset_x + 253, offset_y +   5))
            elif item == "Mount":
                dest_img.paste(img1, (offset_x + 153, offset_y + 240))
            elif item == "Potion":
                dest_img.paste(img1, (offset_x + 253, offset_y + 175))
            elif item == "Food":
                dest_img.paste(img1, (offset_x +  53, offset_y + 175))
        return dest_img

    dest = Image.open("./misc/gear.png")
    dest = person_subimage(dest, kill["Killer"], 0, 146)
    dest = person_subimage(dest, kill["Victim"], 675, 146)

    font = ImageFont.truetype("./misc/CollegiateBlackFLF.ttf",  20)
    img_draw = ImageDraw.Draw(dest)
    img_draw.text((10, 10), f'Vrah: {kill["Killer"]["Name"]}', fill='white', font=font)
    img_draw.text((778, 10), f'Obet: {kill["Victim"]["Name"]}', fill='white', font=font)

    date = kill["TimeStamp"].split("T")[0]
    time = kill["TimeStamp"].split("T")[1].split(".")[0]
    full_time = str(date) + " " + time
    img_draw.text((300, 10), f'Cas (server): {full_time}', fill='white', font=font)

    img_draw.text((300, 50), f'Fame za zabiti: {kill["TotalVictimKillFame"]}', fill='white', font=font)
    img_draw.text((10, 50), f'Gilda: {kill["Killer"]["GuildName"]}', fill='white', font=font)
    img_draw.text((778, 50), f'Gilda: {kill["Victim"]["GuildName"]}', fill='white', font=font)
    img_draw.text((10, 90), f'IP: {int(kill["Killer"]["AverageItemPower"])}', fill='white', font=font)
    img_draw.text((778, 90), f'IP: {int(kill["Victim"]["AverageItemPower"])}', fill='white', font=font)
    arr = BytesIO()
    dest.save(arr, format='PNG')
    arr.seek(0)
    print("Image built.")
    return arr
