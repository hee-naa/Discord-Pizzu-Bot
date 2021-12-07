import discord
from discord.ext import commands

from gtts import gTTS

bot=commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print('연결이 완료되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="눈나들 명령(-tts)"))

@bot.command()
async def tts(ctx, *, text):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

        if voice == None:
            voice = await channel.connect()
            await ctx.guild.change_voice_state(channel=channel, self_deaf=True)

        tts = gTTS(text=text,lang='ko')
        tts.save('tts.mp3')

        audio_source = await discord.FFmpegOpusAudio.from_probe('tts.mp3')
        voice.play(audio_source)
    else:
        await ctx.channel.send("음성 채널에 들어가서 써줘 눈나")

bot.run('OTE3NjQzMjQ1OTU2MjU1ODI0.Ya7r3g.SeW2M5StP4u6Jopw_YxCBy7uSL0')
