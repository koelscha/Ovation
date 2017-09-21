package de.itkl.ovation.messengers.smoope.model;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.smoope.sdk.objects.Conversation;
import com.smoope.sdk.objects.Message;
import de.itkl.ovation.messengers.smoope.resources.clientmessage.ClientMessage;

import java.util.LinkedList;
import java.util.List;

public class ChatBotMessage {

    private String message;
    private String clientId;
    private List<MessageAttachment> attachments = new LinkedList<>();

    public ChatBotMessage() {
        // Jackson deserialization
    }

    public ChatBotMessage(ClientMessage message) {
        this.message = message.getMessage();
        this.clientId = message.getClientId();
    }

    public ChatBotMessage(Message message, Conversation conversation) {
        this.message = "";

        for (Message.Part part :message.getParts()) {
            if (part.getLinks().containsKey("source")) {
                String attachmentUrl = part.getLinks().get("source").getHref();
                MessageAttachment attachment = new MessageAttachment(attachmentUrl, part.getMimeType(), part.getFilename());
                this.attachments.add(attachment);
            }

            if (part.isText()) {
                this.message += part.getBody();
            }
        }
        this.clientId = conversation.getId();
    }


    @JsonProperty
    public String getMessage() {
        return message;
    }

    @JsonProperty
    public void setMessage(String message) {
        this.message = message;
    }

    @JsonProperty
    public List<MessageAttachment> getAttachments() {
        return attachments;
    }

    @JsonProperty
    public void setAttachments(List<MessageAttachment> attachments) {
        this.attachments = attachments;
    }

    @JsonProperty
    public String getClientId() {
        return clientId;
    }

    @JsonProperty
    public void setClientId(String clientId) {
        this.clientId = clientId;
    }
}