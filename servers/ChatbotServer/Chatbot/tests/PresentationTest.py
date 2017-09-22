import unittest

from chatbot import ChatBot


class PresentationTest(unittest.TestCase):
    def setUp(self):
        fileName = "../../json-schemas/examples/presentation.json"
        self.chatbot = ChatBot(fileName)

    def test_answer_with_name(self):
        self.assertEqual(self.chatbot.processMessage("Hello", "1"), "Hello, what can I do for you?")
        self.assertTrue(
            self.chatbot.processMessage("I am going to move soon, and I am having trouble about the price change",
                                        "1").find("When you move we need your new address") >= 0)
        self.assertEqual(self.chatbot.processMessage("01.10.2017", "1"), "What is the new street name and number?")
        self.assertEqual(self.chatbot.processMessage("Saarbrückerstraße 36", "1"), "What is the new zip code?")
        self.assertEqual(self.chatbot.processMessage("10787", "1"), "How large is the new home in square meters?")
        self.assertEqual(self.chatbot.processMessage("104", "1"), "When will you move into your new home?")
        result = self.chatbot.processMessage("1st of October", "1")
        self.assertTrue(result.find("Saarbrückerstraße 36")>=0)
        self.assertTrue(result.find("10787")>=0)
        self.assertTrue(result.find("Berlin")>=0)
        self.assertTrue(result.find("1st of October")>=0)
        self.assertTrue(result.find("104") >= 0)

    def testLostInsuranceCard(self):
        self.assertEqual(self.chatbot.processMessage("Hello", "1"), "Hello, what can I do for you?")
        self.assertTrue(self.chatbot.processMessage("I have lost my insurance card. What should I do?", "1").find(
            "No problem") >= 0)
        self.assertEqual(self.chatbot.processMessage("Oh, great", "1"), "What is your insurance number?")
        self.assertEqual(self.chatbot.processMessage("1234", "1"), "What is your birthdate?")
        self.assertTrue(self.chatbot.processMessage("01.02.2001", "1").find("1234") >= 0)

    def test_entity_recognizer(self):
        fileName = "../../json-schemas/examples/entity_recognizer_test.json"
        self.chatbot = ChatBot(fileName)
        self.assertEqual(self.chatbot.processMessage("Hello", "1"), "Hello, what can I do for you?")
        self.assertTrue(self.chatbot.processMessage("Contract", "1").find("When you move we need your new address") >= 0)
        self.assertEqual(self.chatbot.processMessage(
            "My new flat is located in Saarbrücker Straße 36, 10787 Berlin and has 64 square meters.", "1"),
                         "When will you move into your new home?")

if __name__ == '__main__':
    unittest.main()
