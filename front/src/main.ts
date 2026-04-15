import { createApp } from 'vue'
import App from './App.vue'
import {router} from './router'
import "./assets/main.css"
import { clickOutside } from './directives/outsideClick'
import {createPinia} from 'pinia'
import { createPersistedState } from 'pinia-plugin-persistedstate'


createApp(App).use(createPinia().use(createPersistedState())).use(router).directive('click-outside', clickOutside).mount('#app')
