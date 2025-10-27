<template>
    <button class="button" :style="{width: buttonWidth + 'px', height: buttonWidth* 0.3 + 'px', fontSize: fontSize + 'em'}">
        <slot></slot>
    </button>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
    props: {
        buttonWidth: {
            type: Number,
            required: true
        },
    },
    computed: {
        fontSize() : number{
            if (this.buttonWidth >= 157) {
                return 1.5;
            } else if (this.buttonWidth >=130){
                return 1.2;
            } else if (this.buttonWidth >= 107){
                return 1;
            } else {
                return 0.68;
            }
        }
    }
})
</script>

<style>
 .button{
    border-radius: 8px;
    text-align: center;
 }
</style>