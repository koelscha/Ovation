package de.itkl.ovation.messengers.smoope.resources.message;

import com.codahale.metrics.annotation.Timed;
import com.smoope.sdk.SmoopeApi;
import com.smoope.sdk.SmoopeApiFactory;
import com.smoope.sdk.objects.*;
import com.smoope.sdk.objects.collections.UserPagedList;
import de.itkl.ovation.messengers.smoope.SmoopeMessageImporter;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

@Path("/message")
public class MessageSender {
    private final SmoopeApi mSmoope;
    private final SmoopeMessageImporter mMessageImporter;
    private Logger logger = LoggerFactory.getLogger("/message");

    public MessageSender(SmoopeApi smoope, SmoopeMessageImporter importer) {
        this.mSmoope = smoope;
        this.mMessageImporter = importer;
    }

    @POST
    @Timed
    @Produces(MediaType.APPLICATION_JSON)
    @Consumes(MediaType.APPLICATION_JSON)
    public Response sendMessage(ChatBotMessage chatBotMessage) {
        logger.info("received the message with content '" + chatBotMessage.getMessage() + "' to be sent to the client '" + chatBotMessage.getClientId() +"'.");
        this.sendMessageToSmoope(chatBotMessage);
        return Response.status(200).entity("Successfully sent message with content '" + chatBotMessage.getMessage() + "' to the client '" + chatBotMessage.getClientId() +"'.").build();
    }

    private void sendMessageToSmoope(ChatBotMessage chatBotMessage) {
        Message chatbotAnswer = Message.text(chatBotMessage.getMessage());
        Conversation conversation = mSmoope.getConversation(chatBotMessage.getClientId());
        Message message = mSmoope.actAsUser("5436416d-ed23-4907-82c5-232e4e97ee7a").createMessage(chatbotAnswer, conversation);
        mMessageImporter.updateLatestMessageFor(message, conversation);
    }
}