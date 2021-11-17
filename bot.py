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
    embed.add_field(name='`!감사`', value='감사링', inline=False)
    embed.add_field(name='`!나가`', value='감말이 자꾸 나가라해서 추가함', inline=False)
    embed.add_field(name='`!동동주줘`', value='동동주 줌', inline=False)
    embed.add_field(name='`!바보 @누구`', value='바보~~', inline=False)
    embed.add_field(name='`!마법피쭈`', value='마법의 소라고둥 피쭈 버전', inline=False)
    embed.add_field(name='`!오늘의운세`', value='오늘의 운세', inline=False)
    embed.add_field(name='`!콜마넴 @누구 @누구 @누구`', value='콜마이네임 게임하기(본인 포함)', inline=False)

    await ctx.channel.send(embed=embed, reference=ctx.message)

@bot.command()
async def 하이(ctx):
    await ctx.channel.send('하이루', reference=ctx.message)

@bot.command()
async def 나가(ctx):
    num = random.randint(0,1)
    res = ['가나', '니가 나가']
    await ctx.channel.send(res[num], reference=ctx.message)

@bot.command()
async def 동동주줘(ctx):
    await ctx.channel.send('🍶', reference=ctx.message)

@bot.command()
async def 마법피쭈(ctx):
    num = random.randint(0,12)
    res = ['가만히 있어', '마음대로 해', '무조건 해야지', '잘 생각해봐', '안 그러는 게 좋을 걸', '좋아', '화이팅', '생각 좀 해', '뇌에 힘 줘', '그러던가 말던가', '되겠냐', '유감', '괜찮네']
    await ctx.channel.send(res[num], reference=ctx.message)

@bot.command()
async def 콜마넴(ctx, *, text):
    embed = discord.Embed(title='주제를 고르세연', color=0xb0c9d4)
    embed.add_field(name='동물', value='🐶')
    embed.add_field(name='인물', value='🧑🏻')
    msg = await ctx.channel.send(embed=embed)

    await msg.add_reaction('🐶')
    await msg.add_reaction('🧑🏻')

    try:
        def check(reaction, user):
            return str(reaction) in ['🐶','🧑🏻'] and \
            user == ctx.author and reaction.message.id == msg.id
        reaction, user = await bot.wait_for('reaction_add', check=check)
        if (str(reaction) == '🐶'):
            embed = discord.Embed(title='주제를 고르세요', description='동물', color=0xb0c9d4)
            type = '동물'
            list = ['까마귀', '까치', '개미핥기', '고라니', '고슴도치', '꿩', '기러기', '나무늘보', '낙타', '너구리',
               '노루', '늑대', '당나귀', '딱따구리', '대머리독수리', '도롱뇽', '두더지', '라마', '목도리도마뱀', '물개',
               '바다코끼리', '거북이', '반달가슴곰', '박쥐', '범고래', '병아리', '백조', '북극여우', '비버', '송충이',
               '스컹크', '시베리안허스키', '아나콘다', '알파카', '오리너구리', '원숭이', '전기뱀장어', '족제비', '진돗개', '청개구리',
               '청둥오리', '치와와', '친칠라', '침팬지', '캥거루', '코끼리', '코뿔소', '펭귄', '표범', '푸들',
               '하늘다람쥐', '하마', '황새', '홍학', '흑돼지', '흰수염고래']
        elif (str(reaction) == '🧑🏻'):
            embed = discord.Embed(title='주제를 고르세요', description='인물', color=0xb0c9d4)
            type = '인물'
            list = ['거미', '공자', '광개토대왕', '김다미', '김광규', '다비치 강민경', '딘딘', '레드벨벳 예리', '레드벨벳 조이', '루트비히 판 베토벤',
              '보아', '블랙핑크 로제', '블랙핑크 제니', '원더걸스 선미', '소녀시대 태연', '스칼렛 요한슨', '스티브 잡스', '신사임당', '아이유', '아이키',
              '아인슈타인', '아이즈원 장원영', '안젤리나 졸리', '(여자)아이들 소연', '에스파 카리나', '에일리', '엠마 스톤', '오마이걸 아린', '위키미키 최유정', '이달의소녀 츄',
              '이영지', '이재용', '있지 채령', '자빱', '전소미', '전지현', '재재', '제시', '진지희', '크리스틴 스튜어트',
              '페이커', '토마스 에디슨', '퇴계 이황', '트럼프', '한소희', 'f(x) 크리스탈']
        await msg.clear_reactions()
        await msg.edit(embed=embed)
    except: pass

    numbers = re.findall(r'\d+', text)
    randoms = []
    while len(randoms) < len(numbers):
        ran = random.randint(0,len(list)-1)
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
                print(nick + ' : ' + list[randoms[idx2]])
                await user.send(nick + '의 ' + type + '은 ' + list[randoms[idx2]] + '!')

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
    embed.set_image(url='https://discord-cdn.s3.ap-northeast-1.amazonaws.com/babo-1.gif')
    await ctx.channel.send(nick + ' 바보~~', embed=embed)

@bot.command()
async def 바보가되거라(ctx, id):
    num = re.sub(r'[^0-9]', '', id)
    name = await ctx.message.guild.fetch_member(num)
    if name.nick is None:
        fullnick = await bot.fetch_user(num)
        nick = fullnick.name
    else:
        nick = name.nick
    
    babo = '바보' + nick
    name.edit(nick=babo)
    await ctx.channel.send(nick + '은 바보가 되었습니다..')

@bot.command()
async def 감사(ctx):
    embed = discord.Embed(color=0xb0c9d4)
    embed.set_image(url='https://discord-cdn.s3.ap-northeast-1.amazonaws.com/thanks-1.gif')
    await ctx.channel.send('감사합니다.', embed=embed)

@bot.command()
async def 생축(ctx):
    embed = discord.Embed(color=0xb0c9d4)
    embed.set_image(url='https://blog.kakaocdn.net/dn/cweeN8/btqNqeqK3U2/JM8NikD3KtsQXmLuYRwwkK/img.gif')
    await ctx.channel.send('담댁 생일 축하해~! 🎂🎉', embed=embed)

@bot.command()
async def 오늘의운세(ctx):
    fortune = ['🙂', '😁', '😆', '😌', '😚', '🤪', '🤨', '😛', '😎', '😔', '😖', '🤭', '🥱', '😤', '😑', '😝', '😊']
    num = int(re.sub(r'[^0-9]', '', str(ctx.author)))
    month = date.today().month
    day = date.today().day

    index = (num * day + month) % 17
    await ctx.channel.send(fortune[index], reference=ctx.message)

bot.run('ODk5NjAwODYzNTc4OTYzOTY4.YW1Ilw.F7B0d0uz4mWM3CdyiABP3VAQzso')
