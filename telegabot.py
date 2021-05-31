import telebot
import sqlite3
from newsapi import NewsApiClient
# from keyboa import Keyboa
# from keyboa import Button
from telebot import types

# import keyboa
# from telebot.types import ReplyKeyboardMarkup

newsapi = NewsApiClient(api_key='7c94879680794bb8aeb5e7d512c905ed')
list_hello = ("Привет", "Приветики")
bot = telebot.TeleBot("1798201326:AAHtUNRB6vkhOADDoKT7J5UY31hlqAfW4Ow", parse_mode=None)

conn = sqlite3.connect('Baby_baza.db', check_same_thread=False)
cur = conn.cursor()

# Создание списка с категориями
# cur.execute("SELECT * FROM categories")
# rows = cur.fetchall()
# all_categories = []
# for row in rows:
#     all_categories.append(row[1])
# keyboard_categories = Keyboa(items=all_categories, copy_text_to_callback=True).keyboard

@bot.message_handler(commands=['start', 'help'])
def handle_start_welcome(message):
    markup: ReplyKeyboardMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton('/help')
    item2 = types.KeyboardButton('Показать новости')
    item3 = types.KeyboardButton('/addcategories')
    item4 = types.KeyboardButton('/WantNews')
    markup.add(item1, item2, item3, item4)
    bot.reply_to(message,
                 '/help - помощь, /addcategories - добавить категорию новостей, /WantNews - подписаться на обновление новостей',
                 reply_markup=markup)

@bot.message_handler(commands=['WantNews'])
def WantNews(message):
    try:  # Проверка на наличие в БД
        users = [message.from_user.first_name, message.from_user.id]
        # cur.execute("SELECT users(id_telegram)")
        # one_result = cur.fetchone()
        cur.execute("INSERT INTO users(name, id_telegram) VALUES(?, ?)", users)
        conn.commit()
        bot.send_message(message.from_user.id, "Вы зарегистрированы")
    except:
        bot.send_message(message.from_user.id, "Вы уже зарегистрированы")


# Клавиатура категорий
@bot.message_handler(commands=['addcategories'])
def addcategories(message):
    # bot.send_message(chat_id=message.from_user.id, text='Выберите категории новостей:', reply_markup=keyboard_categories)
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton('business', callback_data='business')
    item2 = types.InlineKeyboardButton('entertainment', callback_data='entertainment')
    item3 = types.InlineKeyboardButton('general', callback_data='general')
    item4 = types.InlineKeyboardButton('health', callback_data='health')
    item5 = types.InlineKeyboardButton('science', callback_data='science')
    item6 = types.InlineKeyboardButton('sports', callback_data='sports')
    item7 = types.InlineKeyboardButton('technology', callback_data='technology')
    markup.add(item1, item2, item3, item4, item5, item6, item7)
    bot.send_message(message.from_user.id, 'XER', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    cur.execute("SELECT id_user FROM users WHERE id_telegram=?", [(call.message.chat.id)])
    id_user = cur.fetchone()
    if id_user is not None:
        try:
            if call.data:
                # Проверка на наличие категории у юзера
                cur.execute("SELECT id_user FROM users WHERE id_telegram=?", [(call.message.chat.id)])
                id_user = cur.fetchone()
                cur.execute("SELECT id_categories FROM categories WHERE categories=?", [(call.data)])
                id_categories = cur.fetchone()
                categories_user = (id_categories[0], id_user[0])
                cur.execute("SELECT * FROM usercat")
                categories_in_sql = cur.fetchall()
                # Добавление категории
                if categories_user not in categories_in_sql:
                    cur.execute("INSERT INTO usercat(id_categories, id_user) VALUES(?, ?)", categories_user)
                    conn.commit()
                    bot.send_message(call.message.chat.id, 'Категория ' + call.data + ' добавлена')
                else:
                    bot.send_message(call.message.chat.id, 'Категория ' + call.data + ' уже добавлена')
            else:
                print('Ничего')
                # bot.edit_message_text(chad_id=call.message.chat.id, message_id=call.message.message_id, text="KKK",
                #                        reply_markup=None)

                # bot.answer_callback_query(call.message.chat.id, show_alert=False, text='Это тестовое уведомление')
        except Exception as e:
            print(repr(e))
    else:
        bot.send_message(call.message.chat.id, 'Вы не зарегистрированы')

    # cur.execute("SELECT id_categories FROM categories WHERE categories=?", [(call.data)])
    # id_categories = cur.fetchone()
    # categories_user = (id_categories[0], id_user[0])
    # categories_in_sql = cur.fetchall()
    # Добавление категории

@bot.message_handler(func=lambda message: True)
def answer_to_message(message):
    # print(message.from_user.id)
    if message.text in list_hello:
        # print(type(message))
        bot.send_message(message.from_user.id, "И тебе привет")
        user = (message.from_user.id, message.from_user.first_name)
        # print(type(user[1]))
        # print(user)
    # Показ новостей
    if message.text == 'Показать новости':
        top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                                  category='business',
                                                  language='en',
                                                  country='us')

        if len(top_headlines['articles']) >= 10:
            bot.send_message(message.from_user.id, "Топ 10 новостей:")
            for i in range(10):
                url = top_headlines['articles'][i]['url']
                bot.send_message(message.from_user.id, url)
        elif len(top_headlines['articles']) == 0:
            bot.send_message(message.from_user.id, "Новостей нет")
        else:
            bot.send_message(message.from_user.id, "Топ " + str(len(top_headlines['articles'])) + ' новостей:')
            for i in range(len(top_headlines['articles'])):
                url = top_headlines['articles'][i]['url']
                bot.send_message(message.from_user.id, url)

bot.polling()
