<template>
  <div id="app">
    <Navbar />
    <div class="container my-5 mx-5">
      <router-view />
    </div>
  </div>
</template>

<script>
import Navbar from './components/Navbar'

export default {
  name: 'App',
  components: {
    Navbar,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

@import "https://cdn.jsdelivr.net/npm/bulma@0.9.1/css/bulma.min.css"
</style>
