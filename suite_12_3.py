import unittest
import runner_and_tournament
import Runner
import tests_12_3


# Часть 1. TestSuit
Tests_s = unittest.TestSuite()
Tests_s.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
Tests_s.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(Tests_s)

# Часть 2. Пропуск тестов
