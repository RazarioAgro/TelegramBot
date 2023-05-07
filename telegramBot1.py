import telebot
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("tokentel")
bot = telebot.TeleBot(token)

questions = ["Столица России?", "Самое большое озеро в мире?", "Самый популярный спорт в мире?"]
answ = [
    ['Египет', 'Москва', 'Лондон', 'Париж'],
    ['Каспиское море', 'Виктория', 'Енисей', 'Байкал'],
    ['Гольф', 'Хокей', 'Футбол', 'Бадминтон']
]
right = [2,1,3]
money = 100
i = 0

@bot.message_handler(content_types=['text'])
def get_text_messange(messange):
  global i, money
  body = messange.text
  if i == 0 or body == str(right[i-1]):
    if i != 0:
      money *= 2
      mess = 'Ваш выйграш: ' + str(money)
      bot.send_message(messange.from_user.id, mess)
    if i == 3:
      bot.send_message(messange.from_user.id, "Игра окончена")
      i = 0
    
    mess = questions[i] + '\n' + '1.' + answ[i][0]+'\n'+'2.'+answ[i][1]+'\n'+'3.'+answ[i][2]+'\n'+'4.'+answ[i][3]+'\n'+'Ответ пишется цифрой!'
    bot.send_message(messange.from_user.id, mess)
    i += 1
  else:
    bot.send_message(messange.from_user.id, "Вы проиграли")

bot.polling(none_stop=True, interval=0)
