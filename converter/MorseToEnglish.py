from data import SymbolsData


class Converter:

    def __init__(self):
        self.symbolData = SymbolsData.Mapping()
        self._morseCode = ''
        self.Word_Value = 1
        self.Character_Value = 2

    # getter method
    @property
    def morseValue(self):
        return self._morseCode

    # setter method
    @morseValue.setter
    def morseValue(self, _morseCode):
        self._morseCode = _morseCode

    # method converts morse to english
    def getMorseToEnglish(self):
        morseCodeDict = self.symbolData.getCodes
        self._morseCode += ' '

        word = ''
        singleCharacter = ''
        countSpaces = 0
        for letter in self._morseCode:

            # checks for space
            if (letter != ' '):

                # counter to keep track of space
                countSpaces = 0

                # storing morse code of a single character
                singleCharacter += letter

            # in case of space
            else:
                # if countSpaces = 1 that indicates a new character
                countSpaces += self.Word_Value

                # if countSpaces = 2 that indicates a new word
                if countSpaces == self.Character_Value:

                    # adding space to separate words
                    word += ' '
                elif singleCharacter is not '/':

                    # accessing the keys using their values (reverse of encryption)
                    if singleCharacter in morseCodeDict.values():
                        word += list(morseCodeDict.keys())[list(morseCodeDict
                                                                .values()).index(singleCharacter)]
                    else:
                        word = 'NotValid'
                    singleCharacter = ''
                else:
                    singleCharacter = ''
                    word += ' '
        return word
