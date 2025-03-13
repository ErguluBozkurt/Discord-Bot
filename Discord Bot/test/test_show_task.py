import unittest
from database import get_db_connection

class TestShowTasks(unittest.TestCase):
    def setUp(self):
        self.conn = get_db_connection()
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, description TEXT, completed INTEGER)")

    def tearDown(self):
        self.c.execute("DROP TABLE IF EXISTS tasks")
        self.conn.close()

    def test_show_tasks(self):
        self.c.execute("INSERT INTO tasks (description, completed) VALUES (?, ?)", ("Test Task 1", 0))
        self.c.execute("INSERT INTO tasks (description, completed) VALUES (?, ?)", ("Test Task 2", 1))
        self.conn.commit()
        self.c.execute("SELECT * FROM tasks")
        tasks = self.c.fetchall()
        self.assertEqual(len(tasks), 2, "Tasks could not be displayed correctly.")

if __name__ == '__main__':
    unittest.main()