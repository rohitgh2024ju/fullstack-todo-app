import sqlite3 as sql


def get_connection():
    conn = sql.connect("tasks.db")
    cur = conn.cursor()

    cur.execute(
        """
    CREATE TABLE IF NOT EXISTS tasks_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        date TEXT,
        is_critical BOOLEAN
    )
    """
    )

    conn.commit()
    return conn


def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
create table if not exists tasks_table(
                id integer primary key autoincrement,
                name text not null,
                datetime text not null,
                is_critical integer)
"""
    )
