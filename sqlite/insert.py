#https://docs.python.org/3/library/sqlite3.html

import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()  # Remember to commit the transaction after executing INSERT.

print("Youpi")
