package de.itkl.ovation.messengers.smoope.resources.message;

import com.fasterxml.jackson.annotation.JsonProperty;

public class Message {

    private String message;
    private String clientId;

    public Message() {
        // Jackson deserialization
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