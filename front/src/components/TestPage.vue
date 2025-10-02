<script lang="ts">

import { defineComponent } from 'vue'

interface Link {
    title: string,
    path: string,
    id: number
}

  
  

export default defineComponent({
    data() {
    return {
        pages: [
        {title: "hello", path: "/hi", id: 0},
        {title: "test", path: "/test", id: 1}
        ] as Link[],
    }

    },

    methods: {
        goTo(path: string){
            this.$router.push(path);
            }
        }
    })
</script>

<template>
    <ul v-for= "page in pages" :key="page.id">
        <li>
            <a href="#" @click="goTo(page.path)">{{page.title}}</a>
        </li>
    </ul>
</template>