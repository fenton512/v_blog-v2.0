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
    <div class="acc-panel" @click.stop="handleAvatarClick()">
      <img src="./assets/avatar.svg" alt="" class="avatar">
      <div v-if="isLongRegistration" class="acc-links">
        <a href="/register">Регистрация</a>
        <div class="rectangle"></div>
        <a href="/login">Вход</a>
      </div>
      <span v-else>Аккаунт</span>
    </div>
  </header>
  <Transition name="RegLog">
    <RegistrationPage v-if="visiableRegLog" v-click-outside="closeRegLogMenu"></RegistrationPage>
  </Transition>
  <router-view></router-view>
</template>

<script lang="ts">
import { defineComponent} from 'vue';
import RegistrationPage from './components/RegistrationPage.vue';

export default defineComponent({
  data() {
    return {
       isLongRegistration: true,
       visiableRegLog: false,
    }
  },
  name: "app",
  components: {
    RegistrationPage,
  },
  methods: {
    rednderAccauntSignature(): void {
      this.isLongRegistration = window.innerWidth > 1024;
    },
    closeRegLogMenu(): void {
      this.visiableRegLog = false;
    },
    handleAvatarClick(): void {
      if (this.isLongRegistration) {
        //play animation
      }
      else {
        this.visiableRegLog = true;
      }
    }
  },
  mounted() {
    this.rednderAccauntSignature();
    window.addEventListener("resize", this.rednderAccauntSignature);
  },
  unmounted() {
    window.removeEventListener("resize", this.rednderAccauntSignature);
  }

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

 .RegLog-enter-active {
  animation: RegLogAppear 1s;
 }
 .RegLog-leave-active {
  animation: RegLogAppear 0.5s reverse;
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

  @keyframes RegLogAppear {
    0% {
      opacity: 0;
    }
    20% {
      transform: translateY(5%);
      opacity: 0.2;;
    }
    100% {
      opacity: 1;
    }
  }
</style>
