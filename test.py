import os

import discord
from dotenv import load_dotenv
import asyncio
from api_calls.get_info_json import Kills

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
client = discord.Client()



@client.event
async def on_ready():
	print(f"{client.user.name} has connected to discord!")
	client.loop.create_task(on_message())


@client.event
async def on_member_join(member):
	await member.crate_dm()
	await member.dm_channel.send(
		f"Hi {member.name} welcome to the server!"
	)


@client.event
async def on_message():
	await client.wait_until_ready()
	channel = client.get_channel(696073839939026945)

	while not client.is_closed():

		await channel.send("Fetching...")
		kills = await Kills.main()
		try:
			await channel.send(kills)
		except discord.errors.HTTPException:
			print("Nothing to report")
		await asyncio.sleep(10)


client.run(TOKEN)
