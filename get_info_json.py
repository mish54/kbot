import aiohttp
import asyncio
import json
from api_calls.get_guild_members import Members


async def fetch(session, url):
	async with session.get(url) as response:
		return await response.text()


async def main():
	members = await Members.get_members()
	killers =
	victims =
	async with aiohttp.ClientSession() as session:
		html = await fetch(session, 'https://gameinfo.albiononline.com/api/gameinfo/events?limit=1&offset=0')
		json_out = json.loads(html)
		for i in json_out[0]["Participants"]:
			#print(f"Victim: {json_out[0]['Victim']['Name']}")
			#print(f"Participants: \nGuildname: {i['GuildName']} \nPlayername: {i['Name']}")
			print(members[-1])


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())
