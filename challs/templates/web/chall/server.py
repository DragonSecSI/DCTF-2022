from flask import Flask, render_template, request
from flask_restful import Api
import sqlite3

app = Flask(__name__)
api = Api(app)

def db_insert(name, obj, quantity):
    con = sqlite3.connect('shopping_list.db')
    cur = con.cursor()
    cur.execute("INSERT INTO ShoppingList VALUES ('" + name + "', '" + obj + "', '" + quantity + "')")
    con.commit()
    con.close()

def db_select(name):
    con = sqlite3.connect('shopping_list.db')
    cur = con.cursor()
    rows = cur.execute("SELECT * FROM ShoppingList WHERE User = '" + name + "'")
    print(rows.arraysize)
    rows = [
        {
            "name": row[0],
            "obj": row[1],
            "quantity": row[2],
        }
        for row in rows
    ]
    con.commit()
    con.close()
    return rows

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        obj = request.form["object"]
        quantity = request.form["quantity"]
        if name is not None and obj is not None and quantity is not None:
            db_insert(name, obj, quantity)

    name = request.args.get("name")
    shopping_list = None
    if name is not None:
        shopping_list = db_select(name)
        if len(shopping_list) == 0:
            shopping_list = None
    return render_template(
        "index.html",
        name=name,
        shopping_list=shopping_list,
    )

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=80,
        debug=False,
    )
