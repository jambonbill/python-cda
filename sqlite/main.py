#https://docs.python.org/3/library/sqlite3.html

import sqlite3
con = sqlite3.connect("tutorial.db")

try:
    cur = con.cursor()
    cur.execute("CREATE TABLE movie(title, year, score)")
except:
    print("CREATE TABLE pas glop")
else:
    print("CREATED")

res = cur.execute("SELECT name FROM sqlite_master")
r=res.fetchone()
print(r)

cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

con.commit()
#con.close()#c pour les pd

print("uppi")


