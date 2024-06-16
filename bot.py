from ai_music_api import api

import telebot


bot = telebot.TeleBot('')

music_generate = api()
music_generate.token('vAv5Yuyyp_5qUiP3cKI4g')


@bot.message_handler(commands=['start'])
def bot_satrt(message):
    bot.send_message(message.chat.id, 'Пришли мне описания трека чтоя я его сгенирировал')


@bot.message_handler(content_types=['text'])
def bot_music_generete(massage):
    id = massage.chat.id
    
    # bot.send_message(id, 'Выбери жанр')

    music_generate.create(title=massage.text, prompt=massage.text, )
    music_generate.ai_requsts()
    res_music = music_generate.res_music()
    
    bot.send_audio(id, audio=res_music['audio_url_0'] , performer='Xamz_pok', title=res_music['title'])
    # music_generate.create()

    

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)




