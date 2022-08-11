# Write a function that counts how many vowels are in a word
# Raise a TypeError with an informative message if 'word' is passed as
#   an integer
# When done, run the test in your script and see your results.
import unittest


def count_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    try:
        for i in word.lower():
            if i in vowels:
                count += 1
        return count
    except TypeError:
        if type(word) == int:
            raise TypeError("Integers do not have vowels")
        else:
            raise TypeError("Enter a string")


class TestVowels(unittest.TestCase):
    def test_counting(self):
        self.assertEqual(count_vowels("python"), 1)
        self.assertEqual(count_vowels("unconvincing"), 4)
        self.assertEqual(count_vowels("sky"), 0)

    def test_error(self):
        with self.assertRaises(TypeError):
            count_vowels(1)
        with self.assertRaises(TypeError):
            count_vowels(1.1)


if __name__ == '__main__':
    # ipython throws an error otherwise
    unittest.main(__name__, argv=['main'], exit=False)
