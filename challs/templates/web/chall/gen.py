import sqlite3

con = sqlite3.connect("shopping_list.db")

cur = con.cursor()
cur.execute('''CREATE TABLE ShoppingList(User text, Obj text, Quantity text)''')
con.commit()

cur = con.cursor()
cur.execute('''INSERT INTO ShoppingList VALUES ('SuperSecretGuestUserThatNooneWillGuess', 'DCTF{template_web}', 'Vsaj 6')''')
con.commit()
