import discord
from discord.ext import commands

from pytube import YouTube
from hendlers import Video

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.command() 
async def play(message, query): 
    # Получение ссылки на видео из сообщения
    url = query

   
    # Создание объекта YouTube
    yt = YouTube(url)

    # Выбор наилучшего качества видео
    ys = yt.streams.get_highest_resolution()
    ytitle = yt.title
    # Загрузка видео
    ys.download(output_path='./video')

    # Получение пути к загруженному видео
    video_path ='./video/' + ys.default_filename

    # Проигрывание аудио из загруженного видео в голосовом канале
    voice_channel = message.message.author.voice.channel
    voice_client = await voice_channel.connect()
    voice_client.play(discord.FFmpegPCMAudio(video_path))
    await message.channel.send(f'Проигрываю {ytitle}')

@bot.command()
async def stop(ctx):
    voice_client = ctx.voice_client

    try:
        if voice_client.is_playing():
            voice_client.stop()
    except:
        await ctx.channel.send('Я не проигрываю музыку')

    try:
        if voice_client.is_connected():
            await voice_client.disconnect()
    except:
        pass

 
    
bot.run('ха лох')
