<template>
  <div class="header">
    <div class="logo">
      <img src="./assets/logo_img.png" alt="" style="display: block; width: 100%; height: auto;">
      <div class="logo-name">
        VECTOR <br> BLOG
      </div>
    </div>
    <nav class="nav-menu">
      <a href="">Блог</a>
      <a href="">Анонсы</a>
      <a href="">О проекте</a>
    </nav>
    <div class="acc-panel">
      <img src="./assets/avatar.svg" alt="" class="avatar">
      <div class="acc-links">
        <a href="">Регистрация</a>
        |
        <a href="">Вход</a>
      </div>
    </div>
  </div>
  <router-view></router-view>
</template>

<script lang="ts">

import { defineComponent} from 'vue';
// import HelloWorld from './components/HelloWorld.vue';
// import TestPage from './components/TestPage.vue';
export default defineComponent({
  name: "app",
  components: {}
})
</script>

<style>
  body {
    background-color: var(--main-bg-color);
  }
  .header {
    display: flex;
    background-color: #682D66;
    padding: 18px 16px;
    height: 89px;
    justify-content: space-between;
  }
  .logo {
    width: 214px;
    height: auto;
    display: flex;
    align-items: center;
  }
  .logo img {
    width: auto;
    height: auto;
    max-width: 78px;
    max-height: 85.22px;
  }
  .logo-name {
    font-weight: 500;
    font-size: 45px;

    line-height: 67%;
    letter-spacing: 0.02em;
    text-transform: uppercase;
    text-align: right;

    padding-left: 2px;
  }
  .nav-menu {
    width: 409px;
    color: #fff;

    font-weight: 500;
    font-size: 45px;
    
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 48px;
  }
  .acc-panel {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .acc-links {
    font-weight: 500;
    font-size: 45px;
  }
</style>
