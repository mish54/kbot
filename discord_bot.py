#!/usr/bin/env
import os
from datetime import datetime
import discord
from dotenv import load_dotenv
import asyncio
from api_calls.get_info_json import PVP_Kills

kill = PVP_Kills()

# nastaveni enviromentu
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
#GUILD2 = os.getenv('DISCORD_GUILD2')

client = discord.Client()



@client.event
async def on_ready():
	print(f"{client.user.name} has connected to discord!")
	client.loop.create_task(on_message())


@client.event
async def on_message(message=""):
	await client.wait_until_ready()
	channel = client.get_channel(697367087844294697)

	while not client.is_closed():
		kills = await kill.main()
		if kills is not None:
			try:
				file = discord.File(kills, filename="kills.png")
				await channel.send("Kill.png", file=file)
			except discord.errors.HTTPException:
				print("Nothing to report")
		else:
			print(str(datetime.now()) + ": No kill found.")
		await asyncio.sleep(5)


client.run(TOKEN)
