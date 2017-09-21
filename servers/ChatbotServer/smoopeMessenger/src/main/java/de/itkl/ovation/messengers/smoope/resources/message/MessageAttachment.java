package de.itkl.ovation.messengers.smoope.resources.message;

import com.fasterxml.jackson.annotation.JsonProperty;

public class MessageAttachment {
    private String fileName;
    private String url;
    private String mimeType;

    public MessageAttachment(String url, String mimeType, String name) {
        this.url = url;
        this.mimeType = mimeType;
        this.fileName=name;
    }

    @JsonProperty
    public String getMimeType() {
        return mimeType;
    }

    @JsonProperty
    public void setMimeType(String mimeType) {
        this.mimeType = mimeType;
    }

    @JsonProperty
    public String getUrl() {
        return url;
    }

    @JsonProperty
    public void setUrl(String url) {
        this.url = url;
    }

    @JsonProperty
    public String getFileName() {
        return fileName;
    }

    @JsonProperty
    public void setFileName(String name) {
        this.fileName = name;
    }
}
