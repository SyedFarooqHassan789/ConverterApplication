import unittest
import CoverterApp as converterMain


class EnglishToMorseTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(EnglishToMorseTests, self).__init__(*args, **kwargs)
        self.MORSE_TO_ENGLISH = 1
        self.ENGLISH_TO_MORSE = 2
        self.getConveterApp = converterMain.ConverterApp()

    def test_validation(self):
        inputValueMorse = '... ...'
        inputValueEnglishWord = 'Tampere'
        isValidMorse = self.getConveterApp.validation(self.MORSE_TO_ENGLISH, inputValueMorse)
        isValidEnglishWord = self.getConveterApp.validation(self.ENGLISH_TO_MORSE, inputValueEnglishWord)
        self.assertEqual(isValidMorse, True)
        self.assertEqual(isValidEnglishWord, True)

    def test_handlingSelection(self):
        inputValueMorse = '- .- -- .--. . .-. .'
        inputValueEnglishWord = 'Oulu'
        resultMorse = self.getConveterApp.handlingSelection(self.MORSE_TO_ENGLISH, inputValueMorse)
        self.assertEqual(resultMorse, 'TAMPERE')
        resultMorse = self.getConveterApp.handlingSelection(self.ENGLISH_TO_MORSE, inputValueEnglishWord)
        self.assertEqual(resultMorse, '--- ..- .-.. ..- ')
