package de.itkl.ovation.messengers.smoope.resources.clientmessage;

import com.codahale.metrics.annotation.Timed;
import de.itkl.ovation.messengers.smoope.model.ChatBots;
import de.itkl.ovation.messengers.smoope.resources.chatbot.ChatBot;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.ws.rs.*;
import javax.ws.rs.client.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.util.Set;

@Path("/clientmessage")
public class ClientMessageReceiver {
    private final ChatBots mChatBots;
    private Logger logger = LoggerFactory.getLogger("/clientmessage");
    private Client client = ClientBuilder.newClient();

    public ClientMessageReceiver(ChatBots chatBots) {
        this.mChatBots = chatBots;
    }

    @POST
    @Timed
    @Produces(MediaType.APPLICATION_JSON)
    @Consumes(MediaType.APPLICATION_JSON)
    public Response receiveMessage(ClientMessage message) {
        logger.info("received the message with content '" + message.getMessage() + "' which will be sent to all registered chatbots.");
        Set<ChatBot> currentlyregisteredChatbots = this.mChatBots.getAllRegistered();
        for (ChatBot bot :currentlyregisteredChatbots) {
            this.sendMessageToBot(message, bot);
        }
        String responseMessage = "Successfully sent message with content '" + message.getMessage() + "' from client '" + message.getClientId() + "' to all " + currentlyregisteredChatbots.size() + " chatbots.";
        logger.info(responseMessage);
        return Response.status(200).entity(responseMessage).build();
    }

    private void sendMessageToBot(ClientMessage message, ChatBot bot) {
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