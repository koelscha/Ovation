package de.itkl.ovation.messengers.smoope.resources.message;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.smoope.sdk.objects.Conversation;
import com.smoope.sdk.objects.Message;
import de.itkl.ovation.messengers.smoope.resources.clientmessage.ClientMessage;

public class ChatBotMessage {

    private String message;
    private String clientId;

    public ChatBotMessage() {
        // Jackson deserialization
    }

    public ChatBotMessage(ClientMessage message) {
        this.message = message.getMessage();
        this.clientId = message.getClientId();
    }

    public ChatBotMessage(Message message, Conversation conversation) {
        this.message = message.getParts().toString();
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
    public String getClientId() {
        return clientId;
    }

    @JsonProperty
    public void setClientId(String clientId) {
        this.clientId = clientId;
    }
}