<template>
    <div v-for="(key, value) in userStore.currentUser" :key="key">{{ value }}: {{ key }}</div>
    <ClassicButton :button-width="114" @click="() => {userStore.logout(); router.push('/');}" v-if="userStore.currentUser">Выйти</ClassicButton>
</template>


<script lang="ts">
import { useUserStore } from '@/stores/userStore';
import { defineComponent } from 'vue';
import ClassicButton from '@/components/ClassicButton.vue';
import {router} from '@/router'

export default defineComponent({
    setup() {
        const userStore = useUserStore()
        return {userStore, router}
    },
    components: {
        ClassicButton
    }
})
</script>
