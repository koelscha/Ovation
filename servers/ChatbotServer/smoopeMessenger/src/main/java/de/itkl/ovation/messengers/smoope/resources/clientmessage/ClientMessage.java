package de.itkl.ovation.messengers.smoope.resources.clientmessage;

import com.fasterxml.jackson.annotation.JsonProperty;

public class ClientMessage {

    private String message;
    private String clientId;

    public ClientMessage() {
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