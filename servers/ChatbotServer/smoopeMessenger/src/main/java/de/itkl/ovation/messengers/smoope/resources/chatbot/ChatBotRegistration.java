package de.itkl.ovation.messengers.smoope.resources.chatbot;

import com.codahale.metrics.annotation.Timed;
import de.itkl.ovation.messengers.smoope.model.ChatBots;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

@Path("/chatbot")
public class ChatBotRegistration {
    private final ChatBots mChatBots;
    private Logger logger = LoggerFactory.getLogger("/chatbot");

    public ChatBotRegistration(ChatBots chatBots) {
        mChatBots = chatBots;
    }

    @GET
    @Timed
    @Produces(MediaType.APPLICATION_JSON)
    public Response listChatBots() {
        return Response.ok(this.mChatBots.getAllRegistered()).build();
    }

    @POST
    @Timed
    @Produces(MediaType.APPLICATION_JSON)
    @Consumes(MediaType.APPLICATION_JSON)
    public Response registerChatbot(ChatBot chatbot) {
        this.mChatBots.register(chatbot);
        logger.info("Sucessfully registered a new chatbot with url '" + chatbot.getUrl() + "'");
        String output = "Chatbot with url '" + chatbot.getUrl() + "' registered succesfully!";
        return Response.status(200).entity(output).build();
    }
}