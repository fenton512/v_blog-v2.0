<template>
  <header class="header">
    <a  href="/" class="logo">
      <img 
        src="./assets/logo_img.png" 
        alt="Blog logo" 
        style="display: block; width: 100%; height: auto;"
        loading="lazy">
      <div class="logo-name">
        VECTOR <br> BLOG
      </div>
    </a>
    <span class="head-splitter"></span>
    <nav class="nav-menu">
      <a href="">Блог</a>
      <a href="">Анонсы</a>
      <a href="">О проекте</a>
    </nav>
    <div class="acc-panel">
      <img src="./assets/avatar.svg" alt="" class="avatar">
      <span class="avatar-signature">Аккаунт</span>
      <div class="acc-links">
        <a href="">Регистрация</a>
        <div class="rectangle"></div>
        <a href="">Вход</a>
      </div>
    </div>
  </header>
  <router-view></router-view>
</template>

<script lang="ts">

import { defineComponent} from 'vue';

export default defineComponent({
  name: "app",
  components: {}
})
</script>

<style>
  .header {
    display: flex;
    background-color: #682D66;
    padding: 18px 16px;
    height: 89px;
    justify-content: space-between;
    column-gap: 10px;
    row-gap: 5px;
  }
  .logo {
    width: 214px;
    height: auto;
    display: flex;
    align-items: center;
    flex-shrink: 0;
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
    column-gap: 2px;
  }
  .acc-links {
    font-weight: 500;
    font-size: 45px;
    display: flex;
    align-items: center;
    column-gap: 8px;
  }
  .rectangle {
    width: 3px;
    height: 29px;
    background-color: var(--main-font-color);
  }
  .avatar-signature {
    display: none;
  }
  .head-splitter {
    order: 1;
    background-color: #fff;
    height: 1px;
    width: auto;
    flex-basis: 100%;
    display: none;
  }

  @media (max-width: 1024px) {
    .acc-links {
      display: none;
    }
    .acc-panel {
      flex-direction: column;
    }
    .avatar-signature {
      display: inline-block;
      font-size: 20px;
    }
  }

  @media (max-width: 800px) {
    .nav-menu {
      column-gap: 16px;
    }
  }

  @media (max-width: 664px) {
    .nav-menu {
      order: 1;
      /* flex-basis: 100%; */
    }
    .header {
      flex-wrap: wrap;
      height: auto;
      justify-content: space-between;
    }
    .head-splitter {
      display: inline;
    }
  }

  @media (max-width: 391px) {
    .nav-menu {
      font-size: 32px;
    }
  }
</style>
