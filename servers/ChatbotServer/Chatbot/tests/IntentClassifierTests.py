import unittest

from IntentClassifiers.RasaClassifier import RasaClassifier


class IntentClassifierTests(unittest.TestCase):
    def setUp(self):
        self.rasa_classifier = RasaClassifier()

    def test_greeting_recognition(self):
        test_messages = {"greeting": ["Hi there.",
                                      "Hey yo whats up?",
                                      "Hello my name is Max Mustermann."],
                         "contract": ["I want to move.",
                                      "Can you change my address?",
                                      "I want to change my address."],
                         "lost": ["I lost my card.",
                                  "Please lock my health insurance card.",
                                  "My card was lost. Please lock it."]
                         }

        for intent, messages in test_messages.items():
            for message in messages:
                self.assertEqual(self.rasa_classifier.classify(message), intent,
                                 "The intent of \"{}\" was not correct!".format(message))


if __name__ == '__main__':
    unittest.main()
