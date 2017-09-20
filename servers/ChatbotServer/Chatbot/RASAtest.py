from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
import spacy
from rasa_nlu.model import Metadata, Interpreter



"""
RASA Traning
"""
training_data = load_data('./demo-rasa.json')
trainer = Trainer(RasaNLUConfig("./config_spacy.json"))
trainer.train(training_data)
model_directory = trainer.persist('./models/')

"""
Example sentence
"""
text = u"I want to know about the insurance info in Kaiserslautern"

# where `model_directory points to the folder the model is persisted in
interpreter = Interpreter.load(model_directory, RasaNLUConfig("rasa/config_spacy.json"))
print interpreter.parse(text)

"""
Entity Extraction
"""
nlp = spacy.load('en')
doc = nlp(text)
for ent in doc.ents:
    print(ent.label_, ent.text)
    # GPE: Location tag
