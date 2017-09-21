# Install the bleeding edge version of TFLearn and rasa
pip install git+https://github.com/tflearn/tflearn.git

git clone https://github.com/RasaHQ/rasa_nlu.git /tmp/rasa_nlu
cd !$
pip install -r requirements.txt
python setup.py install

# Download the data and Models of NLTK and Spacy
python -m nltk.downloader all
python -m spacy download en_core_web_md
python -m spacy download de_core_news_md

