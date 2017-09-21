from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
import spacy
from rasa_nlu.model import Metadata, Interpreter



"""
RASA Traning
"""
"""
training_data = load_data('rasa/data/demo-rasa.json')
trainer = Trainer(RasaNLUConfig("rasa/config_spacy.json"))
trainer.train(training_data)
model_directory = trainer.persist('./models/')
"""



def classify(message):
    interpreter = Interpreter.load(u'./models/default/model_20170920-202800',
                                   RasaNLUConfig("rasa/config_spacy.json"))
    return interpreter.parse(unicode(message, "utf-8"))[u'intent'][u'name']
