<template>
  <el-form :inline="true" :model="composeForm" @submit.prevent.native="onComposeFormSubmit">
    <el-form-item>
      <el-input ref="message" v-model="composeForm.message" placeholder="Message"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" native-type="submit">Send</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  data() {
    return {
      composeForm: {
        message: ""
      }
    };
  },
  methods: {
    onComposeFormSubmit() {
      if (this.composeForm.message.length) {
        this.socket.emit("message", this.composeForm.message, response => {
          if (response && response.data) {
            console.log("Message sent", response.data);
            this.composeForm.message = ''
            this.$refs.message.$el.focus()
          }
        });
      }
    }
  }
};
</script>
<style scoped>
.el-form-item {
  margin-bottom: 10px;
  margin-top: 10px;
}
</style>