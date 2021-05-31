import sqlite3



conn = sqlite3.connect('Baby_baza.db')
cur = conn.cursor()
#cur.execute("ВАШ-SQL-ЗАПРОС-ЗДЕСЬ;")

telegramid=input("Введите id: ")
#cur.execute("SELECT MAX(userid) FROM users")
#cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
cur.execute("INSERT INTO users (id_telegram) VALUES (?)", (telegramid,))
conn.commit()
conn.close()