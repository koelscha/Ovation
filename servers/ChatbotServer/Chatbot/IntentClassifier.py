def classify(message):
    if "HELLO" in message.upper():
        return "greeting"
    else:
        return "contract"