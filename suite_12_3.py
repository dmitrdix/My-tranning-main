import unittest






class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

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

class RunnerTest(unittest.TestCase,Runner):
    is_frozen=False
    @unittest.skipIf(is_frozen==True,'Тесты в этом кейсе заморожены')

    def test_walk(self):
        tw = Runner('tw')
        for i in range(10):
            tw.walk()
        self.assertEqual(tw.distance, 50)

    @unittest.skipIf(is_frozen==True, 'Тесты в этом кейсе заморожены')

    def test_run(self):
        tr = Runner('tr')
        for i in range(10):
            tr.run()
        self.assertEqual(tr.distance, 100)

    @unittest.skipIf(is_frozen==True, 'Тесты в этом кейсе заморожены')

    def test_challenge(self):
        tc1 = Runner('tc1')
        tc2 = Runner('tc2')
        for i in range(10):
            tc1.run()
            tc2.walk()
        self.assertNotEqual(tc1.distance,tc2.distance)


if __name__ == '__main__':
    unittest.main()

class TournamentTest(unittest.TestCase):
    is_frozen = True


    @classmethod
    def setUpClass(cls):
        cls.all_results={}



    def setUp(self):
        self.first = Runner('Усэйн', 10)
        self.second = Runner('Андрей', 9)
        self.third = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            new_result = {}
            for key, value in result.items():
                new_result[key] = value.name
            print(new_result)

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_run_1(self):
        self.tournament_1 = Tournament(90, self.first, self.third)

        self.all_results = self.tournament_1.start()

        last_1 = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_1, 'Ник')
        TournamentTest.all_results[1] = self.all_results

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')

    def test_run_2(self):
        self.tournament_2 = Tournament(90, self.second, self.third)

        self.all_results = self.tournament_2.start()

        last_2 = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_2, 'Ник')
        TournamentTest.all_results[2] = self.all_results

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')

    def test_run_3(self):
        self.tournament_3 = Tournament(90, self.first,self.second, self.third)

        self.all_results = self.tournament_3.start()

        last_3 = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_3, 'Ник')
        TournamentTest.all_results[3] = self.all_results


if __name__ == '__main__':
    unittest.main()