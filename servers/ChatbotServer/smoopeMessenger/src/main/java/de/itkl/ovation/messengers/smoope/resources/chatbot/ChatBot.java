package de.itkl.ovation.messengers.smoope.resources.chatbot;

import com.fasterxml.jackson.annotation.JsonProperty;

public class ChatBot {

    private String url;

    public ChatBot() {
        // Jackson deserialization
    }


    @JsonProperty
    public String getUrl() {
        return url;
    }

    @JsonProperty
    public void setUrl(String url) {
        this.url = url;
    }
}