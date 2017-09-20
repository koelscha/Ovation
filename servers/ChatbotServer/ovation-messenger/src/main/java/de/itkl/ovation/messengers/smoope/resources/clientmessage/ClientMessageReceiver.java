package de.itkl.ovation.messengers.smoope.resources.clientmessage;

import com.codahale.metrics.annotation.Timed;
import de.itkl.ovation.messengers.smoope.model.ChatBots;
import de.itkl.ovation.messengers.smoope.resources.chatbot.ChatBot;
import de.itkl.ovation.messengers.smoope.resources.message.Message;
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

    public ClientMessageReceiver(ChatBots chatBots) {
        this.mChatBots = chatBots;
    }

    @POST
    @Timed
    @Produces(MediaType.APPLICATION_JSON)
    @Consumes(MediaType.APPLICATION_JSON)
    public Response receiveMessage(ClientMessage message) {
        logger.info("received the message with content '" + message.getMessage() + "' which will be sent to all registered chatbots.");
        mChatBots.sendMessageToAllBots(new Message(message));
        String responseMessage = "Successfully sent message with content '" + message.getMessage() + "' from client '" + message.getClientId() + "' to all " + mChatBots.getAllRegistered().size() + " chatbots.";
        logger.info(responseMessage);
        return Response.status(200).entity(responseMessage).build();
    }


}