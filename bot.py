from discord.ext import commands
from config import TOKEN

bot = commands.Bot(command_prefix='//')

bot.run(TOKEN)