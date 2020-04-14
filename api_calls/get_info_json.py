import aiohttp
from aiohttp.client_exceptions import ClientConnectionError
import io
from json import JSONDecodeError
import json
from api_calls.image_builder import get_images
import random

class Kills:
	def __init__(self):
		self.already_displayed = []
		self.kill_messages = {
			1: "Za Moc a Slavu!",
		    2: "Za vetsi slavu gildy!",
		    3: "Chvalte Brychtezena!",
		    3: "Smrt nepratelum!",
		    4: "Baf!",
		    5: "Smrt Msicim Lidem!"
		                      }
		self.victim_messages = {
			1: "Slabi nebudou diktovat!",
			2: "Takova potupa!",
			3: "Bez a rychle ho zabij!",
			3: "Seno a vidle!",
			4: "Zalez do naplaveniny!",
			5: "Jezisi to je takova bolest,\n tak ukrutna bolest!!\n AAAAA!!!"
		}
		self.guild_id = "uatVVzFyQjqf_H_Bfl8i2A"

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
					if i["Killer"]["GuildId"] == self.guild_id and i["EventId"] not in self.already_displayed:
						# TODO: this all is a duplicit code, move to function or find other way to remove it
						print("We have a killer")
						stats = {}
						_items = {}
						_items["Killer"] = i["Killer"]["Equipment"]
						_items["Victim"] =  i["Victim"]["Equipment"]
						date = i["TimeStamp"].split("T")[0]
						time = i["TimeStamp"].split("T")[1].split(".")[0]
						stats["Gdy_se_to_stalo"] = date + " " + time
						self.already_displayed.append(i["EventId"])
						image = get_images(_items,
						                  i["Killer"]["Name"],
						                  i["Victim"]["Name"],
						                  stats["Gdy_se_to_stalo"],
						                  i["Killer"]["GuildName"],
						                  i["Victim"]["GuildName"],
						                  i["Killer"]["AverageItemPower"],
						                  i["Victim"]["AverageItemPower"],
						                  i["TotalVictimKillFame"],
						                  self.kill_messages[random.randint(1,5)],
						                  i["Participants"]
						                  )
						return image

					elif i["Victim"]["GuildId"] == self.guild_id and i["EventId"] not in self.already_displayed:
						print("We have a victim")
						stats = {}
						_items = {}
						_items["Killer"] = i["Killer"]["Equipment"]
						_items["Victim"] = i["Victim"]["Equipment"]
						date = i["TimeStamp"].split("T")[0]
						time = i["TimeStamp"].split("T")[1].split(".")[0]
						stats["Gdy_se_to_stalo"] = date + " " + time
						self.already_displayed.append(i["EventId"])
						image = get_images(_items,
						                   i["Killer"]["Name"],
						                   i["Victim"]["Name"],
						                   stats["Gdy_se_to_stalo"],
						                   i["Killer"]["GuildName"],
						                   i["Victim"]["GuildName"],
						                   i["Killer"]["AverageItemPower"],
						                   i["Victim"]["AverageItemPower"],
						                   i["TotalVictimKillFame"],
						                   self.victim_messages[random.randint(1,5)],
						                   i["Participants"]
						                   )
						return image

					else:
						pass

			except JSONDecodeError:
				return
			if len(self.already_displayed) > 150:
				print("Purging...")
				self.already_displayed = []
