package de.itkl.ovation.messengers.smoope;

import com.smoope.sdk.SmoopeApi;
import com.smoope.sdk.impl.SmoopeClient;
import com.smoope.sdk.objects.Business;
import com.smoope.sdk.objects.Conversation;
import com.smoope.sdk.objects.Message;
import com.smoope.sdk.objects.collections.ConversationPagedList;
import com.smoope.sdk.objects.collections.MessagesPagedList;
import com.smoope.sdk.objects.common.filter.ConversationsFilter;
import com.smoope.sdk.objects.common.filter.MessagesFilter;
import de.itkl.ovation.messengers.smoope.model.ChatBots;
import de.itkl.ovation.messengers.smoope.model.ChatBotMessage;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SmoopeMessageImporter {
    private final SmoopeApi mSmoope;
    private final ChatBots mChatBots;

    private Map<String, String> lastMessages = new HashMap<>();
    private Logger logger = LoggerFactory.getLogger("SmoopeMessageImporter");

    public SmoopeMessageImporter(SmoopeApi smoope, ChatBots chatBots) {
        this.mSmoope = smoope;
        this.mChatBots = chatBots;
    }

    public void importConversations() {
        logger.info("Starting message import from smoope...");
        Business business = mSmoope.getBusiness();
        logger.debug("Got business from smoope. Starting message import for business '" + business.getName() + "'");
        ConversationPagedList conversations = this.mSmoope.getConversationsList(business,  1, 100);
        Map<String, List<Conversation>> embedded = conversations.getEmbedded();
        if (!embedded.containsKey("conversations")) {
            logger.info("No unread conversations available");
            return;
        }
        logger.debug("Got all "+conversations.getContent().size()+" conversations for the current business. Importing messages...");
        List<Conversation> listedConversation = conversations.getContent();
        for(Conversation conversation:listedConversation) {
            logger.debug("Importing messages for conversation " + conversation.getId());
            this.getMessages(conversation);
        }
        logger.info("Finished message import from smoope.");
    }

    private void getMessages(Conversation conversation) {
        MessagesPagedList messages;
        if (lastMessages.containsKey(conversation.getId())) {
            messages = mSmoope.getMessagesList(conversation, MessagesFilter.after(lastMessages.get(conversation.getId())), 1, 100);
        } else {
            messages = mSmoope.getMessagesList(conversation,1, 100);
        }

        Map<String, List<Message>> embedded = messages.getEmbedded();
        if (!embedded.containsKey("messages")) {
            logger.debug("Message content is not available, skipping message import for conversation " + conversation.getId());
            return;
        }
        List<Message> listedMessages = messages.getContent();
        Collections.reverse(listedMessages);
        for(Message message:listedMessages) {
            this.triggerMessageReceived(message, conversation);
        }
    }

    private void triggerMessageReceived(Message message, Conversation conversation) {
        this.lastMessages.put(conversation.getId(), message.getId());
        logger.info("Received new message with id " + message.getId() + " for conversation " + conversation.getId() + ". Forward message to all chatbots.");
        mChatBots.sendMessageToAllBots(new ChatBotMessage(message, conversation));

    }

    public void updateLatestMessageFor(Message message, Conversation conversation) {
        this.lastMessages.put(conversation.getId(), message.getId());
    }
}
