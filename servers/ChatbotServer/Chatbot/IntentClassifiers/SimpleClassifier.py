from IntentClassifiers import IntentClassifier


class SimpleClassifier(IntentClassifier):
    def classify(self, message):
        if "HELLO" in message.upper():
            return "greeting"
        else:
            return "contract"
