<template>
<div class="comment-body">
    <h1>{{ comment.author.nickname }}</h1>
    <p>{{ comment.text }}</p>
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