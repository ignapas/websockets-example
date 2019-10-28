<template>
  <div class="chat">
    <h1>Chat</h1>
    <MessageList v-bind:messages="messages" class="message-list" />
    <MessageCompose class="message-compose" />
  </div>
</template>

<script>
import MessageList from "@/components/MessageList.vue";
import MessageCompose from "@/components/MessageCompose.vue";

export default {
  name: "chat",
  components: {
    MessageList,
    MessageCompose
  },
  data() {
    return {
      messages: []
    }
  },
  mounted() {
    this.socket.emit("chatCreated", null, response => {
      if (response && response.data) {
        this.messages = response.data;
      }
    });
    this.socket.on("newMessage", payload => this.addMessage(payload.data))
  },
  methods: {
    addMessage(message) {
      this.messages.push(message)
    }
  }
};
</script>
<style scoped>
.chat {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100vh;
}
.message-list {
  flex: 1;
  overflow: auto;
}
</style>