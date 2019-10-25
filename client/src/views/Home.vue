<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/osparc-black.png">
    <Connect />
  </div>
</template>

<script>
// @ is an alias to /src
import Connect from '@/components/Connect.vue'

export default {
  name: 'home',
  components: {
    Connect
  }
}
</script>
