package de.itkl.ovation.messengers.smoope;

import com.smoope.sdk.SmoopeApi;
import com.smoope.sdk.impl.SmoopeClient;
import de.itkl.ovation.messengers.smoope.model.ChatBots;
import de.itkl.ovation.messengers.smoope.resources.chatbot.ChatBotRegistration;
import de.itkl.ovation.messengers.smoope.resources.clientmessage.ClientMessageReceiver;
import de.itkl.ovation.messengers.smoope.resources.message.MessageSender;
import io.dropwizard.Application;
import io.dropwizard.setup.Bootstrap;
import io.dropwizard.setup.Environment;

public class SmoopeMessengerApplication extends Application<SmoopeMessengerConfiguration> {
    public static void main(String[] args) throws Exception {
        new SmoopeMessengerApplication().run(args);
    }

    @Override
    public String getName() {
        return "smoope-messenger";
    }

    @Override
    public void initialize(Bootstrap<SmoopeMessengerConfiguration> bootstrap) {
        // nothing to do yet
    }

    @Override
    public void run(SmoopeMessengerConfiguration configuration,
                    Environment environment) {

        SmoopeApi smoope = new SmoopeClient("APP_ID", "SECRET");

        MessageImporter importer = new MessageImporter(smoope);
        importer.importConversations();


        ChatBots chatBots = new ChatBots();
        final ChatBotRegistration resource = new ChatBotRegistration(chatBots);
        environment.jersey().register(resource);

        final MessageSender messageSender = new MessageSender();
        environment.jersey().register(messageSender);

        final ClientMessageReceiver clientMessageReceiver = new ClientMessageReceiver(chatBots);
        environment.jersey().register(clientMessageReceiver);
    }

}