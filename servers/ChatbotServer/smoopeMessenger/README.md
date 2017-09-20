# How to prepare:

Enter your smoope credentials (app_id, secret) into the main class src/main/java/.../SmoopeMessengerApplication.java

# How to run (for debugging):

./gradlew clean run

# How to deploy (for debugging):

./gradlew clean shadowJar
java -jar build/libs/smoopeMessenger-all.jar server

# Endpoints

## /chatbot
### POST
* Allows to register a chatbot, which is called whenever a message from a client is received
* The chatbot must be a request with a json containing the property "url"

```bash
curl -X POST localhost:8080/chatbot --data "{\"url\": \"localhost:5000\"}" -H "Content-Type: application/json"
```

### GET
* Returns all registered chatbots as json

```bash
curl -X GET localhost:8080/chatbot
```

## /message

### POST
* Sends a message to a client. The message must be in a json body, containing the properties "message" and "clientId"

```bash
curl -X POST localhost:8080/message --data "{\"message\": \"foobar\", \"clientId\": \"123\"}" -H "Content-Type: application/json"
```

## /clientmessage
* Must be called if a client writes a new message.
* It informs all registered chatbots about the new message

```bash
curl -X POST localhost:8080/clientmessage --data "{\"message\": \"foobar\", \"clientId\": \"123\"}" -H "Content-Type: application/json"
```
