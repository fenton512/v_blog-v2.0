import { createApp } from 'vue'
import App from './App.vue'
import {router} from './router'
import "./assets/main.css"
import { clickOutside } from './directives/outsideClick'
import {createPinia} from 'pinia'


createApp(App).use(createPinia()).use(router).directive('click-outside', clickOutside).mount('#app')
