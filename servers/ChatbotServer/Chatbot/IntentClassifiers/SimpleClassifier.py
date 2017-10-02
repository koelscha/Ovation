from IntentClassifiers import IntentClassifier


class SimpleClassifier(IntentClassifier):
    def classify(self, message):
        if "HALLO" in message.upper():
            return "greeting"
        else:
            return "contract"
