import logging
import unittest


logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                        format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_walk(self):
        try:
            runner_obj = Runner("TestRunnerObj", -5)

            for i in range(10):
                runner_obj.walk()
            self.assertEqual(runner_obj.distance, 50)

            logger.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logger.warning("Неверная скорость для Runner: %s", e)


    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_run(self):
        try:
            runner_obj = Runner(2)
            for _ in range(10):
                runner_obj.run()
            self.assertEqual(runner_obj.distance, 100)
            logger.info('"test_run" выполнен успешно')
        except TypeError as e:
            logger.warning("Неверный тип данных для объекта Runner: %s", e)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_challenge(self):
        runner_obj_1 = Runner("TestRunnerObj1")
        runner_obj_2 = Runner("TestRunnerObj2")
        for _ in range(10):
            runner_obj_1.run()
            runner_obj_2.walk()
        self.assertNotEqual(runner_obj_1.distance, runner_obj_2.distance)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                        format="%(asctime)s | %(levelname)s | %(message)s")
    unittest.main()
