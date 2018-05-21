import unittest
from converter import MorseToEnglish


class MorseToEnglishTests(unittest.TestCase):
    def test_getMorseToEnglish(self):
        inputValue = '- .- -- .--. . .-. .'
        self.getMorseToEnglish = MorseToEnglish.Converter()
        self.getMorseToEnglish.morseValue = inputValue
        result = self.getMorseToEnglish.getMorseToEnglish()
        self.assertEqual(result, 'TAMPERE')
