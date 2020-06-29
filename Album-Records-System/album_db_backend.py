# importing necessary modules
import sqlite3

def connect():
    # establish connection
    conn = sqlite3.connect("albums.db")
    cur = conn.cursor()
    #creating table if it doesn't exist already
    cur.execute("CREATE TABLE IF NOT EXISTS album (id INTEGER PRIMARY KEY, title text, artist text, year INTEGER, label text)")
    # datatable must be commit
    conn.commit()
    conn.close()

# insert function
def insert_data(title, artist, year, label):
    conn = sqlite3.connect("albums.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO album VALUES (NULL,?,?,?,?)",(title,artist,year,label))
    conn.commit()
    conn.close()

# set a default value incase user doesn't enter in all fields
def search_database(title="", artist="", year="", label=""):
    conn = sqlite3.connect("albums.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM album WHERE title=? OR artist=? OR year=? OR label=?", (title,artist,year,label))
    rows = cur.fetchall()
    # close connection
    conn.close()
    return rows
def update_record(id, title, artist, year, label):
    conn = sqlite3.connect("albums.db")
    cur = conn.cursor()
    cur.execute("UPDATE album SET title=?, artist=?, year=?, label=? WHERE id=?", (title,artist,year,label,id))
    conn.commit()
    conn.close()

def view_data():
    conn = sqlite3.connect("albums.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM album")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("albums.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM album WHERE id=?", (id,))
    conn.commit()
    conn.close()

connect()
# example of pre-exiting data
insert_data('Street OT', 'Olamide', 2014, 'YBNL')
insert_data('Radio', 'LL Cool J', 1985, 'Def Jam')
insert_data('My Beautiful Dark Twisted Fantasy', 'Kanye West', 2010, 'Def Jam, Roc-A-Fella')
insert_data('The Carter', 'Lil Wayne', 2008, 'Cash Money')
insert_data('Eyan Mayweather', 'Olamide', 2015, 'YBNL')


# print(search(year=2020))
# print(search_database(artist="Burna"))
