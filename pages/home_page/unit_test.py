import unittest


class TestSetup(unittest.TestCase):
    def setUp(self):
        print('Print function A')
    def test_methodA(self):
        print('Print function B')

    def test_methodB(self):
        print('Print Sample function1')

    def tearDown(self):
        print('Print Sample function2')

if __name__ == '__main__':
    unittest.main(verbosity=2)


def capitalize_first_last_letters(str1):
    str1 = result = str1.title()
    result = ""
    for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
    return result[:-1]


print(capitalize_first_last_letters("python exercises practice solution"))
print(capitalize_first_last_letters("w3resource"))


string = "how are you"
string = a = string.title()
print(a)
