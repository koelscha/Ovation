# How to prepare:

Enter your smoope credentials (app_id, secret) into the main class src/main/java/.../SmoopeMessengerApplication.java

# How to run (for debugging):

./gradlew clean run

# Endpoints

## /chatbot
### POST
* Allows to register a chatbot, which is called whenever a message from a client is received
* The chatbot must be a request with a json containing the property "url"

### GET
* Returns all registered chatbots as json

## /message

### POST
* Sends a message to a client. The message must be in a json body, containing the properties "message" and "clientId"

## /clientmessage
* Must be called if a client writes a new message.
* It informs all registered chatbots about the new message
