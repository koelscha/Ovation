import unittest

from chatbot import ChatBot


class ChatbotTest(unittest.TestCase):
    def setUp(self):
        self.chatbot = ChatBot()

    def test_answer_with_name(self):
        self.chatbot.processMessage("I want to move!", "1")
        self.assertEqual(self.chatbot.processMessage("Max Mustermann", "1"), "Your name is {}.")

    def test_greeting_with_contract(self):
        self.assertEqual(self.chatbot.processMessage("Hello Ovation", "1"), "How can help you?")
        self.chatbot.processMessage("I want to move!", "1")
        self.assertEqual(self.chatbot.processMessage("Max Mustermann", "1"), "Your name is {}.")

if __name__ == '__main__':
    unittest.main()
