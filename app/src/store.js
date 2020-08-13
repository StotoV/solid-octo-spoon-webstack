import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        status: '',
        token: localStorage.getItem('token') || '',
        user : {}
    },
    mutations: {
        auth_request(state){
            state.status = 'loading'
        },
        auth_success(state, token, user){
            state.status = 'success'
            state.token = token
            state.user = user
            localStorage.setItem('token', token)
        },
        auth_error(state){
            state.status = 'error'
        },
        logout(state){
            state.status = ''
            state.token = ''
            localStorage.removeItem('token')
        },
    },
    actions: {
        logging_in({commit}) {
            return new Promise((resolve) => {
                commit('auth_request')
                resolve()
            })
        },
        login({commit}, token, user) {
            return new Promise((resolve) => {
                commit('auth_success', token, user)
                resolve()
            })
        },
        logout({commit}){
            return new Promise((resolve) => {
                commit('logout')
                resolve()
            })
        }
    },
    getters : {
        token: state => state.token,
        isLoggedIn: state => !!state.token,
        authStatus: state => state.status,
    }
});
