package de.itkl.ovation.messengers.smoope;

import com.fasterxml.jackson.annotation.JsonProperty;
import io.dropwizard.Configuration;
import org.hibernate.validator.constraints.NotEmpty;

public class SmoopeMessengerConfiguration extends Configuration {

    @NotEmpty
    private String smoopeAppId;

    @NotEmpty
    private String smoopeSecret;


    @JsonProperty
    public String getSmoopeAppId() {
        return smoopeAppId;
    }

    @JsonProperty
    public void setSmoopeAppId(String appId) {
        this.smoopeAppId = appId;
    }

    @JsonProperty
    public String getSmoopeSecret() {
        return smoopeSecret;
    }

    @JsonProperty
    public void setSmoopeSecret(String secret) {
        this.smoopeSecret = secret;
    }

}