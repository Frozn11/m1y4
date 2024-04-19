import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 


@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username:
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img()) 
        try:
            bot.send_message(message.chat.id, pokemon.achievements())
        except Exception as e:
            print(f'Hell no: {e}')
            pass
        print()        
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")


bot.infinity_polling(none_stop=True)

