<script lang="ts">
import { defineComponent } from 'vue';
import {useUserStore} from '@/stores/userStore'
import { refreshFetch } from '@/scripts/refresh_fetch';
import { check_response } from '@/scripts/check_response';
import { HTTPErrType } from '@/types';

const address = process.env.VUE_APP_ROOT_ADDRESS
export default defineComponent({
    setup() {
        const userStore = useUserStore()
        return {userStore}
    },
    data() {
        return {
            email: "",
            authType: "default"
        }
    },
    methods: {
        async handleSubmit(): Promise<void> {
            let endpoint = (this.authType === "register" && this.authType) ? "/users/" : "/users/token/"
            const form = this.$refs.submitForm as HTMLFormElement
            try {
                const result = await check_response(`${address}${endpoint}`, {
                    method: "POST",
                    credentials: "include",
                    body: new FormData(form)
                })
                let response = await result.json()
                this.userStore.accessToken = (this.authType === "register") ? response.token.access_token : response.access_token
                // this.userStore.refreshToken = (this.authType === "register") ? response.token.refresh_token : response.refresh_token
                const currentUserRequest =  await refreshFetch(`${address}/users/me`, {
                    method: "GET"
                })
                let currentUser = await currentUserRequest.json()
                this.userStore.currentUser = currentUser
                console.log(this.userStore.accessToken, this.userStore.currentUser)
            } 
            catch (e) {
                const err = e as HTTPErrType
                console.error(err)
                alert(err.detail)
            }
        }
    }, 
})
</script>


<template>
    <input type="radio" name="auth_type" v-model="authType" id="reg" value="register">
    <label for="reg">Регистрация</label>
    <input type="radio" name="auth_type" v-model="authType" id="log" value="login">
    <label for="log">Логин</label>
    <form @submit.prevent="handleSubmit" ref="submitForm">
        <input v-model="email" type="email" placeholder="email" name="username" autocomplete="on"/>
        <input type="text" placeholder="Пароль" name="password">
        <input v-if="authType=='register'" type="text" placeholder="oleg228" name="nickname">
        <button type="submit">Отправить</button>
    </form>
    <div>{{ authType }}</div>

</template>