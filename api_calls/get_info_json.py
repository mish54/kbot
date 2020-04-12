import aiohttp
from aiohttp.client_exceptions import ClientConnectionError
import io
from json import JSONDecodeError
import json

import api_calls.variables
from api_calls.kill import Kill

class PVP_Kills:
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
					if kill["Killer"]["GuildId"] is GUILD_ID and kill["Victim"]["GuildId"] is GUILD_ID
						and kill["EventId"] not in self.kills_to_print:
						print("We have an incident!")
						self.kills.append(Kill(kill,2))

					# clen guildy uspesne nekoho zabil
					else if kill["Killer"]["GuildId"] is GUILD_ID and kill["EventId"] not in self.kills_to_print:
						print("We have a killer")
						self.kills.append(Kill(kill,0))

					# clen guildy padnul v boji
					elif kill["Victim"]["GuildId"] is GUILD_ID and kill["EventId"] not in self.kills_to_print:
						print("We have a victim")
						self.kills.append(Kill(kill,1))

					# cizi guilda
					else:
						pass

				last_kill_id = kills[0]["EventId"]

			except JSONDecodeError:
				return
