from data import SymbolsData


class EnglishConverter:

    def __init__(self):
        self.symbolData = SymbolsData.Mapping()
        self._englishWord = ""

    # getter method
    @property
    def englishWord(self):
        return self._englishWord

    # setter method
    @englishWord.setter
    def englishWord(self, _englishWord):
        self._englishWord = _englishWord

    # method convert english to morse
    def getEnglishToMorse(self):
        morseCodeDict = self.symbolData.getCodes
        morseCode = ''
        for letter in self._englishWord:
            if letter != ' ':
                morseCode += morseCodeDict[letter] + ' '
            else:
                morseCode += ' '

        return morseCode
