import { createWebHistory, createRouter } from "vue-router";

import WelcomPage from "./components/WelcomPage.vue";
import Auth from "./components/AuthChoice.vue";
import AuthForm from "./components/AuthForm.vue"
const routes = [
    {path: '/', component: WelcomPage},
    {path: '/auth', component: Auth},
    {path: '/register', component:AuthForm}
    
]

export const router = createRouter({
    history: createWebHistory(),
    routes,
})
