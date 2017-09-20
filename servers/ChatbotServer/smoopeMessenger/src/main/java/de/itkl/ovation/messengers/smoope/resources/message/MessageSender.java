package de.itkl.ovation.messengers.smoope.resources.message;

import com.codahale.metrics.annotation.Timed;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

@Path("/message")
public class MessageSender {
    private Logger logger = LoggerFactory.getLogger("/message");

    @POST
    @Timed
    @Produces(MediaType.APPLICATION_JSON)
    @Consumes(MediaType.APPLICATION_JSON)
    public Response sendMessage(ChatBotMessage chatBotMessage) {
        logger.info("received the message with content '" + chatBotMessage.getMessage() + "' to be sent to the client '" + chatBotMessage.getClientId() +"'.");
        return Response.status(200).entity("Successfully sent message with content '" + chatBotMessage.getMessage() + "' to the client '" + chatBotMessage.getClientId() +"'.").build();
    }
}