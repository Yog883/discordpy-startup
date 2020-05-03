from discord.ext import commands
import random
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

#nlist={'威圧':15, '言いくるめ':5, '医学':1, '運転':20, '応急手当':30, 'オカルト':5, '隠密':20, '回避':0, '科学':1, '鍵開け':1, '鑑定':5, '機械修理':10, '聞き耳':20, '近接戦闘':25, 'クトゥルフ神話':0, '芸術':5, '経理':5, '考古学':1, 'コンピューター':5, 'サバイバル':10, '自然':10, '拳銃':20, 'ライフル':25, 'ショットガン':25, '重機械操作':1, '信用':0, '心理学':10, '人類学':1, '水泳':20, '精神分析':1, '説得':10, '操縦':1, '跳躍':20, '追跡':10, '手さばき':10, '機械修理':10, '電子工学':1, '投擲':20, '登攀':20, '図書館':20, 'ナビゲート':10, '変装':5, '法律':5, '母国語':0, '魅惑':15, '目星':25, '歴史':5}

klist={'威圧':15, '言いくるめ':5, '医学':1, '運転':20, '応急手当':30, 'オカルト':5, '隠密':20, '回避':0, '科学':1, '鍵開け':1, '鑑定':5, '機械修理':10, '聞き耳':20, '近接戦闘':25, 'クトゥルフ神話':0, '芸術':5, '経理':5, '考古学':1, 'コンピューター':5, 'サバイバル':10, '自然':10, '拳銃':20, 'ライフル':25, 'ショットガン':25, '重機械操作':1, '信用':0, '心理学':10, '人類学':1, '水泳':20, '精神分析':1, '説得':10, '操縦':1, '跳躍':20, '追跡':10, '手さばき':10, '機械修理':10, '電子工学':1, '投擲':20, '登攀':20, '図書館':20, 'ナビゲート':10, '変装':5, '法律':5, '母国語':0, '魅惑':15, '目星':25, '歴史':5}
dlist={'威圧':15, '言いくるめ':5, '医学':1, '運転':20, '応急手当':30, 'オカルト':5, '隠密':20, '回避':0, '科学':1, '鍵開け':1, '鑑定':5, '機械修理':10, '聞き耳':20, '近接戦闘':25, 'クトゥルフ神話':0, '芸術':5, '経理':5, '考古学':1, 'コンピューター':5, 'サバイバル':10, '自然':10, '拳銃':20, 'ライフル':25, 'ショットガン':25, '重機械操作':1, '信用':0, '心理学':10, '人類学':1, '水泳':20, '精神分析':1, '説得':10, '操縦':1, '跳躍':20, '追跡':10, '手さばき':10, '機械修理':10, '電子工学':1, '投擲':20, '登攀':20, '図書館':20, 'ナビゲート':10, '変装':5, '法律':5, '母国語':0, '魅惑':15, '目星':25, '歴史':5}

def mdrand():
    return random.randint(1,100)

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def status(ctx):
    await ctx.send('準備中... v0.92')

@bot.command()
async def what(ctx, what):
    await ctx.send(f'{what}を振りました'+str(random.randint(1,100)))

@bot.command()
async def k(ctx, what):
    if what not in dlist:
        await ctx.send(f'{what}ロールが登録されていません。')
        return
    mname = 'キリコ'
    dicenum = mdrand()
    mresult = '失敗...'
    judge = klist[what]
    if dicenum == 1:
        mresult = '！　クリティカル(決定的成功)！！'
    elif dicenum <= judge:
        mresult = '！  成功！'
    else:
        mresult = '！  失敗...'
    await ctx.send(mname + f'の{what}ロール(' + str(klist[what]) + ') → ' + str(dicenum) + mresult)
    
#@bot.command()
#async def d(ctx, what):
#    if what not in dlist:
#        await ctx.send(f'{what}ロールが登録されていません。')
#        return
#    name = '医者'
#    dicenum = mdrand()
#    if dicenum = 1:
#        await ctx.send(name+f'の{what}ロール('+str(klist[what])+') → '+str(dicenum)+'!  クリティカル(決定的成功)！！')
#    elif dicenum <= klist[what]:
#        await ctx.send(name+f'の{what}ロール('+str(klist[what])+') → '+str(dicenum)+'!  成功！')
#    else:
#        await ctx.send(name+f'の{what}ロール('+str(klist[what])+') → '+str(dicenum)+'!  失敗...')
#    return

bot.run(token)
