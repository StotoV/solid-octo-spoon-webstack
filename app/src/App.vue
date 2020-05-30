<template>
    <div id="app">
        <HelloWorld :msg="msg"/>
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
            errors: []
        }
    },
    created: function() {
        this.login()
    },
    methods: {
        login: function() {
            this.api.auth.hello()
            .then(response => {
                this.msg = response.data;
            })
            .catch(e => {
                console.log(e);
                this.msg = 'Error, the API failed to say hello.';
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
