<template>
    <div class="hello">
        <h3>Hello, log in please</h3>

        <input type="text" name="email" v-model="input.email" placeholder="Email" />
        <input type="password" name="password" v-model="input.password" placeholder="Password" />
        <button type="button" v-on:click="login()">Login</button>

        <p v-html="msg"></p>
    </div>
</template>

<script>
export default {
    name: 'Login',
    data() {
        return {
            input: {
                email: '',
                password: ''
            },
            msg: ''
        }
    },
    methods: {
        async login() {
            this.msg = 'Logging in...'
            this.api.auth.login(this.input.email, this.input.password)
            .then(() => {
                this.msg = 'Logged in'
                this.$router.push({name: 'hello'})
            })
            .catch(error => {
                this.msg = error
            })
        }
    }
}
</script>

<style scoped>
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
