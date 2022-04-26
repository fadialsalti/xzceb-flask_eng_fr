import unittest
from translator import frenchToEnglish, englishToFrench

class Testf2e(unittest.TestCase):
    """ Test french to english """
    def test_1(self):
        self.assertEqual(frenchToEnglish('0'), '0')
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertNotEqual(frenchToEnglish("None"), '')


class Teste2f(unittest.TestCase):
    """ Test english to french """
    def test_1(self):
        self.assertEqual(englishToFrench('0'), '0')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench("None"), '')

unittest.main()