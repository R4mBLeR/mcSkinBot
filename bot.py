import discord
from discord.ext import commands
import config
import requests

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('bot is running...')

@bot.command(name="skin")
async def skin(ctx, nick):
    url = "https://crafthead.net/profile/"+nick
    doc = requests.get(url)
    if(doc.status_code==200):
        json = doc.json()
        id = json['id']
        skin = "https://crafatar.com/skins/"+id
        await ctx.send("https://namemc.com/profile/"+nick)
        embed=discord.Embed(title=nick, colour=0x00ff00)
        embed.set_image(url=skin)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Error!")
    

bot.run(config.token)