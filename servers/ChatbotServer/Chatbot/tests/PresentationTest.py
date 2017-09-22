import unittest

from chatbot import ChatBot


class PresentationTest(unittest.TestCase):
    def setUp(self):
        fileName = "../../json-schemas/examples/presentation.json"
        self.chatbot = ChatBot(fileName)

    def test_bike(self):
        fileName = "../../json-schemas/examples/presentation.json"
        self.chatbot = ChatBot(fileName)
        self.assertEqual(self.chatbot.processMessage("bike", "1"),
                         "I will check that for you. Can you tell me the cost of your bycicle or send a photo of the invoice")
        self.assertEqual(self.chatbot.processMessage("Ok.", "1"), "What was the price of your bicycle?")
        self.assertEqual(self.chatbot.processMessage("500", "1"), "Bikes are included up to a value of 500 €")

if __name__ == '__main__':
    unittest.main()
