<template>
    <h1>This is welcome page</h1>
    <div class="new-post-container">
        <textarea name="newPost" id="" v-model="newPostText"></textarea>
        <button @click="writePost">ЗАПОСТИТЬ</button>
    </div>
    <div class="posts-container">
            <Post v-for="post in posts" :key="post.id" :post="post" @update-comment="(newComment) => {post.comments.push(newComment)}"></Post>
    </div>
    <button @click="() => {userStore.getCurrentUser()}"></button>
</template>


<script lang="ts">
import { defineComponent} from 'vue';
import { PostType, HTTPErrType} from '@/types'
import Post from './Post.vue';
import { useUserStore } from '@/stores/userStore';
import { refreshFetch } from '@/scripts/refresh_fetch';
const address = process.env.VUE_APP_ROOT_ADDRESS

export default defineComponent({
    data() {
        return {
            posts: [] as PostType[],
            newPostText: ""
        }
    },
    methods: {
        async fetchAllPosts(): Promise<void> {
            const response = await fetch(`${address}/posts/`, {
                method: "GET",
                headers: {
                    "Content-Type": 'application/json'
                }
            })
            if (!response.ok) {
                const error = await response.json()
                console.error(error.detail)
                return
            }
            const result = await response.json() as PostType[]
            this.posts = result
        },
        async writePost() {
            try {
                const response = await refreshFetch(`${address}/posts/`, {
                    method: "POST",
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        text: this.newPostText,
                        themes: ["test"]
                    })
                })
                alert("Пост успешно создан")
                const newPost = await response.json() as PostType
                this.posts.push(newPost)
                this.newPostText = ""
            } catch (e) {
                const err = e as HTTPErrType
                console.error(err)
                alert(err.detail)
            }
        }
    },
    created() {
        this.fetchAllPosts()
    },
    components: {
        Post
    },
    setup() {
        const userStore = useUserStore()
        return {userStore}
    }
})
</script>

<style scoped>
.posts-container {
    display: flex;
    align-items: center;
    flex-direction: column;
    gap: 15px;
}
</style>