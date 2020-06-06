<template>
    <div class="hello">
        <h1>{{ msg }}</h1>
        <p>{{ body }}</p>
    </div>
</template>

<script>
export default {
    name: 'HelloWorld',
    props: {
        msg: {
            type: String,
            required: true
        },
        body: {
            type: String,
            required: true
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
