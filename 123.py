from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='7c94879680794bb8aeb5e7d512c905ed')
#
# # /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          #sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')
a=[]
print(len(a))
for i in range(len(top_headlines['articles'])):
    print(top_headlines['articles'][i]['url'])


# # # /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2017-12-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)
#
# # /v2/sources
# sources = newsapi.get_sources()

    #if message.text in list_reg:
    #    message.from_user.id
        #Записывание в бд
# sql блок
# conn = sqlite3.connect('Baby_baza.db')
# cur = conn.cursor()
# #cur.execute("ВАШ-SQL-ЗАПРОС-ЗДЕСЬ;")
#
# telegramid=input("Введите id: ")
# #cur.execute("SELECT MAX(userid) FROM users")
# #cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
# cur.execute("INSERT INTO users (telegramid) VALUES (?)", (telegramid,))
# conn.commit()
# conn.close()

# @bot.message_handler(content_types=['text'])
# def send_text(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, 'Привет, мой создатель')
#     elif message.text.lower() == 'пока':
#         bot.send_message(message.chat.id, 'Прощай, создатель')


# import telebot
# from keyboa import Keyboa
#
#
# bot = telebot.TeleBot("1798201326:AAHtUNRB6vkhOADDoKT7J5UY31hlqAfW4Ow", parse_mode=None)

# menu = ["spam", "eggs", "ham"]
# keyboard = Keyboa(items=menu).keyboard
# @bot.message_handler(commands=['start', 'help'])
# def handle_start_welcome(message):
# 	bot.reply_to(message, "FPFPFPF")
#
# @bot.message_handler(func=lambda message: True)
# def answer_to_message(message):
#     bot.send_message(chat_id=message.from_user.id, text='text', reply_markup=keyboard)

# fruitscomplex = [
#   "banana",
#   ["coconut", "orange"],
#   ["peach", "apricot", "apple"],
#   "pineapple",
#   ["avocado", "melon"],
# ]
#
# kb_fruits_complex = keyboa_maker(items=fruits_complex, copy_text_to_callback=True)
#
# bot.send_message(
#   chat_id=uid, reply_markup=kb_fruits_complex,
#   text="Please select one of the fruit:")
#
# bot.polling()