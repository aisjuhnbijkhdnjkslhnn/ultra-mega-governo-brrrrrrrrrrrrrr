import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


if __name__ == '__main__':
    bot.run('YOUR_BOT_TOKEN')
