import aiohttp
from aiohttp.client_exceptions import ClientConnectionError
from json import JSONDecodeError
import json
from api_calls.get_guild_members import Members
from api_calls.image_builder import get_images


class Kills:
	def __init__(self):
		self.members = Members().members
		self.already_displayed = []
		print(self.members[1])

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
				for i in json_out:
					if i["Killer"]["Id"] in self.members and i["EventId"] not in self.already_displayed:
						print("We have a killer")
						stats = {}
						killer_items = []
						victim_items = []
						for killer_item in i["Killer"]["Equipment"]:
							try:
								killer_items.append(i["Killer"]["Equipment"][killer_item]["Type"])
							except TypeError:
								pass
						items_dict = {"killer": killer_items}
						for victim_item in i["Killer"]["Equipment"]:
							try:
								victim_items.append(i["Killer"]["Equipment"][victim_item]["Type"])
							except TypeError:
								pass
						items_dict["victim"] = victim_items
						date = i["TimeStamp"].split("T")[0]
						time = i["TimeStamp"].split("T")[1].split(".")[0]
						stats["Gdy_se_to_stalo"] = date + " " + time
						self.already_displayed.append(i["EventId"])
						image = get_images(items_dict,
						                  i["Killer"]["Name"],
						                  i["Victim"]["Name"],
						                  stats["Gdy_se_to_stalo"],
						                  i["Killer"]["GuildName"],
						                  i["Victim"]["GuildName"],
						                  i["Killer"]["AverageItemPower"],
						                  i["Victim"]["AverageItemPower"]
						                  )
						return image

					elif i["Victim"]["Id"] in self.members and i["EventId"] not in self.already_displayed:
						print("We have a victim")
						stats = {}
						killer_items = []
						victim_items = []
						for killer_item in i["Killer"]["Equipment"]:
							try:
								killer_items.append(i["Killer"]["Equipment"][killer_item]["Type"])
							except TypeError:
								pass
						items_dict = {"killer": killer_items}
						for victim_item in i["Killer"]["Equipment"]:
							try:
								victim_items.append(i["Killer"]["Equipment"][victim_item]["Type"])
							except TypeError:
								pass
						items_dict["victim"] = victim_items
						date = i["TimeStamp"].split("T")[0]
						time = i["TimeStamp"].split("T")[1].split(".")[0]
						stats["Gdy_se_to_stalo"] = date + " " + time
						self.already_displayed.append(i["EventId"])
						image = get_images(items_dict,
						                   i["Killer"]["Name"],
						                   i["Victim"]["Name"],
						                   stats["Gdy_se_to_stalo"],
						                   i["Killer"]["GuildName"],
						                   i["Victim"]["GuildName"],
						                   i["Killer"]["AverageItemPower"],
						                   i["Victim"]["AverageItemPower"]
						                   )
						return image

					else:
						pass

			except JSONDecodeError:
				return
			if len(self.already_displayed) > 150:
				print("Purging...")
				self.already_displayed = []
