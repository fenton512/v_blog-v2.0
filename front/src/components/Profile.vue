<template>
    <h1>PORNO</h1>
    <div v-for="(key, value) in userStore.currentUser" :key="key">{{ value }}: {{ key }}</div>
</template>


<script lang="ts">
import { useUserStore } from '@/stores/userStore';
import { defineComponent } from 'vue';

export default defineComponent({
    setup() {
        const userStore = useUserStore()
        return {userStore}
    }
})
</script>
