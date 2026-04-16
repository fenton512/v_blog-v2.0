<template>
<div class="comment-body">
    <div class="author-comment">{{ comment.author.nickname }}</div>
    <div class="comment-text">{{ comment.text }}</div>
    <div class="time-container">
        <div> {{ comment.created_at }}</div>
    </div>
</div>
</template>


<script lang="ts">
import { defineComponent, PropType } from 'vue';
import { CommentType } from '@/types';
export default defineComponent({
    props: {
        comment:  {
            type: Object as PropType<CommentType>,
            required: true
        }
    }
})
</script>

<style>
.comment-body {
    display: flex;
    flex-direction: column;
    padding-left: 35px;
    font-size: 20px;
    border:2px solid rgb(240, 254, 254);;
    border-radius: 6px;
    margin-bottom: 4px;
    background-color: rgb(236, 244, 244);
}
.comment-text {
    font-size: 22px;
    padding-left: 8px;
}
.time-container {
    font-size: 14px;
}
</style>