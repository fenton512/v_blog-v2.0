<template>
    <div v-for="(key, value) in userStore.currentUser" :key="key">{{ value }}: {{ key }}</div>
    <ClassicButton :button-width="114" @click="logout()" v-if="userStore.currentUser">Выйти</ClassicButton>
</template>


<script lang="ts">
import { useUserStore } from '@/stores/userStore';
import { defineComponent } from 'vue';
import ClassicButton from '@/components/ClassicButton.vue';
import {router} from '@/router'
import { check_response } from '@/scripts/check_response';
import { HTTPErrType } from '@/types';

export default defineComponent({
    setup() {
        const userStore = useUserStore()
        return {userStore, router}
    },
    components: {
        ClassicButton
    },
    methods: {
      async logout() {
            const address = process.env.VUE_APP_ROOT_ADDRESS
            try {
                var response = await check_response(`${address}/users/refresh/logout`, {
                    method: "PATCH",
                    credentials: "include"
                })
            }
            catch(e) {
                const error = e as HTTPErrType
                console.error(error)
                alert(error.detail)
                return
            }
            let output = await response.json()
            alert(`${output.message}`)
            this.userStore.logout() 
            router.push('/');
        }
    }
})
</script>
