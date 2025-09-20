import sqlite3

conn = sqlite3.connect('bookvault.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS admins (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
)
''')

cursor.execute('''
INSERT OR IGNORE INTO admins (username, password)
VALUES ('BOOKVAULT_USER', 'b1')
''')

conn.commit()
conn.close()
