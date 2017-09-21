import json
import unittest

from chatbot import ChatBot


class ChatbotTest(unittest.TestCase):
    businessCases = {
        "api": "1.0.0-SNAPSHOT",
        "businessCases": [
            {
                "name": "Test",
                "intent": "contract",
                "confirmationPhrase": "Bye!",
                "entities": [
                    {
                        "name": "name",
                        "question": "Name?",
                        "extractor": "MirrorExtractor"
                    }
                ],
                "businessLogic": "InsuranceCalculator",
                "openingQuestion": "I want to know your name."
            }
        ]
    }

    def createTestJsonFile(self):
        file_name = 'testBusinessCases.json'
        with open(file_name, 'w') as f:
            f.write(json.dumps(self.businessCases, indent=4))
        return file_name

    def setUp(self):
        self.chatbot = ChatBot(self.createTestJsonFile())

    def test_answer_with_name(self):
        self.assertEqual(self.chatbot.processMessage("Contract", "1"), "I want to know your name.")
        self.assertEqual(self.chatbot.processMessage("Dominik", "1"), "Dominik")
        self.assertEqual(self.chatbot.processMessage("whatever", "1"), "Bye!")

if __name__ == '__main__':
    unittest.main()
