import { createWebHistory, createRouter } from "vue-router";

import WelcomPage from "./components/WelcomPage.vue";
import Registration from "./components/RegistrationPage.vue";
const routes = [
    {path: '/', component: WelcomPage},
    {path: '/register', component: Registration}
]

export const router = createRouter({
    history: createWebHistory(),
    routes,
})
