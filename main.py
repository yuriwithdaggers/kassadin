import re
import requests
import discord
from discord.ext import commands
from decouple import config
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound


bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
    print(f'You are null and void... ~ "{bot.user.name}"')
    print('github.com/yuriwithdaggers')

# <Embed> -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
async def embedDays(nick, region, days):
    url_image = 'https://external-preview.redd.it/K7kgJJoMDnZ12UckcpAExt3EZY307CWHNDkdU-0uelc.jpg?auto=webp&s=409b77562cb6c2b961ccbc53aaf5968a975c7f7a'

    embed = discord.Embed(
        description = f"Summoner Name: **{nick}**\n**{nick}** is available in **{days}** days!",
        color=0xed377d,
    )

    embed.set_author(name=f"Summoner Name: {nick} | Region: {region.upper()}", icon_url=bot.user.avatar_url)
    embed.add_field(name='-='*25, value=f'🌠   If the nick is in an inactive account, there is no way to get it.\n')
    embed.set_thumbnail(url=url_image)
    embed.set_footer(text=f"\ngithub.com/yuriwithdaggers") #Please, keep the credits.
    
    return embed

async def embedAvailable(nick, region):
    url_image = 'https://external-preview.redd.it/K7kgJJoMDnZ12UckcpAExt3EZY307CWHNDkdU-0uelc.jpg?auto=webp&s=409b77562cb6c2b961ccbc53aaf5968a975c7f7a'

    embed = discord.Embed(
        description = f"Summoner Name: **{nick}**\n**{nick}** is available!",
        color=0x5cfa77,
    )

    embed.set_author(name=f"Summoner Name: {nick} | Region: {region.upper()}", icon_url=bot.user.avatar_url)
    embed.add_field(name='-='*25, value=f'🌠   Get him before someone else gets it first...\n')
    embed.set_thumbnail(url=url_image)
    embed.set_footer(text=f"\ngithub.com/yuriwithdaggers") #Please, keep the credits.
    
    return embed 

async def embedProbably(nick, region):
    url_image = 'https://external-preview.redd.it/K7kgJJoMDnZ12UckcpAExt3EZY307CWHNDkdU-0uelc.jpg?auto=webp&s=409b77562cb6c2b961ccbc53aaf5968a975c7f7a'

    embed = discord.Embed(
        description = f"Summoner Name: **{nick}**\n**{nick}** is probably available!",
        color=0xf2e141,
    )

    embed.set_author(name=f"Summoner Name: {nick} | Region: {region.upper()}", icon_url=bot.user.avatar_url)
    embed.add_field(name='-='*25, value=f'🌠   It may or may not be possible to get it, 50/50\n🌠   If the nick is in a banned account or in an inactive account for a long time, it will not be possible to get it\n')
    embed.set_thumbnail(url=url_image)
    embed.set_footer(text=f"\ngithub.com/yuriwithdaggers") #Please, keep the credits.
    
    return embed 
# # </Embed> -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# <Check nickname> -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
@bot.command(name="check")
async def check(ctx, region, *nickname):
        nick = " ".join(nickname)
        regions = ('br', 'na', 'oce', 'las', 'lan', 'eune', 'euw', 'kr', 'jp', 'ru', 'tr')
        region = region.lower()
        if region not in regions:
            await ctx.send("Invalid region.   [BR, NA, OCE, LAS, LAN, EUNE, EUW, KR, JP, RU, TR]")
            return
        url = f'https://lols.gg/en/name/checker/{region}/' + str(nick)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}

        async def daysLeft():
            r = requests.get(url, headers=headers)
            r = r.text
            countDown = re.search("available in([^.]*)days", r)
            days = int(countDown.group(1))
            return days
        
        async def available():
            r = requests.get(url, headers=headers)
            r = r.text
            if 'is available!</h4>' in r or 'is available!</h2>' in r:
                await ctx.send(embed=await embedAvailable(nick, region))
            elif f'is probably available!</h4>' in r:
                await ctx.send(embed=await embedProbably(nick, region))
            else:
                days = await daysLeft()
                await ctx.send(embed=await embedDays(nick, region, days))
        
        await available()
# </Check nickname> -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# <Error> -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error,MissingRequiredArgument):
        await ctx.send('You need to put the region and the nick, example: "!check br Seiku"')
    elif isinstance(ctx,CommandNotFound):
        await ctx.send('The command to check the nick is "!check"')
# <\Error> -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
TOKEN= config('TOKEN')
bot.run(TOKEN)
