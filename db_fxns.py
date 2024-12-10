import sqlite3


#database
#table
#field/columns
#datatypes

def create_table():
  conn = sqlite3.connect('todo.db')
  c = conn.cursor()
  c.execute(
    '''CREATE TABLE IF NOT EXISTS tasks_table(
      task_id INTEGER PRIMARY KEY AUTOINCREMENT,
      task_name TEXT,
      task_status TEXT,
      task_due_date DATE
    )'''
  )

def insert_data(task_name, task_status, task_due_date):
  conn = sqlite3.connect('todo.db')
  c = conn.cursor()
  c.execute(
    '''INSERT INTO tasks_table(
      task_name, 
      task_status, 
      task_due_date)
      VALUES(?,?,?)
    ''',
    (task_name, task_status, task_due_date)
    )
  conn.commit()


def read_data():
  conn = sqlite3.connect('todo.db')
  c = conn.cursor()
  c.execute('SELECT * FROM tasks_table')
  data = c.fetchall()
  return data


def read_not_started():
  conn = sqlite3.connect('todo.db')
  c = conn.cursor()
  c.execute("SELECT task_name, task_status FROM tasks_table WHERE task_status LIKE 'Not Started'")
  data = c.fetchall()
  return data


def read_tasknames():
  conn = sqlite3.connect('todo.db')
  c = conn.cursor()
  c.execute("SELECT DISTINCT task_name FROM tasks_table")
  data = c.fetchall()
  return data

def get_tasks_by_name(task):
  conn = sqlite3.connect('todo.db')
  c = conn.cursor()
  c.execute("""
    SELECT * 
    FROM 
    tasks_table WHERE task_name LIKE ?
    """, [(task)]
    # tasks_table WHERE task_name task LIKE "{}".format(task)
  )
  data = c.fetchall()
  return data



def get_task_by_id(id):
  conn = sqlite3.connect('todo.db')
  c = conn.cursor()
  c.execute("""
    SELECT * 
    FROM 
    tasks_table WHERE task_id = ?
    """, [(id)]
    # tasks_table WHERE task_name task LIKE "{}".format(task)
  )
  data = c.fetchall()
  return data

def update_data(task_id, task_name, task_status, task_due_date):
  conn = sqlite3.connect('todo.db')
  c = conn.cursor()
  c.execute("""
    UPDATE tasks_table
    SET task_name = ?, task_status = ?, task_due_date = ?
    WHERE task_id = ?
    """, (task_name, task_status, task_due_date, task_id)
  )
  conn.commit()

def delete_data(task_id):
  conn = sqlite3.connect('todo.db')
  c = conn.cursor()
  c.execute("""
    DELETE FROM tasks_table
    WHERE task_id = ?
    """, (task_id,)
  )
  conn.commit()

