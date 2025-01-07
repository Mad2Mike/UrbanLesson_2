import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed
        self.iterations = 0

    def run(self):
        self.distance += self.speed * 2
        self.iterations += 1

    def __str__(self):
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

        finishers = []

        while self.participants:
            for participant in self.participants[:]:
                participant.run()
                if participant.distance >= self.full_distance:

                    finishers.append(participant)
                    self.participants.remove(participant)


        finishers.sort(key=lambda x: x.iterations)
        results = {index + 1: runner.name for index, runner in enumerate(finishers)}

        return results


# runner1 = Runner("Усэйн", 10)
# runner2 = Runner("Андрей", 9)
# runner3 = Runner("Ник", 3)
#
# tournament1 = Tournament(90, runner1, runner3)
# results1 = tournament1.start()
# for index, (key, value) in enumerate(results1.items()):
#     print(f" Место: {key}, Бегинер: {value}")
#
# tournament2 = Tournament(90, runner2, runner3)
# results2 = tournament2.start()
# for index, (key, value) in enumerate(results2.items()):
#     print(f" Место: {key}, Бегинер: {value}")
#
# tournament3 = Tournament(90, runner1, runner2, runner3)
# results3 = tournament3.start()
# for index, (key, value) in enumerate(results3.items()):
#     print(f" Место: {key}, Бегинер: {value}")



class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.allResults = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.allResults.keys()):
            print(cls.allResults[key])


    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.allResults[len(self.allResults) + 1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.allResults[len(self.allResults) + 1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены'")
    def test_3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.allResults[len(self.allResults) + 1] = results
        self.assertTrue(results[max(results.keys())] == "Ник")


if __name__ == '__main__':
    unittest.main()
