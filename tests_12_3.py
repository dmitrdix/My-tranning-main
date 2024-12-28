import unittest
import suite_12_3


calcST = unittest.TestSuite()
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(suite_12_3.RunnerTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(suite_12_3.TournamentTest))


runner = unittest.TextTestRunner(verbosity=2 )
runner.run(calcST)