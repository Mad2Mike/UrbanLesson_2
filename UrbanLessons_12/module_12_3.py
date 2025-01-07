import unittest

from UrbanLessons_12 import module_12_2
from UrbanLessons_12 import module_12_1

tournamentSt = unittest.TestSuite()

tournamentSt.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))
tournamentSt.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))

test_runner = unittest.TextTestRunner(verbosity=3)
test_runner.run(tournamentSt)