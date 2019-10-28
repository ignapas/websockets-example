import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    chat: {
      messages: []
    }
  },
  mutations: {
    setMessages: (state, messages) => {
      state.chat.messages = messages
    },
    addMessage: (state, message) => {
      state.chat.messages.push(message)
    }
  },
  actions: {
  },
  modules: {
  }
})
