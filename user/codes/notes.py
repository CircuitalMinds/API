import sqlite3
import markdown
from flask import Flask, render_template, request, flash, redirect, url_for


def init_db():
    import sqlite3

    connection = sqlite3.connect('database.db')

    with open('schema.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    cur.execute("INSERT INTO notes (content) VALUES (?)", ('# The First Note',))
    cur.execute("INSERT INTO notes (content) VALUES (?)", ('_Another note_',))
    cur.execute("INSERT INTO notes (content) VALUES (?)",
                ('Visit [this page](https://www.digitalocean.com/community/tutorials) for more tutorials.',))

    connection.commit()
    connection.close()


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)
app.config['SECRET_KEY'] = 'this should be a secret random string'


@app.route('/')
def index():
    conn = get_db_connection()
    db_notes = conn.execute('SELECT id, created, content FROM notes;').fetchall()
    conn.close()

    notes = []
    for note in db_notes:
       note = dict(note)
       note['content'] = markdown.markdown(note['content'])
       notes.append(note)

    return render_template('index.html', notes=notes)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    conn = get_db_connection()

    if request.method == 'POST':
        content = request.form['content']
        if not content:
            flash('Content is required!')
            return redirect(url_for('index'))
        conn.execute('INSERT INTO notes (content) VALUES (?)', (content,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create.html')
