import sqlite3
connention = sqlite3.connect('data.db')
cursor=connention.cursor()
create_table="CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,username text,password text)"
cursor.execute(create_table)
create_table="CREATE TABLE IF NOT EXISTS items(name text,price real)"
cursor.execute(create_table)


connention.commit()
connention.close()