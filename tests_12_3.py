import runner_and_tournament
import unittest
import Runner


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.q = runner_and_tournament.Runner('Усейн', 10)
        self.w = runner_and_tournament.Runner('Андрей', 9)
        self.e = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results:
            # print(cls.all_results[key].items())
            for key, value in cls.all_results[key].items():
                print(f'{key}: {value}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour(self):
        self.tournament_1 = runner_and_tournament.Tournament(90, self.q, self.e)  # создаем объект класса Забег
        self.all_results = self.tournament_1.start()  # в словарь all_result записываем результат функции (место:участн)
        last_runner_name = self.all_results[max(self.all_results.keys())].name  # записываем имя с максимальным местом
        self.assertTrue(last_runner_name == 'Ник')  # вызываем юнит-метод сравнения
        TournamentTest.all_results[1] = self.all_results   #записываем словарь с ключом 1

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour_1(self):
        self.tournament_1 = runner_and_tournament.Tournament(90, self.e, self.w, self.q)
        self.all_results = self.tournament_1.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[2] = self.all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour_2(self):
        self.tournament_1 = runner_and_tournament.Tournament(90, self.e, self.w)
        self.all_results = self.tournament_1.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[3] = self.all_results


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        q = Runner.Runner('Петр')
        for i in range(10):
            q.walk()
        self.assertEqual(q.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        Sergey = Runner.Runner('Сергей')
        for i in range(10):
            Sergey.run()
        self.assertEqual(Sergey.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        Mitya = Runner.Runner('Митя')
        Egor = Runner.Runner('Егор')
        for i in range(10):
            Mitya.run()
            Egor.walk()
            self.assertNotEqual(Mitya.distance, Egor.distance)

if __name__ == '__main__':
    unittest.main()