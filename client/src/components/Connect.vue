<template>
  <el-form :inline="true" :model="connectForm" @submit.prevent.native="onConnectFormSubmit">
    <el-form-item label="What is your name?">
      <el-input v-model="connectForm.login" placeholder="Name"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" native-type="submit">Connect</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  data() {
    return {
      connectForm: {
        login: ""
      }
    };
  },
  methods: {
    onConnectFormSubmit() {
      if (this.connectForm.login.length) {
        this.socket.emit("login", this.connectForm.login, response => {
          if (response && response.data) {
            this.$router.push("chat");
          }
        })
      }
    }
  }
};
</script>