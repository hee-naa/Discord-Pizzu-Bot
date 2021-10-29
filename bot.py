import discord
from discord.ext import commands

import random
import re
from datetime import date

bot=commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('연결이 완료되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="!도움말"))

@bot.command()
async def 도움말(ctx):
    embed = discord.Embed(title="도움말", description="피쭈봇 사용법", color=0xb0c9d4)
    embed.set_footer(text="피쭈 제작")

    embed.add_field(name='`!하이`', value='하이하이', inline=False)
    embed.add_field(name='`!나가`', value='감말이 자꾸 나가라해서 추가함', inline=False)
    embed.add_field(name='`!동동주줘`', value='동동주 줌', inline=False)
    embed.add_field(name='`!바보 @누구`', value='바보~~', inline=False)
    embed.add_field(name='`!마법피쭈`', value='마법의 소라고둥 피쭈 버전', inline=False)
    embed.add_field(name='`!오늘의운세`', value='오늘의 운세', inline=False)
    embed.add_field(name='`!콜마넴 @누구 @누구 @누구`', value='콜마이네임 게임하기(본인 포함)', inline=False)

    await ctx.channel.send(embed=embed, reference=ctx.message)

@bot.command()
async def 하이(ctx):
    await ctx.channel.send('하이~~!', reference=ctx.message)

@bot.command()
async def 나가(ctx):
    await ctx.channel.send('싫어 -_-', reference=ctx.message)

@bot.command()
async def 동동주줘(ctx):
    await ctx.channel.send('🍶', reference=ctx.message)

@bot.command()
async def 마법피쭈(ctx):
    num = random.randint(0, 12)
    res = ['가만히 있어', '마음대로 해', '무조건 실행', '잘 생각해봐', '안 그러는 게 좋을 걸', '좋아', '화이팅', '생각 좀 해', '뇌에 힘 줘', '그러던가 말던가', '되겠냐', '유감', '괜찮네']
    await ctx.channel.send(res[num], reference=ctx.message)

@bot.command()
async def 콜마넴(ctx, *, text):
    animals = ['개미핥기', '목도리도마뱀', '알파카', '대머리독수리', '흑돼지', '진돗개', '바다코끼리', '원숭이', '오리너구리', '나무늘보', '아나콘다', '송충이', '반달가슴곰', '비버', '전기뱀장어', '범고래', '북극여우', '하늘다람쥐']
    numbers = re.findall(r'\d+', text)

    randoms = []
    while len(randoms) < len(numbers):
        ran = random.randint(0,17)
        if ran not in randoms:
            randoms.append(ran)
    
    for idx1 in range(len(numbers)):
        for idx2 in range(len(numbers)):
            if idx1 != idx2:
                mem = await ctx.message.guild.fetch_member(numbers[idx2])
                if mem.nick is None:
                    fullnick = await bot.fetch_user(numbers[idx2])
                    nick = fullnick.name
                else:
                    nick = mem.nick

                user = await bot.fetch_user(numbers[idx1])
                await user.send(nick + '의 동물은 ' + animals[randoms[idx2]] + '!')

@bot.command()
async def 바보(ctx, id):
    num = re.sub(r'[^0-9]', '', id)
    name = await ctx.message.guild.fetch_member(num)
    if name.nick is None:
        fullnick = await bot.fetch_user(num)
        nick = fullnick.name
    else:
        nick = name.nick

    embed = discord.Embed(color=0xb0c9d4)
    embed.set_image(url='https://s3.us-west-2.amazonaws.com/secure.notion-static.com/0779915b-1847-4de2-9592-d2701bdeef12/%E1%84%81%E1%85%A9%E1%84%87%E1%85%AE%E1%84%80%E1%85%B5.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20211029%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20211029T100835Z&X-Amz-Expires=86400&X-Amz-Signature=9050ad91b5125ce1b48681ca307e566581ecf002a558919633cfdc60cd2c540c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22%25E1%2584%2581%25E1%2585%25A9%25E1%2584%2587%25E1%2585%25AE%25E1%2584%2580%25E1%2585%25B5.gif%22')

    await ctx.channel.send(nick + ' 바보~~', embed=embed)

@bot.command()
async def 오늘의운세(ctx):
    fortune = ['🙂', '😁', '😆', '😌', '😚', '🤪', '🤨', '😛', '😎', '😔', '😖', '🤭', '🥱', '😤', '😑', '😝', '😊']
    num = int(re.sub(r'[^0-9]', '', str(ctx.author)))
    month = date.today().month
    day = date.today().day

    index = (num * day + month) % 17
    await ctx.channel.send(fortune[index], reference=ctx.message)

bot.run('ODk5NjAwODYzNTc4OTYzOTY4.YW1Ilw.F7B0d0uz4mWM3CdyiABP3VAQzso')
