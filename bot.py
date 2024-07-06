from ai_music_api import api

import telebot

from telebot import types


bot = telebot.TeleBot('')

music_generate = api()
music_generate.token()


@bot.message_handler(commands=['start'])
def bot_satrt(message):
    bot.send_message(message.chat.id, 'Пришли мне описания трека чтоя я его сгенирировал')
 
 
@bot.message_handler(content_types=['text'])
def bot_music_generete(massage):
    id = massage.chat.id

    markup = types.InlineKeyboardMarkup()

    btn_pop = types.InlineKeyboardButton('Поп', callback_data='pop')
    btn_rock = types.InlineKeyboardButton('Рок', callback_data='rock')
    btn_hip_hop = types.InlineKeyboardButton('Хип-хоп', callback_data='hip-hop' )
    btn_jazz = types.InlineKeyboardButton('Джаз', callback_data='jazz')
    btn_reggae = types.InlineKeyboardButton('Регги', callback_data='reggae')
    btn_electronic = types.InlineKeyboardButton('Электро', callback_data='electronic')
    btn_rap = types.InlineKeyboardButton('Рэп', callback_data='rep')
    btn_reggaeton = types.InlineKeyboardButton('Реггетон', callback_data='reggaeton')
    
    markup.add(btn_pop, 
               btn_rock, 
               btn_hip_hop, 
               btn_reggae, 
               btn_electronic, 
               btn_jazz, 
               btn_rap, 
               btn_reggaeton,
           )

    music_generate.create(title=massage.text, prompt=massage.text, )      

    bot.send_message(id, 'Выбери жанр', reply_markup=markup)
     
@bot.callback_query_handler(func=lambda callback: True)
def callbeck_prompt(callback):
    id = callback.from_user.id
    
    print(
        callback.data
    )
    
    music_generate.gpt_prompt(callback.data)
    music_generate.ai_requsts()
    res_music = music_generate.res_music()
    
    bot.send_audio(id, audio=res_music['audio_url_0'], performer='Xamz_pok', title=res_music['title'])     

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)




