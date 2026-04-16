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
        <p class="author">Автор: <span style="color: var(--main-bg-color);">{{ post.author.nickname }}</span></p>
        <div class="post-content">{{ post.text }}</div>
        <div class="time-container">
            <div class="creation-updation-time">Написан: <span style="color: var(--main-bg-color);">{{ post.created_at }}</span></div>
        </div>
        <div class="new-comment-container">
            <h3 style="letter-spacing: 0.05rem;">Comments:</h3>
            <div class="new-comment">
                <textarea v-if="userStore.accessToken" v-model="commentText" name="newComment" placeholder="Оставь свой комментарий" rows="1"></textarea>
                <button @click="submitComment">Отправить</button>
            </div>
        </div>
        <div class="comment-container">
            <Comment v-for="comment in post.comments" :key="comment.id" :comment="comment"></Comment>
        </div>
    </div>
</template>

<style>
.author {
    font-size: 20px;
    margin: 8px 0;

}
.post-container {
    width: 370px;
    padding: 0px 5px;
    border: 3px black solid;
    background-color: var(--main-font-color);
    color: var(--black);
    border-radius: 10px;
}
.time-container {
    display: flex;
    justify-content: right;
    margin: 7px 0;
}
.creation-updation-time {
    width: fit-content;
}
.new-comment-container {
    display: flex;
    justify-content: space-around;
}
.new-comment {
    display: flex;
    align-items: center;
}
.post-content {
    font-size: 40px;
}
</style>