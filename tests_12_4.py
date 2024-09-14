import logging
import unittest
import runner_1

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            q = runner_1.Runner('Петр', -3)
            for i in range(10):
                q.walk()
            self.assertEqual(q.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as ve:
            logging.warning(f'Неверная скорость для Runner', exc_info=True)


    def test_run(self):
        try:
            Sergey = runner_1.Runner(444, 6)
            for i in range(10):
                Sergey.run()
            self.assertEqual(Sergey.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as te:
            logging.warning(f'Неверный тип данных для объекта Runner', exc_info=True)


    def test_challenge(self):
        Mitya = runner_1.Runner('Митя')
        Egor = runner_1.Runner('Егор')
        for i in range(10):
            Mitya.run()
            Egor.walk()
            self.assertNotEqual(Mitya.distance, Egor.distance)


logging.basicConfig(filename='runner_test.log',
                    filemode='w',
                    level=logging.INFO,
                    encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s | %(message)s | %(filename)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')

if __name__ == '__main__':
    unittest.main()