from discord.ext import commands
import random
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

#nlist={'威圧':15, '言いくるめ':5, '医学':1, '運転':20, '応急手当':30, 'オカルト':5, '隠密':20, '回避':0, '科学':1, '鍵開け':1, '鑑定':5, '機械修理':10, '聞き耳':20, '近接戦闘':25, 'クトゥルフ神話':0, '芸術':5, '経理':5, '考古学':1, 'コンピューター':5, 'サバイバル':10, '自然':10, '拳銃':20, 'ライフル':25, 'ショットガン':25, '重機械操作':1, '信用':0, '心理学':10, '人類学':1, '水泳':20, '精神分析':1, '説得':10, '操縦':1, '跳躍':20, '追跡':10, '手さばき':10, '機械修理':10, '電子工学':1, '投擲':20, '登攀':20, '図書館':20, 'ナビゲート':10, '変装':5, '法律':5, '母国語':0, '魅惑':15, '目星':25, '歴史':5}
dlist={'アイデア':70,'威圧':15, '言いくるめ':5, '医学':80, '運転':20, '応急手当':30, 'オカルト':5, '隠密':20, '回避':65, '科学':61, '鍵開け':1, '鑑定':5, '機械修理':10, '聞き耳':50, '近接戦闘':25, 'クトゥルフ神話':15, '芸術':5, '経理':5, '考古学':1, 'コンピューター':5, 'サバイバル':10, '自然':10, '拳銃':20, 'ライフル':25, 'ショットガン':25, '重機械操作':1, '信用':82, '心理学':75, '人類学':1, '水泳':20, '精神分析':1, '説得':65, '操縦':9, '跳躍':20, '追跡':10, '手さばき':10, '電気修理':10, '電子工学':1, '投擲':20, '登攀':20, '図書館':20, 'ナビゲート':10, '変装':5, '法律':5, '日本語':90, 'ドイツ語':90, '魅惑':15, '目星':50, '歴史':5}
klist={'アイデア':85,'威圧':30,'言いくるめ':5, '医学':1,'運転':55,'応急手当':40,'オカルト':5,     '隠密':20,     '回避':0,     '科学':1,     '鍵開け':1, '鑑定':5,     '機械修理':50,     '聞き耳':20,     '近接戦闘':75,     'クトゥルフ神話':13, '芸術':5,     '経理':5,     '考古学':1,     'コンピューター':5, 'サバイバル':50, '自然':10,     '拳銃':20,     'ライフル':25,     'ショットガン':25, '重機械操作':1, '信用':0,     '心理学':50,     '人類学':1,     '水泳':20,     '精神分析':1, '説得':10,     '操縦':1,     '跳躍':20,     '追跡':10,     '手さばき':10, '電気修理':10,     '電子工学':1,     '投擲':20,     '登攀':20,     '図書館':20, 'ナビゲート':10, '変装':5,     '法律':85,     '母国語':0,     '魅惑':15, '目星':75, '歴史':65}
def mdrand():
    return random.randint(1,100)

def dicejudge(dicenum, judge):
    if dicenum == 1:
        mresult = '！　クリティカル(決定的成功)！！'
    elif dicenum <= judge:
        if dicenum <= judge//5:
            mresult = '！  成功！(Extreme)'
        elif dicenum <= judge//2:
            mresult = '！  成功！(Hard)'
        else:
            mresult = '！  成功！(Regular)'
    else:
        if judge >= 50:
            if dicenum == 100:
                mresult = '！  ファンブル(致命的失敗...)'
            else:
                mresult = '！  失敗...'                
        else:
            if dicenum >= 96:
                mresult = '！  ファンブル(致命的失敗...)'
            else:
                mresult = '！  失敗...'
    return mresult

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def botstatus(ctx):
    await ctx.send('Ready!! v1.04')

@bot.command()
async def what(ctx, what):
    await ctx.send(f'{what}を振りました'+str(random.randint(1,100)))

@bot.command()
async def k(ctx, what):
    if what not in klist:
        await ctx.send(f'{what}ロールが登録されていません。')
        return
    mname = 'キリコ'
    dicenum = mdrand()
    mresult = dicejudge(dicenum, klist[what])
    await ctx.send(mname + f'の{what}ロール(' + str(klist[what]) + ') → ' + str(dicenum) + mresult)

@bot.command()
async def chkk(ctx):
    i = 0
    for k in klist:
        if i == 0:
            outlist = ' '
        outlist = outlist + str(k) + ':' + str(klist[k]) + ',  '
        i = i + 1
        if i == 10:
            await ctx.send(outlist)
            i = 0
    await ctx.send(outlist)

@bot.command()
async def d(ctx, what):
    if what not in dlist:
        await ctx.send(f'{what}ロールが登録されていません。')
        return
    mname = '九鬼'
    dicenum = mdrand()
    mresult = dicejudge(dicenum, dlist[what])
    await ctx.send(mname + f'の{what}ロール(' + str(dlist[what]) + ') → ' + str(dicenum) + mresult)

@bot.command()
async def chkd(ctx):
    i = 0
    for k in dlist:
        if i == 0:
            outlist = ' '
        outlist = outlist + str(k) + ':' + str(dlist[k]) + ',  '
        i = i + 1
        if i == 10:
            await ctx.send(outlist)
            i = 0
    await ctx.send(outlist)

@bot.command()
async def r(ctx, what):
    return

bot.run(token)
