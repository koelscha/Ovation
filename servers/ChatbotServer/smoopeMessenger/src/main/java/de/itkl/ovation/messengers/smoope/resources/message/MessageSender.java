package de.itkl.ovation.messengers.smoope.resources.message;

import com.codahale.metrics.annotation.Timed;
import com.smoope.sdk.SmoopeApi;
import com.smoope.sdk.objects.*;
import com.smoope.sdk.objects.collections.UserPagedList;
import de.itkl.ovation.messengers.smoope.SmoopeMessageImporter;
import de.itkl.ovation.messengers.smoope.model.ChatBotMessage;
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
        UserPagedList operatorWithMaximumOneItem = mSmoope.getOperatorsList(1, 1);
        if (operatorWithMaximumOneItem.getEmbedded().containsKey("users") && operatorWithMaximumOneItem.getContent().size()>0) {
            User firstOperator = operatorWithMaximumOneItem.getContent().get(0);
            Message message = mSmoope.actAsUser(firstOperator).createMessage(chatbotAnswer, conversation);
            mMessageImporter.updateLatestMessageFor(message, conversation);
        } else {
            logger.warn("No operators found for current business. Could not sent message out to client!");
        }

    }
}