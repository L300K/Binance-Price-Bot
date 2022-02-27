import requests, json
import discord
from discord.ext import commands
import datetime
bot = commands.Bot(command_prefix='!')
watchlist = "GALAUSDT"

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def setcrypto(ctx, crypto):
    global watchlist
    watchlist = crypto
    await ctx.channel.send("Crypto Type : " + crypto)

@bot.command()
async def setlow(ctx, low):
    while True:
        prices = json.loads(requests.get("https://fapi.binance.com/fapi/v1/ticker/price").content)
        for v in prices:
            if v['symbol'] in watchlist:
                symbol = v['symbol']
                pc = str(v['price'])
                time = str(v['time'])
                s = int(time) / 1000
                a = datetime.datetime.fromtimestamp(s).strftime('%d/%m/%Y %H:%M:%S')
        if pc <= low:
            print(low)
            await ctx.channel.send(watchlist + " : Now Low \nPrice : " + pc + "\nTime : " + a)
            break

@bot.command()
async def sethigh(ctx, high):
    while True:
        prices = json.loads(requests.get("https://fapi.binance.com/fapi/v1/ticker/price").content)
        for v in prices:
            if v['symbol'] in watchlist:
                symbol = v['symbol']
                pc = str(v['price'])
                time = str(v['time'])
                s = int(time) / 1000
                a = datetime.datetime.fromtimestamp(s).strftime('%d/%m/%Y %H:%M:%S')
        if pc >= high:
            print(high)
            await ctx.channel.send(watchlist + " : Now High \nPrice : " + pc + "\nTime : " + a)
            break

bot.run('DISCORD TOKEN')
