<template>
    <main  ref="myElement" class="main" :style="{width: windowWidth * 0.5 + 'px' }">
        <!-- <div class="exitCross">&#10006;</div> -->
        <h1>This is registration</h1>
    </main>
</template>


<script lang="ts">
import { defineComponent } from "vue";

    export default defineComponent({
        data() {
            return {
                windowWidth: 0,
                elementWidth: 0.
            }
        },
        mounted() {
            this.getWindowWidth();
            window.addEventListener('resize', this.getWindowWidth)
        },
        unmounted() {
            window.removeEventListener('resize', this.getWindowWidth);
        },
        methods: {
            getWindowWidth(): void {
                this.windowWidth = (window.innerWidth);
            },
            getElementWidth(): number {
                const myElement = this.$refs.myElement as HTMLElement;
                return myElement.offsetWidth;
            }
        }
    })
</script>
<style scoped>
    .main {
        z-index: 1;

        position: absolute;
        top: 45%;
        left: 25%;

        background-color: gray;
        border: 4.70px solid var(--black);
        border-radius: 30px;

    }
    /* .exitCross {
        position: absolute;
        right: 12px;
        top: 1px;

        width: 3%;
    } */
</style>