package de.itkl.ovation.messengers.smoope.model;

import de.itkl.ovation.messengers.smoope.resources.chatbot.ChatBot;

import java.util.HashSet;
import java.util.Set;

public class ChatBots {

    private Set<ChatBot> mCurrentChatbots = new HashSet<ChatBot>();

    public Set<ChatBot> getAllRegistered() {
        return mCurrentChatbots;
    }

    public void register(ChatBot bot) {
        this.mCurrentChatbots.add(bot);
    }
}
