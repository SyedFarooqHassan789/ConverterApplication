from data import SymbolsData


class EnglishToMorse:

    def __init__(self):
        self.symbolData = SymbolsData.Mapping()

    def getEnglishToMorse(self, message):
        MORSE_CODE_DICT = self.symbolData
        cipher = ''
        for letter in message:
            if letter != ' ':

                # Looks up the dictionary and adds the
                # correspponding morse code
                # along with a space to separate
                # morse codes for different characters
                cipher += MORSE_CODE_DICT[letter] + ' '
            else:
                # 1 space indicates different characters
                # and 2 indicates different words
                cipher += ' '

        return cipher
