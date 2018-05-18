from converter import EnglishtoMorse
from converter import MorseToEnglish


class ConverterApp:
    def __init__(self):
        self.getEnglishToMorse = EnglishtoMorse.EnglishConverter()
        self.getMorseToEnglish = MorseToEnglish.MorseConverter()

    def main(self):
        filename = input('Select 1 for Morse to English and Select 2 for English to Morse')
        morseValue = "--. . . -.- ... -....- ..-. --- .-. -....- --. . . -.- ..."
        englishWord = "GEEKS-FOR-GEEKS"
        self.getMorseToEnglish.morseValue = morseValue
        result = self.getMorseToEnglish.getMorseToEnglish()

        self.getEnglishToMorse.englishWord = englishWord
        result = self.getEnglishToMorse.getEnglishToMorse()


converterApp = ConverterApp()
converterApp.main()
