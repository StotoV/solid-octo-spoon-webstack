import axios from 'axios'

export default {
    hello() {
        return axios.get('/api/hello')
    }
}
