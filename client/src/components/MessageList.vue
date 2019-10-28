<template>
  <div class="chatroom">
    <el-row v-for="message in messages" v-bind:key="message.id">
      <el-col :md="{ span: 8, offset: 8 }">
        <Message v-bind:message="message" />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Message from "@/components/Message"
export default {
  name: 'ChatRoom',
  components: {
    Message
  },
  props: {
    messages: String
  },
  methods: {
    scrollToBottom() {
      const msgList = this.$el
      msgList.scrollTop = msgList.scrollHeight
    }
  },
  updated() {
    this.scrollToBottom();
  }
}
</script>
