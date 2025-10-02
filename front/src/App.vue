<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <picture>
  <source srcset="mdn-logo-wide.png" media="(min-width: 600px)" />
  <img src="mdn-logo-narrow.png" alt="MDN" />
</picture>
  <!-- <HelloWorld msg="Welcome to Your Vue.js + TypeScript App"/> -->
   <!-- <TestPage/>
   <router-view></router-view> -->
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import HelloWorld from './components/HelloWorld.vue';
import TestPage from './components/TestPage.vue';


@Options({
  components: {
    TestPage,
    HelloWorld
  },
})
export default class App extends Vue {}
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
