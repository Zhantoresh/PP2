"""
Define a class which has at least two methods: getString: 
to get a string from console input printString: to print the string in upper case.
"""
class StringInputAndOutput:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Введите строку: ")

    def printString(self):
        print("Строка в верхнем регистре:", self.input_string.upper())


string = StringInputAndOutput()
string.getString()
string.printString()