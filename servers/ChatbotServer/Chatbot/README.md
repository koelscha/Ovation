# How to use
* configure `serverAddress` - address of the Messenger.
* configure `chatBotAddress` - address of the ChatBot.
* run `python3 chatbot.py`


# Endpoints

### /message

##### POST
* send a message to the chatbot for processing.
* Format: JSON

      {"message": string,
       "clientId": string
      }