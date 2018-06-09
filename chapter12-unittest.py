import unittest


def capitalise(input_string):
    output_string = ""
    for character in input_string:
        if character.islower():
            # if character.isupper():
            output_string = output_string + chr(ord(character) - 32)
            # output_string = output_string + character
        else:
            output_string = output_string + character
            # output_string = output_string + chr(ord(character) - 32)
    return output_string


class Tests(unittest.TestCase):
    def test_1(self):
        # run ok if expectation satisfied, for further information, check case.py
        self.assertEqual("HELLOWORLD", capitalise("helloWorld"))

    def test_2(self):
        self.assertEqual("HELLO WORLD", capitalise("Hello World"))

    def test_3(self):
        self.assertEqual('!"%!@#$%^*&()_+=', capitalise('!"%!@#$%^*&()_+='))

    def test_4(self):
        self.assertEqual("1234567890", capitalise("1234567890"))

    def test_5(self):
        self.assertEqual("HELLO WORLD", capitalise("HELLO WORLD"))


if __name__ == "__main__":
    # when unittest.main() is invoked, Python will run all methods which start with test_ in unittest.TestCase subclass
    # which refers to test_1 method in this example
    # Try to use massive valid input in designing test case
    unittest.main(verbosity=2)
