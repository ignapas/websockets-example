import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// ElementUI
import ElementUI from 'element-ui'
import './theme/index.css'

import io from 'socket.io-client'

Vue.config.productionTip = false

Vue.use(ElementUI)

const socket = io()
Vue.mixin({
  data() {
    return {
      socket
    }
  }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
