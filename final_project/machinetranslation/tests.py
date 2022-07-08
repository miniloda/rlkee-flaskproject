from . import translator
import unittest


class test_translator(unittest.TestCase):
    def test_english_to_french_basic(self):
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")
    def test_english_to_french_null(self):
        self.assertEqual(translator.english_to_french(None), "")
    def test_french_to_english_basic(self):
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")
    def test_french_to_english_null(self):
        self.assertEqual(translator.french_to_english(None), "")

if __name__ == "__main__":
    unittest.main()