import os
import unittest

from IntentClassifiers.RasaClassifier import RasaClassifier


class IntentClassifierTests(unittest.TestCase):
    def setUp(self):
        print(os.getcwd())
        rasa_model = '../rasa/models/model_20170921-221417'
        rasa_config = "../rasa/config_spacy.json"
        self.rasa_classifier = RasaClassifier(rasa_model, rasa_config)

    def test_greeting_recognition(self):
        test_messages = ["Hi there.",
                         "Hey yo whats up?",
                         "Hello my name is Max Mustermann."]

        for message in test_messages:
            self.assertEqual(self.rasa_classifier.classify(message), "greeting",
                             "The intent of \"{}\" was not correct!".format(message))

    def test_contract_recognition(self):
        pass


if __name__ == '__main__':
    unittest.main()
