import aiohttp
import requests
from json import JSONDecodeError
import json
from api_calls.get_guild_members import Members


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
			html = await Kills.fetch(session, 'https://gameinfo.albiononline.com/api/gameinfo/events?limit=51&offset=0')
			try:
				json_out = json.loads(html)
				for i in json_out:
					if i["Killer"]["Id"] in self.members and i["EventId"] not in self.already_displayed:
						print("We have a killer")
						stats = {}
						date = i["TimeStamp"].split("T")[0]
						time = i["TimeStamp"].split("T")[1].split(".")[0]
						stats["Gdy_se_to_stalo"] = date + " " + time
						stats["Gdo_to_koupil"] = i["Victim"]["Name"]
						stats["Jaka_gilda"] = i["Victim"]["GuildName"]
						stats["Meno_vraha"] = i["Killer"]["Name"]
						stats["Vrah_byl_vodkad"] = i["Killer"]["GuildName"]
						stats["Jak_byl_silnej"] = i["Killer"]["AverageItemPower"]
						stats["Gdo_tam_byl_este"] = [i["Participants"][0]["Name"]]
						self.already_displayed.append(i["EventId"])
						return stats

					elif i["Victim"]["Id"] in self.members and i["EventId"] not in self.already_displayed:
						print("We have a victim")
						stats = {}
						date = i["TimeStamp"].split("T")[0]
						time = i["TimeStamp"].split("T")[1].split(".")[0]
						stats["Gdy_se_to_stalo"] = date + " " + time
						stats["Gdo_to_koupil"] = i["Victim"]["Name"]
						stats["Jaka_gilda"] = i["Victim"]["GuildName"]
						stats["Meno_vraha"] = i["Killer"]["Name"]
						stats["Vrah_byl_vodkad"] = i["Killer"]["GuildName"]
						stats["Jak_byl_silnej"] = i["Killer"]["AverageItemPower"]
						stats["Gdo_tam_byl_este"] = [i["Participants"][0]["Name"]]
						self.already_displayed.append(i["EventId"])
						return stats

					else:
						pass

			except JSONDecodeError:
				return
			if len(self.already_displayed) > 150:
				print("Purging...")
				self.already_displayed = []
