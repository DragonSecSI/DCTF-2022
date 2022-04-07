#!/usr/bin/python3

from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

@app.route("/license_check")
def licenseCheck():

    con = sqlite3.connect("ctf.db")
    cur = con.cursor()
    try:
        lice = request.args.get("license_key")
        query = "SELECT * FROM license_keys WHERE license_key = '" + lice + "';"


        cur.execute(query)
        res = cur.fetchall()
    
        cur.close()
        con.close()
    except Exception as e:
        cur.close()
        con.close()
        return str(e), 500

    return str(res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
