from backend.app.database import get_connection


def add_task(name, date, is_critical):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tasks_table (name, date, is_critical) VALUES (?, ?, ?)",
        (name, date, is_critical),
    )
    conn.commit()
    conn.close()


def fetch_tasks():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, date, is_critical FROM tasks_table")
    rows = cur.fetchall()
    conn.close()

    tasks = []
    for row in rows:
        task = {
            "id": row[0],
            "name": row[1],
            "date": row[2],
            "is_critical": bool(row[3])
        }
        tasks.append(task)

    return tasks



def delete_task(task_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks_table WHERE id = ?", (task_id,))
    conn.commit()
    rows_deleted = cur.rowcount
    conn.close()
    return rows_deleted


