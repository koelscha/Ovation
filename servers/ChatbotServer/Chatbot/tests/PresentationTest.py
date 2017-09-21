import json
import unittest

from chatbot import ChatBot

class PresentationTest(unittest.TestCase):
    def setUp(self):
        fileName = "../../json-schemas/examples/presentation.json"
        self.chatbot = ChatBot(fileName)

    def test_answer_with_name(self):
        self.assertEqual(self.chatbot.processMessage("Hello", "1"), "Hello, hat can I do for you?")
        self.assertTrue(self.chatbot.processMessage("Contract", "1").find("When you move we need your new address")>=0)
        self.assertEqual(self.chatbot.processMessage("OK", "1"), "What is the new street name and number?")
        self.assertEqual(self.chatbot.processMessage("Saarbrückerstraße 36", "1"), "What is the new zip code?")
        self.assertEqual(self.chatbot.processMessage("10787", "1"), "In which city will you live?")
        self.assertEqual(self.chatbot.processMessage("Berlin", "1"), "How large is the new home in square meters?")
        self.assertEqual(self.chatbot.processMessage("104", "1"), "When will you move into your new home?")
        result = self.chatbot.processMessage("1st of October", "1")
        self.assertTrue(result.find("Saarbrückerstraße 36")>=0)
        self.assertTrue(result.find("10787")>=0)
        self.assertTrue(result.find("Berlin")>=0)
        self.assertTrue(result.find("1st of October")>=0)
        self.assertTrue(result.find("104") >= 0)

if __name__ == '__main__':
    unittest.main()
