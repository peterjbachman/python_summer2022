import unittest
from lab03 import * # needs to be same wd as lab03.py


class labTests(unittest.TestCase):
    # fill in a few tests for each
    # make sure to account for correct and incorrect input
    def test_shout(self):
        self.assertEqual(lab03.shout("foo"), "FOO")
        self.assertEqual(lab03.shout("hi there"), "HI THERE")
        self.assertNotEqual(lab03.shout("bar"), "bar")
        with self.assertRaises(AttributeError):
            lab03.shout(1)
            lab03.shout(1.2)

    def test_reverse(self):
        self.assertEqual(lab03.reverse("test"), "tset")
        self.assertEqual(lab03.reverse("hi there"), "ereht ih")
        self.assertNotEqual(lab03.reverse("bar"), "bar")
        with self.assertRaises(TypeError):
            lab03.reverse(1)
            lab03.reverse(1.2)

    def test_reversewords(self):
        self.assertEqual(lab03.reversewords("test"), "test")
        self.assertEqual(lab03.reversewords("hi there"), "there hi")
        with self.assertRaises(AttributeError):
            lab03.reversewords(1)
            lab03.reversewords(1.2)

    def test_reversewordletters(self):
        self.assertEqual(lab03.reversewordletters("test"), "tset")
        self.assertEqual(lab03.reversewordletters("hi there"), "ih ereht")
        self.assertNotEqual(lab03.reversewordletters("bar"), "bar")
        with self.assertRaises(TypeError):
            lab03.reversewordletters(1)
            lab03.reversewordletters(1.2)

    def test_piglatin(self):
        self.assertEqual(lab03.piglatin("test"), "esttay")
        self.assertEqual(lab03.piglatin("hi there"), "ihay heretay")
        self.assertNotEqual(lab03.piglatin("bar"), "bar")
        with self.assertRaises(AttributeError):
            lab03.piglatin(1)
            lab03.piglatin(1.2)


if __name__ == '__main__':
    unittest.main(__name__, argv=['main'], exit=False)
