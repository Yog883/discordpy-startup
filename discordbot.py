from discord.ext import commands
import random
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

def mdrand():
    return random.randint(1,100)

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def status(ctx):
    await ctx.send('準備中...')

@bot.command()
async def what(ctx, what):
    await ctx.send(f'{what}を振りました'+str(random.randint(1,100)))

@bot.command()
async def k(ctx, what):
    dicenum = mdrand()
    await ctx.send(f'キリコの{what}ロール → '+str(dicenum)+'!  成功？')

@bot.command()
async def d(ctx, what):
    dicenum = random.randint(1,100)
    await ctx.send(f'医者の{what}ロール → '+str(dicenum)+'!  成功？')

bot.run(token)
