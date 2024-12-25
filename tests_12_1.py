import unittest

class Runner:
    def __init__(self, name):
        self.name=name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase,Runner):
    def test_walk(self):
        tw = Runner('tw')
        for i in range(10):
            tw.walk()
        self.assertEqual(tw.distance, 50)

    def test_run(self):
        tr = Runner('tr')
        for i in range(10):
            tr.run()
        self.assertEqual(tr.distance, 100)

    def test_challenge(self):
        tc1 = Runner('tc1')
        tc2 = Runner('tc2')
        for i in range(10):
            tc1.run()
            tc2.walk()
        self.assertNotEqual(tc1.distance,tc2.distance)


if __name__ == '__main__':
    unittest.main()