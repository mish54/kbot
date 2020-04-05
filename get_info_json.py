import aiohttp
import asyncio
import json
from api_calls.get_guild_members import Members
from api_calls.get_killers import Killers
from api_calls.get_victims import Victims


async def fetch(session, url):
	async with session.get(url) as response:
		return await response.text()


async def main():
	members = await Members.get_members()
	killers = await Killers.get_members()
	victims = await Victims.get_members()
	async with aiohttp.ClientSession() as session:
		html = await fetch(session, 'https://gameinfo.albiononline.com/api/gameinfo/events?limit=1&offset=0')
		json_out = json.loads(html)
		print(members[-1])
		print(f"Victim {victims[-1]}")
		print(f"Killer {killers[-1]}")



if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())
