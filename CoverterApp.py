from converter import EnglishtoMorse
from converter import MorseToEnglish


class ConverterApp:
    def __init__(self):
        self.getEnglishToMorse = EnglishtoMorse.EnglishConverter()
        self.getMorseToEnglish = MorseToEnglish.MorseConverter()

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
        if selection is 1:
            self.getMorseToEnglish.morseValue = inputValue
            result = self.getMorseToEnglish.getMorseToEnglish()
        elif selection is 2:
            self.getEnglishToMorse.englishWord = inputValue
            result = self.getEnglishToMorse.getEnglishToMorse()
        else:
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


converterApp = ConverterApp()
converterApp.main()
