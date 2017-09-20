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

import java.util.Timer;
import java.util.TimerTask;

public class SmoopeMessengerApplication extends Application<SmoopeMessengerConfiguration> {
    private String appSecret = "SECRET";
    private String appId = "APP_ID";

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
        ChatBots chatBots = new ChatBots();

        SmoopeApi smoope =new SmoopeClient.Builder(appId, appSecret).sandbox(true).build();

        SmoopeMessageImporter importer = new SmoopeMessageImporter(smoope, chatBots);
        Timer timer = new Timer();
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                importer.importConversations();
            }
        }, 0, 5000);



        final ChatBotRegistration resource = new ChatBotRegistration(chatBots);
        environment.jersey().register(resource);

        final MessageSender messageSender = new MessageSender(smoope, importer);
        environment.jersey().register(messageSender);

        final ClientMessageReceiver clientMessageReceiver = new ClientMessageReceiver(chatBots);
        environment.jersey().register(clientMessageReceiver);
    }

}