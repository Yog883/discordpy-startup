from discord.ext import commands
import random
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

klist={'one':1, 'two':2, 'three':3}
dlist={'one':1, 'two':2, 'three':3}

def mdrand():
    return random.randint(1,100)

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def status(ctx):
    await ctx.send('準備中... v0.82')

@bot.command()
async def what(ctx, what):
    await ctx.send(f'{what}を振りました'+str(random.randint(1,100)))

@bot.command()
async def k(ctx, what):
    dicenum = mdrand()
    if what not in dlist:
        await ctx.send(f'{what}ロールが登録されていません。')
        return
    if dicenum <= klist[what]:
        await ctx.send(f'キリコの{what}ロール → '+str(dicenum)+'!  成功！')
    else:
        await ctx.send(f'キリコの{what}ロール → '+str(dicenum)+'!  失敗...')            

@bot.command()
async def d(ctx, what):
    dicenum = mdrand()
    if what not in dlist:
        await ctx.send(f'{what}ロールが登録されていません。')
        return
    await ctx.send(f'医者の{what}ロール → '+str(dicenum)+'!  成功？')

bot.run(token)
