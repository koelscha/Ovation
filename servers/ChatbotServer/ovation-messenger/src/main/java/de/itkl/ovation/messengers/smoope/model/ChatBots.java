package de.itkl.ovation.messengers.smoope.model;

import de.itkl.ovation.messengers.smoope.resources.chatbot.ChatBot;
import de.itkl.ovation.messengers.smoope.resources.message.ChatBotMessage;
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

    public void sendMessageToAllBots(ChatBotMessage chatBotMessage) {
        for (ChatBot bot :getAllRegistered()) {
            this.sendMessageToBot(chatBotMessage, bot);
        }
    }

    private void sendMessageToBot(ChatBotMessage chatBotMessage, ChatBot bot) {
        WebTarget target = client.target(bot.getUrl());
        Invocation.Builder invocationBuilder = target.request(MediaType.APPLICATION_JSON);
        Response response = invocationBuilder.post(Entity.entity(chatBotMessage, MediaType.APPLICATION_JSON));
        if (response.getStatus() == 200) {
            logger.info("Successfully sent the message with content '" + chatBotMessage.getMessage()+ "' from client '" + chatBotMessage.getClientId() + "' to the bot with url '" + bot.getUrl() + "'.");
        } else {
            logger.warn("Could not send the message with content '" + chatBotMessage.getMessage()+ "' from client '" + chatBotMessage.getClientId() + "' to the bot with url '" + bot.getUrl() + "'. Reason: " + response.getStatusInfo());
        }
    }
}
