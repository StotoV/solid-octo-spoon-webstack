import Vue from 'vue'
import Axios from 'axios'
import Router from 'vue-router'

import store from './store.js'
import HelloWorld from './components/HelloWorld.vue'
import Login from './components/Login.vue'

Vue.use(Router)

let router = new Router({
    mode: 'history',
    routes: [
        {
            path: '/login',
            name: 'login',
            component: Login
        },
        {
            path: '/',
            name: 'hello',
            component: HelloWorld,
            meta: { 
                requiresAuth: true
            }
        }
    ]
})

router.beforeEach((to, from, next) => {
    if(to.matched.some(record => record.meta.requiresAuth)) {
        if (store.getters.isLoggedIn) {
            Axios.defaults.headers.common['Authorization'] = 'Bearer ' + store.getters.token
            next()
            return
        }
        next({name: 'login'}) 
    } else {
        next() 
    }
})

export default router
