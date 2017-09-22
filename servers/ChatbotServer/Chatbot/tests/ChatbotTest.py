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
                "extractor": "MirrorExtractor",
                "entities": [
                    {
                        "name": "name",
                        "question": "Name?"
                    }
                ],
                "businessLogic": "EntityResponder",
                "openingQuestion": "I want to know your name."
            }
        ]
    }
    file_name = 'testBusinessCases.json'

    def createTestJsonFile(self):
        with open(self.file_name, 'w') as f:
            f.write(json.dumps(self.businessCases, indent=4))

    def setUp(self):
        self.createTestJsonFile()
        self.chatbot = ChatBot(self.file_name)

    def tearDown(self):
        import os
        os.remove(self.file_name)

    def test_answer_with_name(self):
        self.assertEqual(self.chatbot.processMessage("Contract", "1"), "I want to know your name.")
        self.assertEqual(self.chatbot.processMessage("Nice", "1"), "Name?")
        self.assertEqual(self.chatbot.processMessage("Dominik", "1"), "Dominik")
        self.assertEqual(self.chatbot.processMessage("whatever", "1"), "Bye!")

if __name__ == '__main__':
    unittest.main()
