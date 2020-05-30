import Vue from 'vue'
import App from './App.vue'
import Factory from './api/factory.js'

Vue.config.productionTip = false

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
    render: h => h(App),
})
