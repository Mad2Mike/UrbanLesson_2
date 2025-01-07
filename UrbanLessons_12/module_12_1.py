import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 200

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_walk(self):
        runner_obj = Runner("TestRunnerObj")

        for i in range(10):
            runner_obj.walk()
        self.assertEqual(runner_obj.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_run(self):
        runner_obj = Runner("TestRunnerObj")
        for _ in range(10):
            runner_obj.run()
        self.assertEqual(runner_obj.distance, 2000)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_challenge(self):
        runner_obj_1 = Runner("TestRunnerObj1")
        runner_obj_2 = Runner("TestRunnerObj2")
        for _ in range(10):
            runner_obj_1.run()
            runner_obj_2.walk()
        self.assertNotEqual(runner_obj_1.distance, runner_obj_2.distance)

if __name__ == '__main__':
    unittest.main()