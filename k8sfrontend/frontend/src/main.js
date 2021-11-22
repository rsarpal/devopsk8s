import Vue from 'vue'
import App from './App.vue'
import router from '@/router'
import { createProvider } from './vue-apollo'
//import VueApollo from "vue-apollo"

Vue.config.productionTip = false

new Vue({
  router,
  apolloProvider: createProvider(),
  render: h => h(App)
}).$mount('#app')


// apolloProvider: createProvider({
//   httpEndpoint: 'http://localhost:8000/graphql',
//   wsEndpoint: null,
// }),