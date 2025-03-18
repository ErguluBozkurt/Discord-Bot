import unittest
from database import get_db_connection

class TestCompleteTask(unittest.TestCase):
    def setUp(self):
        self.conn = get_db_connection()
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, description TEXT, completed INTEGER)")

    def tearDown(self):
        self.c.execute("DROP TABLE IF EXISTS tasks")
        self.conn.close()

    def test_complete_task(self):
        self.c.execute("INSERT INTO tasks (description, completed) VALUES (?, ?)", ("Test Task", 0))
        self.conn.commit()
        task_id = self.c.lastrowid
        self.c.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        self.conn.commit()
        self.c.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        task = self.c.fetchone()
        self.assertEqual(task['completed'], 1, "Mission not completed.")
    
        
if __name__ == '__main__':
    unittest.main()
