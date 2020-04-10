import aiohttp
from aiohttp.client_exceptions import ClientConnectionError
import io
from json import JSONDecodeError
import json

from api_calls.image_builder import get_images
import api_calls.variables

class Kills:
	def __init__(self):
		self.kills_to_print = []
		self.last_kill_id = -1

	@staticmethod
	async def fetch(session, url):
		async with session.get(url) as response:
			return await response.text()

	async def main(self):
		async with aiohttp.ClientSession() as session:
			try:
				html = await Kills.fetch(session,
				                         'https://gameinfo.albiononline.com/api/gameinfo/events?limit=51&offset=0')
			except:
				print("Client exception error, continuing...")
				pass

			try:
				json_out = json.loads(html)
				for kill in json_out:
					if kill["Killer"]["GuildId"] is GUILD_ID and kill["EventId"] not in self.kills_to_print:
						print("We have a killer")
						stats = {}
						killer_items = []
						victim_items = []
						for killer_item in kill["Killer"]["Equipment"]:
							try:
								killer_items.append(kill["Killer"]["Equipment"][killer_item]["Type"])
							except TypeError:
								pass
						items_dict = {"killer": killer_items}
						for victim_item in kill["Victim"]["Equipment"]:
							try:
								victim_items.append(kill["Victim"]["Equipment"][victim_item]["Type"])
							except TypeError:
								pass
						items_dict["victim"] = victim_items
						date = kill["TimeStamp"].split("T")[0]
						time = kill["TimeStamp"].split("T")[1].split(".")[0]
						stats["Gdy_se_to_stalo"] = date + " " + time
						self.kills_to_print.append(i["EventId"])
						image = get_images(items_dict,
						                  kill["Killer"]["Name"],
						                  kill["Victim"]["Name"],
						                  stats["Gdy_se_to_stalo"],
						                  kill["Killer"]["GuildName"],
						                  kill["Victim"]["GuildName"],
						                  kill["Killer"]["AverageItemPower"],
						                  kill["Victim"]["AverageItemPower"]
						                  )
						return image

					elif kill["Victim"]["GuildId"] is GUILD_ID and kill["EventId"] not in self.kills_to_print:
						print("We have a victim")
						stats = {}
						killer_items = []
						victim_items = []
						for killer_item in kill["Killer"]["Equipment"]:
							try:
								killer_items.append(kill["Killer"]["Equipment"][killer_item]["Type"])
							except TypeError:
								pass
						items_dict = {"killer": killer_items}
						for victim_item in kill["Victim"]["Equipment"]:
							try:
								victim_items.append(kill["Victim"]["Equipment"][victim_item]["Type"])
							except TypeError:
								pass
						items_dict["victim"] = victim_items
						date = kill["TimeStamp"].split("T")[0]
						time = kill["TimeStamp"].split("T")[1].split(".")[0]
						stats["Gdy_se_to_stalo"] = date + " " + time
						self.kills_to_print.append(kill["EventId"])
						image = get_images(items_dict,
						                   kill["Killer"]["Name"],
						                   kill["Victim"]["Name"],
						                   stats["Gdy_se_to_stalo"],
						                   kill["Killer"]["GuildName"],
						                   kill["Victim"]["GuildName"],
						                   kill["Killer"]["AverageItemPower"],
						                   kill["Victim"]["AverageItemPower"]
						                   )
						return image

					else:
						pass

			except JSONDecodeError:
				return
			if len(self.kills_to_print) > 150:
				print("Purging...")
				self.kills_to_print = []
