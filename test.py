import os

import discord
from dotenv import load_dotenv

import aiohttp

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
client = discord.Client()



@client.event
async def on_ready():
	print(f"{client.user.name} has connected to discord!")


@client.event
async def on_member_join(member):
	await member.crate_dm()
	await member.dm_channel.send(
		f"Hi {member.name} welcome to the server!"
	)


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	quote = "ervweijnbwrotbinworinvweorneworvinero"

	if message.content == "10!":
		await message.channel.send(file=discord.File("picture.png"))


client.run(TOKEN)
