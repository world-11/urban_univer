import runner_and_tournament
import unittest


class TournamentTest(unittest.TestCase):
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
    def test_tour(self):
        self.tournament_1 = runner_and_tournament.Tournament(90, self.q, self.e)  # создаем объект класса Забег
        self.all_results = self.tournament_1.start()  # в словарь all_result записываем результат функции (место:участн)
        last_runner_name = self.all_results[max(self.all_results.keys())].name  # записываем имя с максимальным местом
        self.assertTrue(last_runner_name == 'Ник')  # вызываем юнит-метод сравнения
        TournamentTest.all_results[1] = self.all_results   #записываем словарь с ключом 1

    def test_tour_1(self):
        self.tournament_1 = runner_and_tournament.Tournament(90, self.e, self.w, self.q)
        self.all_results = self.tournament_1.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[2] = self.all_results

    def test_tour_2(self):
        self.tournament_1 = runner_and_tournament.Tournament(90, self.e, self.w)
        self.all_results = self.tournament_1.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[3] = self.all_results