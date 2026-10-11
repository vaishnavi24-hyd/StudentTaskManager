
import unittest
from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("Study Python")
        self.assertEqual(len(self.manager.view_tasks()), 1)

    def test_complete_task(self):
        self.manager.add_task("Study DSA")
        self.assertTrue(self.manager.complete_task(0))

    def test_invalid_task(self):
        self.assertFalse(self.manager.complete_task(5))


if __name__ == "__main__":
    unittest.main()
