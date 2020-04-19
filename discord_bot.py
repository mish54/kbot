#!/usr/bin/env
import os
from datetime import datetime
import discord
from dotenv import load_dotenv
import asyncio
from api_calls.get_info_json import Kills

# nastaveni enviromentu
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
GUILD_ID = os.getenv("GUILD_ID")
client = discord.Client()

kill = Kills(GUILD_ID)


@client.event
async def on_ready():
	print(f"{client.user.name} has connected to discord!")
	client.loop.create_task(on_message())


@client.event
async def on_message():
	await client.wait_until_ready()
	channel = client.get_channel(628899744617332737)

	while not client.is_closed():
		kills = await kill.main()
		if kills is not None:
			try:
				file = discord.File(kills, filename="kills.png")
				await channel.send("Kill.png", file=file)
			except discord.errors.HTTPException:
				print("Nothing to report")
		else:
			print(datetime.now())
		await asyncio.sleep(2)


client.run(TOKEN)
