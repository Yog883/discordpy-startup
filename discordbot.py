#Discord.pyの読み込み
import discord
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong2')

#メッセージを取得した時に実行される
#@client.event
#async def on_message(message): 
#
#    #条件に当てはまるメッセージかチェックし正しい場合は返す
#    def check(msg):
#        return msg.author == message.author
#    
#    #ユーザーからのメッセージを待つ
#    wait_message = await client.wait_for("message", check=check)
#
#    #取得したメッセージを書き込まれたチャンネルへ送信
#    await message.channel.send(wait_message.content)

#Botの実行
client.run(TOKEN)
