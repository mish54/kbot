import requests
from PIL import Image, ImageDraw, ImageFont, ImageColor
from io import BytesIO

def get_person_image(person_equipment):
    """ Funkce pro vytvoreni obrazku pro jednoho hrace. """

    def item_paste(image, x, y, url):
        """ Pomocna funkce pro stazeni obrazku z url adresy a vlozeni do obrazku. """
        response = requests.get(url).content
        subimage = Image.open(BytesIO(response))
        subimage.thumbnail((64, 64))
        image.paste(subimage, (x, y))
        return image

    def get_url_image(item_name, quality):
        """ Pomocna funkce pro ziskani ulr adresy obrazku predmetu. """
        return f'https://gameinfo.albiononline.com/api/gameinfo/items/{item_name}.png?quality={quality}'

    # vytvoreni zakladu
    dest = Image.open("./pictures/gear.png")
    dest = item_paste( dest, 0, 0, get_url_image("T4_2H_DUALSICKLE_UNDEAD@3", 2) )
    return dest

def get_inventory_image(inventory_container):
    pass

get_person_image([]).show()
