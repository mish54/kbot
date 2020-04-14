import aiohttp
from aiohttp.client_exceptions import ClientConnectionError
import io
from json import JSONDecodeError
import json

import api_calls.variables
from api_calls.image_builder import get_image

class PVP_Kills:
	def __init__(self):
		self.already_displayed = []
		self.last_kill_id = -1

	@staticmethod
	async def fetch(session, url):
		async with session.get(url) as response:
			return await response.text()

	async def main(self):
		async with aiohttp.ClientSession() as session:
			try:
				# stazeni obsahu stranky
				html = await PVP_Kills.fetch(session,
				                         'https://gameinfo.albiononline.com/api/gameinfo/events?limit=51&offset=0')
			except:
				print("Client exception error, continuing...")
				pass

			try:
				# dekodovani stranky JSONu na contejnery pythonu
				json_out = json.loads(html)

				for kill in json_out:

					# zabiti hracu guildy navzajem (napr. hellgate)
					if kill["Killer"]["GuildId"] is GUILD_IDs and kill["Victim"]["GuildId"] is GUILD_ID \
						and kill["EventId"] not in self.already_displayed:
						print("We have an incident!")
						self.already_displayed.append(i["EventId"])
						image = get_image(kill, 2)
						return image

					# clen guildy uspesne nekoho zabil
					elif kill["Killer"]["GuildId"] is GUILD_IDs and kill["EventId"] not in self.already_displayed:
						print("We have a killer")
						self.already_displayed.append(i["EventId"])
						image = get_image(kill, 0)
						return image

						# clen guildy padnul v boji
					elif kill["Victim"]["GuildId"] is GUILD_IDs and kill["EventId"] not in self.already_displayed:
						print("We have a victim")
						self.already_displayed.append(i["EventId"])
						image = get_image(kill, 1)
						return image

					# cizi guilda
					else:
						pass

			except JSONDecodeError:
				return

			if len(self.already_displayed) > 150:
				print("Purging...")
				self.already_displayed = list(self.already_displayed[-10:])
