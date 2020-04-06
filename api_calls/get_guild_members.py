import aiohttp
import json
from json import JSONDecodeError

class Members:

	def __init__(self):
		pass

	@staticmethod
	async def fetch(session, url):
		async with session.get(url) as response:
			return await response.text()

	# TODO: make guild configurable
	@staticmethod
	async def get_members():
		current_member_ids = []
		async with aiohttp.ClientSession() as session:
			html = await Members.fetch(session, f'https://gameinfo.albiononline.com/api/gameinfo/guilds/uatVVzFyQjqf_H_Bfl8i2A/members')
			try:
				json_out = json.loads(html)
				for i in json_out:
					current_member_ids.append(i["Id"])
			except JSONDecodeError:
				pass
		return current_member_ids
