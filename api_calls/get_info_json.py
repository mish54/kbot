import aiohttp
from json import JSONDecodeError
import json
from api_calls.image_builder import get_images
import random
from aiohttp.client_exceptions import ClientPayloadError


class Kills:
	def __init__(self, guild_id):
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
		self.guild_id = guild_id

	@staticmethod
	async def fetch(session, url):
		async with session.get(url) as response:
			try:
				assert response.status == 200
			except AssertionError:
				print(f"Response recieved: {response.status}")

			try:
				payload = await response.read()
			except ClientPayloadError:
				print("Got payload exception")
			return payload

	async def main(self):
		async with aiohttp.ClientSession() as session:
			html = await Kills.fetch(session,
			                         'https://gameinfo.albiononline.com/api/gameinfo/events?limit=51&offset=0'
			                         )
			try:
				json_out = json.loads(html.decode("utf-8"))

				for kill in json_out:

					# zabiti hracu guildy navzajem (napr. hellgate)
					if kill["Killer"]["GuildId"] == self.guild_id and kill["Victim"]["GuildId"] == self.guild_id \
						and kill["EventId"] not in self.already_displayed:
						print("We have an incident!")
						self.already_displayed.append(kill["EventId"])
						image = get_image(kill, 2, self.kill_messages[random.randint(1,5)])
						return image

					# clen guildy uspesne nekoho zabil
					elif kill["Killer"]["GuildId"] == self.guild_id and kill["EventId"] not in self.already_displayed:
						print("We have a killer")
						self.already_displayed.append(kill["EventId"])
						image = get_image(kill, 0, self.kill_messages[random.randint(1,5)])
						return image

					# clen guildy padnul v boji
					elif kill["Victim"]["GuildId"] == self.guild_id and kill["EventId"] not in self.already_displayed:
						print("We have a victim")

						self.already_displayed.append(kill["EventId"])
						image = get_image(kill, 1, self.victim_messages[random.randint(1,5)])
						return image

					# cizi guilda
					else:
						pass

			except JSONDecodeError:
				return

			if len(self.already_displayed) > 150:
				print("Purging...")
				self.already_displayed = list(self.already_displayed[-10:])
