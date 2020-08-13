import Vue from 'vue'
import router from './router.js'
import Factory from './api/factory.js'
import Axios from 'axios'
import './assets/css/styles.css'

Vue.config.productionTip = false
Vue.prototype.$http = Axios;

// Load the API
Vue.mixin({
    data: function() {
        return {
            api: Factory
        }
    },
})

new Vue({
    el: '#app',
    router
})
