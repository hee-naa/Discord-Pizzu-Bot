import requests

import discord
from discord.ext import commands

from gtts import gTTS

intents = discord.Intents.default()
intents.members = True
bot=commands.Bot(command_prefix='-', intents = intents)

@bot.event
async def on_ready():
    print('연결이 완료되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="눈나들 명령(-tts)"))

@bot.command()
async def tts(ctx, *, text):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

        if voice is None:
            voice = await channel.connect()
            await ctx.guild.change_voice_state(channel=channel, self_deaf=True)

        tts = gTTS(text=text,lang='ko')
        tts.save('tts.mp3')

        audio_source = await discord.FFmpegOpusAudio.from_probe('tts.mp3')
        voice.play(audio_source)
    else:
        await ctx.channel.send('음성 채널에 들어가서 써줘 눈나')

@bot.event
async def on_typing(channel, user, when):
    if when.minute % 13 == 0 and when.second == 30:
        await channel.send('어? ' + user.display_name + '눈나 뭐 치고 있네?')

@bot.event
async def on_member_update(before, after):
    if before.display_name != after.display_name:
        channels = before.guild.text_channels
        for channel in channels:
            if channel.name == '일반':
                await channel.send('어? ' + before.display_name + '눈나 별명 바꿨네ㅎ 이제 ' + after.display_name + '눈나라고 부르면 될까?')
                break

@bot.event
async def on_raw_reaction_add(payload):
    if payload.member.bot is False:
        channel = bot.get_channel(payload.channel_id)
        msg = await channel.fetch_message(payload.message_id)
        await msg.add_reaction(payload.emoji)

@bot.event
async def on_voice_state_update(member, before, after):
    voice = before.channel if after.channel is None else after.channel
    members = voice.members
    if len(members) == 1 and members[0].bot is True and members[0].display_name == '읍준':
        channels = member.guild.text_channels
        for channel in channels:
            if channel.name == '일반':
                await channel.send('어? 눈나들 다 나갔네 준이 다음에 또 불러줘ㅎ')
                break

@bot.command()
async def send_message_marin(ctx, *, text):
    channel = bot.get_channel(843710788656824343)
    await channel.send(text)

bot.run('OTE3NjQzMjQ1OTU2MjU1ODI0.Ya7r3g.SeW2M5StP4u6Jopw_YxCBy7uSL0')
