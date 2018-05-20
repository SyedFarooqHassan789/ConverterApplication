from converter import EnglishtoMorse
from converter import MorseToEnglish
import re


class ConverterApp:
    def __init__(self):
        self.getEnglishToMorse = EnglishtoMorse.EnglishConverter()
        self.getMorseToEnglish = MorseToEnglish.MorseConverter()
        self.MORSE_TO_ENGLISH = 1
        self.ENGLISH_TO_MORSE = 2

    def main(self):
        while True:
            try:
                selection = int(input('Select 1 for Morse to English and Select 2 for English to Morse\n'))
            except ValueError:
                print("Wrong Input")
                continue
            else:
                break
        self.addingInputFile(selection)

    def addingInputFile(self, selection):
        inputFileValue = ''
        try:
            inputFile = input('Enter File Name For Input\n')
            with open(inputFile, 'r') as inputFile:
                inputFileValue = inputFile.read()

            result = self.handlingSelection(selection, inputFileValue)
            if result is not 0:
                self.writeToOutputFile(result)
        except FileNotFoundError:
            pass
        except IOError:
            pass

    def handlingSelection(self, selection, inputValue):
        isValid = self.validation(selection, inputValue)

        if selection is self.MORSE_TO_ENGLISH and isValid:
            self.getMorseToEnglish.morseValue = inputValue
            result = self.getMorseToEnglish.getMorseToEnglish()
            if result is 'NotValid':
                print('File contain inappropiate characters')
                return 0

        elif selection is self.ENGLISH_TO_MORSE and isValid:
            self.getEnglishToMorse.englishWord = inputValue.upper()
            result = self.getEnglishToMorse.getEnglishToMorse()

        else:
            print('Input is not valid')
            return 0
        return result

    def writeToOutputFile(self, result):
        try:
            outputFile = input('Enter File Name For Ouput\n')
            with open(outputFile, 'w') as outputFile:
                outputFile.write(result)
        except IOError:
            pass
        except FileNotFoundError:
            pass
        except Exception as e:
            print(e)
            pass

    def validation(self, selection, inputValue):
        isValid = False

        if selection == self.MORSE_TO_ENGLISH:
            morseCodeRegex = '[.\\s-]'
            pattern = re.compile(morseCodeRegex)
            isValid = bool(pattern.match(inputValue))

        elif selection == self.ENGLISH_TO_MORSE:
            inputValue = inputValue.split()[0]
            englishCodeRegex = '^[a-zA-Z0-9]*$'
            pattern = re.compile(englishCodeRegex)
            isValid = bool(pattern.match(inputValue))

        else:
            print("Wrong Input")
        return isValid


converterApp = ConverterApp()
converterApp.main()
