import aiohttp
import json


class Victims:

	def __init__(self):
		pass

	@staticmethod
	async def fetch(session, url):
		async with session.get(url) as response:
			return await response.text()

	# TODO: make guild configurable
	@staticmethod
	async def get_members():
		current_victim_ids = []
		async with aiohttp.ClientSession() as session:
			html = await Victims.fetch(session, f'https://gameinfo.albiononline.com/api/gameinfo/events?limit=51&offset=0')
			json_out = json.loads(html)
			for i in json_out:
				current_victim_ids.append(i["Victim"]["Id"])

		return current_victim_ids
