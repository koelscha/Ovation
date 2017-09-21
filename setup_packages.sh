# Install the bleeding edge version of TFLearn and rasa
pip install git+https://github.com/tflearn/tflearn.git
pip install git+https://github.com/RasaHQ/rasa_nlu.git

# Download the data and Models of NLTK and Spacy
python -m nltk.downloader all
python -m spacy download en_core_web_md
python -m spacy download de_core_news_md

