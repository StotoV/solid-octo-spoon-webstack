<template>
    <div id="app">
        <HelloWorld :msg="msg" :body="body"/>
    </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
    name: 'App',
    components: {
        HelloWorld
    },
    data: function() {
        return {
            msg: String,
            body: String,
        }
    },
    created: function() {
        this.hello()
        this.bodyCall()
    },
    methods: {
        async hello() {
            this.msg = 'Loading message...'

            this.api.auth.hello()
            .then(response => {
                this.msg = response.data
            })
            .catch(function() {
                this.msg = 'Error, the API failed to say hello.'
            })
        },
        async bodyCall() {
            this.body = 'Loading body...'

            this.api.auth.hello()
            .then(response => {
                this.body = response.data
            })
            .catch(function() {
                this.body = 'Error, the API failed to say hello.'
            })
        }
    }
}
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
</style>
