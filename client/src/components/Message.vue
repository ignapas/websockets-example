<template>
  <el-card body-style="padding: 0 10px; text-align: left;">
    <div class="author"><small class="author">{{ message.author }}</small></div>
    <p>{{ message.text }}</p>
  </el-card>
</template>

<script>
export default {
  name: 'message',
  props: {
    message: Object
  }
}
</script>
<style scoped>
.author {
  margin-top: 5px;
}
.el-card {
  margin-top: 5px;
}
</style>