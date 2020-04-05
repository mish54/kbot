import aiohttp
import asyncio
from json import JSONDecodeError
import json
from api_calls.get_guild_members import Members


class Kills:
	def __init__(self):
		pass

	@staticmethod
	async def fetch(session, url):
		async with session.get(url) as response:
			return await response.text()

	@staticmethod
	async def main():
		members = await Members.get_members()
		async with aiohttp.ClientSession() as session:
			html = await Kills.fetch(session, 'https://gameinfo.albiononline.com/api/gameinfo/events?limit=51&offset=0')
			try:
				json_out = json.loads(html)

				for i in json_out:
					if i["Killer"]["Id"] in members:
						print("We have a killer")
						stats = {}
						stats["Gdo_to_koupil"] = i["Victim"]["Name"]
						stats["Jaka_gilda"] = i["Victim"]["GuildName"]
						stats["Meno_vraha"] = i["Killer"]["Name"]
						stats["Vrah_byl_vodkad"] = i["Killer"]["GuildName"]
						stats["Jak_byl_silnej"] = i["Killer"]["AverageItemPower"]
						stats["Gdo_tam_byl_este"] = [i["Participants"][0]["Name"]]
						return stats

					elif i["Victim"]["Id"] in members:
						print("We have a victim")
						stats = {}
						stats["Gdo_to_koupil"] = i["Victim"]["Name"]
						stats["Jaka_gilda"] = i["Victim"]["GuildName"]
						stats["Meno_vraha"] = i["Killer"]["Name"]
						stats["Vrah_byl_vodkad"] = i["Killer"]["GuildName"]
						stats["Jak_byl_silnej"] = i["Killer"]["AverageItemPower"]
						stats["Gdo_tam_byl_este"] = [i["Participants"][0]["Name"]]
						return stats

					else:
						pass

			except JSONDecodeError:
				return
