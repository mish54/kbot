#!/usr/bin/env
import os

import discord
from dotenv import load_dotenv
import asyncio
from api_calls.get_info_json import Kills

load_dotenv()

kill = Kills()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
client = discord.Client()



@client.event
async def on_ready():
	print(f"{client.user.name} has connected to discord!")
	client.loop.create_task(on_message())


@client.event
async def on_message():
	await client.wait_until_ready()
	channel = client.get_channel(628899744617332737)

	pvp_kills = PVP_Kills() # pocatecni inicializace kills
	while not client.is_closed():
		await pvp_kills.main()
		if len(pvp_kills.kills_to_print) == 0:
			try:
				# TODO upravit obrazky
				file = discord.File(pvp_kills.kills_to_print, filename="kills.png")
				await channel.send("Kill.png", file=file)
			except discord.errors.HTTPException:
				print("Nothing to report")
		else:
			print("No new PvP kill for selected guild.")
		await asyncio.sleep(1)


client.run(TOKEN)
