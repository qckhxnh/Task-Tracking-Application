import psycopg2
from typing import List
import datetime
from model import Todo

def connect():
    def create_connection():
        conn = psycopg2.connect(
            host="localhost",
            database="database",
            user="postgres",
            password="Quockhanh2004@"
        )
        if conn:
            print("Connected to the database")
        else:
            print("Failed to connect to the database")
        return conn
    conn = create_connection()
    cur = conn.cursor()
    return cur, conn
cur, conn = connect()


def create_table():
    cur.execute("""CREATE TABLE IF NOT EXISTS todos (
            task text,
            category text,
            date_added timestamp,
            date_completed timestamp,
            status integer,
            position integer
            )""")
    conn.commit()

create_table()

def insert_todo(todo: Todo):
    cur.execute('SELECT COUNT(*) FROM todos')
    count = cur.fetchone()[0]
    todo.position = count if count else 0
    with conn:
        cur.execute('INSERT INTO todos VALUES (%s, %s, %s, %s, %s, %s)',
                  (todo.task, todo.category, todo.date_added,
                   todo.date_completed, todo.status, todo.position))

def get_all_todos() -> List[Todo]:
    cur.execute('SELECT * FROM todos')
    results = cur.fetchall()
    todos = []
    for result in results:
        todos.append(Todo(*result))
    return todos


def delete_todo(position):
    cur.execute('SELECT COUNT(*) FROM todos')
    count = cur.fetchone()[0]

    with conn:
        c.execute("DELETE FROM todos WHERE position=%s", (position,))
        for pos in range(position+1, count):
            change_position(pos, pos-1, False)


def change_position(old_position: int, new_position: int, commit=True):
    cur.execute('UPDATE todos SET position = %s WHERE position = %s',
              (new_position, old_position))
    if commit:
        conn.commit()


def update_todo(position: int, task: str, category: str):
    with conn:
        if task is not None and category is not None:
            c.execute('UPDATE todos SET task = %s, category = %s WHERE position = %s',
                      (task, category, position))
        elif task is not None:
            c.execute('UPDATE todos SET task = %s WHERE position = %s',
                      (task, position))
        elif category is not None:
            c.execute('UPDATE todos SET category = %s WHERE position = %s',
                      (category, position))


def complete_todo(position: int):
    with conn:
        c.execute('UPDATE todos SET status = 2, date_completed = %s WHERE position = %s',
                  (datetime.datetime.now(), position))

# Don't forget to close the cursor and connection when you're done
# conn.close()
