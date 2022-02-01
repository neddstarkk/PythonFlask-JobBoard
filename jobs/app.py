from distutils.util import execute
from email.policy import default
from flask import Flask, render_template, g
import sqlite3

PATH = '../db/job.sqlite'

app = Flask(__name__)

def open_connection():
    connection = getattr(g, '_connection', default=None)

    if connection is None:
        connection = g._connection = sqlite3.connect(PATH)
    
    connection.row_factory = sqlite3.Row

    return connection


def execute_sql(sql, values = (), commit = False, single = False):
    connection = open_connection() 

    cursor = connection.execute(sql, values)

    if commit == True:
        results = connection.commit()
    else:
        results = cursor.fetchone() if single else cursor.fetchall()

    cursor.close()

    return results

@app.route("/")
@app.route("/jobs")
def jobs():
    return render_template('index.html')
