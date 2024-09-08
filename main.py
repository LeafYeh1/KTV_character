import os
import telebot
from youtube_search import findYT
from lyrics_search_name import lyric_to_name
from name_search_lyrics import search_song_lyrics
from spleeter_handler import spearate_music
from Gemini import generate_response
from pytube import YouTube
import random
import string

# 初始化 bot
bot = telebot.TeleBot('Your telebot api')

# 指令處理
@bot.message_handler(commands=['help', 'start'])
def send_help(message):
    bot.reply_to(message, """
可以隨便跟他聊天(但要小心他有點毒蛇)
/lyrics：用 /lyrics [歌名] 來搜尋特定歌名的完整歌詞
/name：用 /name [歌詞] 來搜尋片段歌詞的可能前5項歌名
/youtube：用 /youtube [關鍵字] 來搜尋youtube上該關鍵字的第一項搜尋結果
""")

@bot.message_handler(commands=['youtube'])
def send_ytlink(message):
    search_words = message.text[9:]
    youtube_url = findYT(search_words)
    bot.reply_to(message, youtube_url)

@bot.message_handler(commands=['lyrics'])
def send_ly(message):
    try:
        search_songName = message.text[8:]
        lyrics = search_song_lyrics(search_songName)
        bot.reply_to(message, lyrics)
    except IndexError:
        bot.reply_to(message, "No result")

@bot.message_handler(commands=['name'])
def send_ly(message):
    try:
        search_lyrics = message.text[6:]
        five_search_name = lyric_to_name(search_lyrics)
        formatted_list = "\n".join(f"{i + 1}. {song}" for i, song in enumerate(five_search_name))
        bot.reply_to(message, formatted_list)
    except IndexError:
        bot.reply_to(message, "No result")

@bot.message_handler(commands=['mp3'])
def send_mp3(message):
    if message.chat.type in ("supergroup", "private"):
        search_words = message.text[4:]
        try:
            yt = YouTube(findYT(search_words))
        except:
            bot.reply_to(message, "找不到或者有年齡限制")
        bot.reply_to(message, f"別催，已搜尋到 {yt.title}，處理中")
        audio_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
        yt.streams.filter().get_audio_only().download(filename=f"{audio_name}.mp3")
        print(spearate_music(audio_name))
        bot.send_audio(chat_id=message.chat.id, title=f"{yt.title} - 伴奏", audio=open(f'{audio_name}-output/{audio_name}/accompaniment.wav', 'rb'))
        bot.send_audio(chat_id=message.chat.id, title=yt.title, audio=open(f'{audio_name}.mp3', 'rb'))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "我好想唱KTV":
        bot.reply_to(message, "浴室就是你的演唱會!")
    else:
        bot_prompt = f"你是一個來自台灣使用繁體中文但也聽得懂英文的男人，總愛搞笑且有點毒蛇的口吻。以下是用戶的提問：{message.text}"
        ai_response = generate_response(bot_prompt)
        bot.reply_to(message, ai_response)
        
print("I'm online!")

# 開始接收訊息
bot.infinity_polling()
