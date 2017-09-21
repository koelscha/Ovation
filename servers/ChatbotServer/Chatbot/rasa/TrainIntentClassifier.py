from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.converters import load_data
from rasa_nlu.model import Trainer

training_data = load_data("data/intents_training.json")
trainer = Trainer(RasaNLUConfig("config_spacy.json"))
trainer.train(training_data)
trainer.persist("models/")
