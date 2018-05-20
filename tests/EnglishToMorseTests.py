import unittest
from converter import EnglishtoMorse


class EnglishToMorseTests(unittest.TestCase):
    def test_getoEnglishToMorse(self):
        inputValue = 'TAMPERE'
        self.getMorseToEnglish = EnglishtoMorse.EnglishConverter()
        self.getMorseToEnglish.englishWord = inputValue
        result = self.getMorseToEnglish.getEnglishToMorse()
        self.assertEqual(result, '- .- -- .--. . .-. . ')
