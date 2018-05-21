from converter import EnglishtoMorse
from converter import MorseToEnglish
import re


class ConverterApp:
    def __init__(self):
        self.EnglishToMorseConverter = EnglishtoMorse.Converter()
        self.MorseToEnglishConverter = MorseToEnglish.Converter()
        self.MORSE_TO_ENGLISH = 1  # define constants
        self.ENGLISH_TO_MORSE = 2  # define constants

    # main of program
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

    # function taking input file as input
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
            print("Input File Not Found")
            pass
        except IOError:
            pass

    # when user click on 1 or 2 for selection
    def handlingSelection(self, selection, inputValue):
        isValid = self.validation(selection, inputValue)

        if selection is self.MORSE_TO_ENGLISH and isValid:
            self.MorseToEnglishConverter.morseValue = inputValue
            result = self.MorseToEnglishConverter.getMorseToEnglish()
            if result is 'NotValid':
                print('File contain inappropiate characters')
                return 0

        elif selection is self.ENGLISH_TO_MORSE and isValid:
            self.EnglishToMorseConverter.englishWord = inputValue.upper()
            result = self.EnglishToMorseConverter.getEnglishToMorse()

        else:
            print('Input is not valid')
            return 0
        return result

    # write to output file
    def writeToOutputFile(self, result):
        try:
            outputFile = input('Enter File Name For Output\n')
            with open(outputFile, 'w') as outputFile:
                outputFile.write(result)
        except IOError:
            pass
        except FileNotFoundError:
            print("Output File Not Found")
            pass
        except Exception as e:
            print(e)
            pass

    # validates the input if user give wrong value file for conversion
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
