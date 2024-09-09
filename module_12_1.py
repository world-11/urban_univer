import unittest
import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        q = Runner.Runner('Петр')
        for i in range(10):
            q.walk()
        self.assertEqual(q.distance, 50)
        
    def test_run(self):
        Sergey = Runner.Runner('Сергей')
        for i in range(10):
            Sergey.run()
        self.assertEqual(Sergey.distance, 100)
        
    def test_challenge(self):
        Mitya = Runner.Runner('Митя')
        Egor = Runner.Runner('Егор')
        for i in range(10):
            Mitya.run()
            Egor.walk()
            self.assertNotEqual(Mitya.distance, Egor.distance)

if __name__ == '__main__':
    unittest.main()