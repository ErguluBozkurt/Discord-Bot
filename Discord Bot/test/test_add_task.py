import unittest
from database import get_db_connection

class TestAddTask(unittest.TestCase):
    def setUp(self):
        self.conn = get_db_connection()
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, description TEXT, completed INTEGER)")

    def tearDown(self):
        self.c.execute("DROP TABLE IF EXISTS tasks")
        self.conn.close()

    def test_add_task(self):
        self.c.execute("INSERT INTO tasks (description, completed) VALUES (?, ?)", ("Test Task", 0))
        self.conn.commit()
        self.c.execute("SELECT * FROM tasks WHERE description = ?", ("Test Task",))
        task = self.c.fetchone()
        self.assertIsNotNone(task, "Failed to add a task.")
        
    def test_add_long_description_task(self):
        long_description = "a" * 256
        with self.assertRaises(ValueError):
            self.c.execute("INSERT INTO tasks (description, completed) VALUES (?, ?)", (long_description, 0))
            self.conn.commit()
            
if __name__ == '__main__':
    unittest.main()
