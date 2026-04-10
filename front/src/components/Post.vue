<script lang="ts">

import { defineComponent, PropType } from "vue";
import {CommentType, PostType, HTTPErrType} from "@/types";
import Comment  from "@/components/Comment.vue";
import { useUserStore } from "@/stores/userStore";
import { refreshFetch } from "@/scripts/refresh_fetch";

export default defineComponent({
    setup(){
        const userStore =  useUserStore()
        return {userStore}
    },
    props: {
        post: {
            type: Object as PropType<PostType>,
            required: true
        }
    },
    emits: [
        "updateComment"
    ],
    components: {
        Comment
    },
    data() {
        return {
            commentText: ""
        }
    },
    methods: {
        async submitComment(): Promise<void> {
            const address = process.env.VUE_APP_ROOT_ADDRESS
            try {
                const response = await refreshFetch(`${address}/comments/${this.post.id}`, {
                    method: "POST",
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({text: this.commentText})
    
                })
                const newComment = await response.json() as CommentType
                this.commentText=""
                this.$emit("updateComment", newComment)
            } catch(e) {
                const err = e as HTTPErrType
                console.error(err)
                alert(err.detail)
            }
        }
    }
})
</script>


<template>
    <div class="post-container">
        <p class="author">Автор: {{ post.author.nickname }}</p>
        <div class="post-content">{{ post.text }}</div>
        <div class="creation-updation-time">{{ post.created_at }}</div>
        <div class="comment-container">
            <h5>Comments:</h5>
            <textarea v-if="userStore.accessToken" v-model="commentText" name="newComment" placeholder="Оставь свой комментарий" rows="1"></textarea>
            <button @click="submitComment">Отправить</button>
            <Comment v-for="comment in post.comments" :key="comment.id" :comment="comment"></Comment>
        </div>
    </div>
</template>