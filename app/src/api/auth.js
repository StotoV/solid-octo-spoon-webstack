import Axios from 'axios'

import store from '@/store.js'

export default class Auth {
    constructor(base_url) {
        this.base_url = base_url.concat('/auth')
    }

    login(email, password) {
        var bodyFormData = new FormData()
        bodyFormData.set('email', email)
        bodyFormData.set('password', password)
        
        return new Promise((resolve, reject) => {
            store.dispatch('logging_in')
            Axios({
                method: 'POST',
                url: this.base_url.concat('/login'),
                data: bodyFormData
            })
            .then(response => {
                const token = response.data.token
                const user = response.data.user
                store.dispatch('login', token, user)
                .then(() => {
                    resolve()
                })
            })
            .catch(error => {
                store.dispatch('logout')
                .then(() => {
                    switch(error.response.status) {
                        case 401:
                            reject('Invalid credentials')
                            break;
                        default:
                            reject('Something went wrong on the server.')
                    }
                })
            })
        })
    }

    hello() {
        return new Promise((resolve, reject) => {
            Axios({
                method: 'GET',
                url: this.base_url.concat('/hello')
            })
            .then(response => {
                resolve(response)
            })
            .catch(error => {
                switch(error.response.status) {
                    case 401:
                        reject('Unauthorized')
                        break;
                    default:
                        reject('Something went wrong on the server.')
                }
            })
        })
    }
}
