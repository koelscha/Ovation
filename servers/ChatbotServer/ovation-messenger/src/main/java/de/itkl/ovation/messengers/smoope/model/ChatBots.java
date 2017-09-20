package de.itkl.ovation.messengers.smoope.model;

import de.itkl.ovation.messengers.smoope.resources.chatbot.ChatBot;
import de.itkl.ovation.messengers.smoope.resources.clientmessage.ClientMessage;
import de.itkl.ovation.messengers.smoope.resources.message.Message;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.ws.rs.client.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.util.HashSet;
import java.util.Set;

public class ChatBots {

    private Set<ChatBot> mCurrentChatbots = new HashSet<ChatBot>();
    private Logger logger = LoggerFactory.getLogger("chatbots-model");
    private Client client = ClientBuilder.newClient();

    public Set<ChatBot> getAllRegistered() {
        return mCurrentChatbots;
    }

    public void register(ChatBot bot) {
        this.mCurrentChatbots.add(bot);
    }

    public void sendMessageToAllBots(Message message) {
        for (ChatBot bot :getAllRegistered()) {
            this.sendMessageToBot(message, bot);
        }
    }

    private void sendMessageToBot(Message message, ChatBot bot) {
        WebTarget target = client.target(bot.getUrl());
        Invocation.Builder invocationBuilder = target.request(MediaType.APPLICATION_JSON);
        Response response = invocationBuilder.post(Entity.entity(message, MediaType.APPLICATION_JSON));
        if (response.getStatus() == 200) {
            logger.info("Successfully sent the message with content '" + message.getMessage()+ "' from client '" +message.getClientId() + "' to the bot with url '" + bot.getUrl() + "'.");
        } else {
            logger.warn("Could not send the message with content '" + message.getMessage()+ "' from client '" +message.getClientId() + "' to the bot with url '" + bot.getUrl() + "'. Reason: " + response.getStatusInfo());
        }
    }
}
