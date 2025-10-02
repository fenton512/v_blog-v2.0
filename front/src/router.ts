import { createWebHistory, createRouter } from "vue-router";

import HelloWorld from "./components/HelloWorld.vue";
import Test from "./components/TestPage.vue";

const routes = [
    {path: '/hi', component: HelloWorld},
    {path: '/test', component: Test}
]

export const router = createRouter({
    history: createWebHistory(),
    routes,
})
