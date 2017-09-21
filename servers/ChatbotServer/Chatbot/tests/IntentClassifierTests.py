import unittest

from IntentClassifiers.RasaClassifier import RasaClassifier


class IntentClassifierTests(unittest.TestCase):
    def setUp(self):
        rasa_model = '../rasa/models/model_20170921-221417'
        rasa_config = "../rasa/config_spacy.json"
        self.rasa_classifier = RasaClassifier(rasa_model, rasa_config)

    def test_greeting_recognition(self):
        test_messages = {"greeting": ["Hi there.",
                                      "Hey yo whats up?",
                                      "Hello my name is Max Mustermann."],
                         "contract": ["I want to move.",
                                      "Can you change my address?",
                                      "I want to change my address."]
                         }

        for intent, messages in test_messages.items():
            for message in messages:
                self.assertEqual(self.rasa_classifier.classify(message), intent,
                                 "The intent of \"{}\" was not correct!".format(message))


if __name__ == '__main__':
    unittest.main()
