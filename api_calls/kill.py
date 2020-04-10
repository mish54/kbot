from api_calls.image_builder import get_images
import api_calls.variables

class Kill:
    """Trida pro zpracovani jedne smrti.

    Attributes
    ----------
    json : list
        json reprezentace killu
    type : int
        typ smrti (0-killer, 1-victim, 2-killer&victim)
    event_id : int
        ID udalosti
    killer : BytesIO
        obrazek vraha a co mel na sobe
    stats : BytesIO
        vykresleni statistiky zucastnenych
    victim : BytesIO
        obrazek obeti a co mel na sobe
    loot : BytesIO
        obrazek inventare
    """

    def __init__(self, json, type):
        self.json = json
        self.type = type
        self.image_init()

    #TODO
    def image_init(self):
        pass

#stats = {}
#killer_items = []
#victim_items = []
#for killer_item in kill["Killer"]["Equipment"]:
#    try:
#        killer_items.append(kill["Killer"]["Equipment"][killer_item]["Type"])
#    except TypeError:
#        pass
#items_dict = {"killer": killer_items}
#for victim_item in kill["Victim"]["Equipment"]:
#    try:
#        victim_items.append(kill["Victim"]["Equipment"][victim_item]["Type"])
#    except TypeError:
#        pass
#items_dict["victim"] = victim_items
#date = kill["TimeStamp"].split("T")[0]
#time = kill["TimeStamp"].split("T")[1].split(".")[0]
#stats["Gdy_se_to_stalo"] = date + " " + time
#self.kills_to_print.append(i["EventId"])
#image = get_images(items_dict,
#                  kill["Killer"]["Name"],
#                  kill["Victim"]["Name"],
#                  stats["Gdy_se_to_stalo"],
#                  kill["Killer"]["GuildName"],
#                  kill["Victim"]["GuildName"],
#                  kill["Killer"]["AverageItemPower"],
#                  kill["Victim"]["AverageItemPower"]
#                  )
#return image
