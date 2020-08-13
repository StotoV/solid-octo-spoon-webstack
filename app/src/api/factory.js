import Auth from '@/api/auth'

var base_url = '/api'
export default { 
    version: '0.1.0',
    auth: new Auth(base_url)
}
