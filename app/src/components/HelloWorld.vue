<template>
    <div class="hello">
        <h1>Hello world page</h1>
        <p v-html="msg"></p>

        <button type="button" v-on:click="logout()">Logout</button>
    </div>
</template>

<script>
import store from '@/store.js'

export default {
    name: 'HelloWorld',
    data() {
        return {
            msg: ''
        }
    },
    created: function() {
        this.hello()
    },
    methods: {
        logout() {
            store.dispatch('logout')
            this.$router.push({name: 'login'})
        },
        async hello() {
            this.msg = 'Loading message...'

            this.api.auth.hello()
            .then(response => {
                this.msg = response.data
            })
            .catch(error => {
                this.msg = error
            })
        }
    }
}
</script>

<style scoped>
.hello {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
h3 {
    margin: 40px 0 0;
}
ul {
    list-style-type: none;
    padding: 0;
}
li {
    display: inline-block;
    margin: 0 10px;
}
a {
    color: #42b983;
}
</style>
