package de.itkl.ovation.messengers.smoope;

import com.smoope.sdk.SmoopeApi;
import com.smoope.sdk.objects.Conversation;
import com.smoope.sdk.objects.Message;
import com.smoope.sdk.objects.collections.ConversationPagedList;
import com.smoope.sdk.objects.collections.MessagesPagedList;
import com.smoope.sdk.objects.common.filter.MessagesFilter;

import java.util.HashMap;
import java.util.Map;
import java.util.function.Consumer;

public class MessageImporter {
    private final SmoopeApi mSmoope;
    private Map<String, String> lastMessages = new HashMap<>();

    public MessageImporter(SmoopeApi smoope) {
        this.mSmoope = smoope;
    }

    public void importConversations() {
        ConversationPagedList conversations = this.mSmoope.getConversationsList(1, 10);
        conversations.forEach(getConversationConsumer());
    }

    private Consumer<Conversation> getConversationConsumer() {
        return conversation -> this.getMessages(conversation);
    }

    private void getMessages(Conversation conversation) {
        MessagesPagedList messages;
        if (lastMessages.containsKey(conversation.getId())) {
            messages = mSmoope.getMessagesList(conversation, MessagesFilter.after(lastMessages.get(conversation.getId())), 1, 10);
        } else {
            messages = mSmoope.getMessagesList(conversation,1, 10);
        }

        messages.forEach(message -> this.triggerMessageReceived(message, conversation));

    }

    private void triggerMessageReceived(Message message, Conversation conversation) {
        this.lastMessages.put(conversation.getId(), message.getId());

    }
}
