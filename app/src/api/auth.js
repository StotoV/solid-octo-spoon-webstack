import axios from 'axios'

export default {
    login(username, password) {
        return axios.$post('auth/login', { username, password })
    },
    hello() {
        return axios.get('/api/hello');
    }
}
