<template>
    <main class="main" :style="{width: elementWidth + 'px' }">
        <div class="pictures">
            <img :style="{width: imgWidth + 'px', height: imgWidth + 'px'}" src="../assets/vector_with_loopa.gif" alt="" class="vector">
            <div :style="{width: cloudWidth + 'px', height: cloudWidth + 'px'}" class="cloud"> 
                <div class="cloudText" :style="{width: cloudText + 'px'}">А я тебя вообще знаю?</div>
            </div>        
        </div>
        <div class="buttons">
            <ClassicButton :buttonWidth="buttonWidth" class="reg-log-but">войти</ClassicButton>
            <ClassicButton :button-width="buttonWidth" class="reg-log-but">зарегистрироваться</ClassicButton>
        </div>
    </main>
</template>


<script lang="ts">
import { defineComponent } from "vue";
import ClassicButton from "./ClassicButton.vue";
    export default defineComponent({
        data() {
            return {
                elementWidth: 0,
            }
        },
        mounted() {
            this.getElementWidth();
            window.addEventListener('resize', this.getElementWidth);
        },
        unmounted() {
            window.removeEventListener('resize', this.getElementWidth);
        },
        methods: {
            getElementWidth(): void {
                this.elementWidth = window.innerWidth*0.7;
            },
        },
        components: {
            ClassicButton
        },
        computed: {
            imgWidth(): number {
                return this.elementWidth* 0.4;
            },
            cloudWidth(): number {
                return this.elementWidth*0.3;
            },
            buttonWidth(): number {
                return this.elementWidth * 0.32;
            },
            cloudText(): number {
                return this.cloudWidth * 0.8;
            }
        }
    })
</script>
<style scoped>
    .main {
        z-index: 1;

        position: absolute;
        top: 45%;
        left: 15%;

        background-color: var(--white);
        border: 4.70px solid var(--black);
        border-radius: 30px;

        display: flex;
        align-items: center;
        flex-wrap: wrap;
        flex-direction: column;
        gap: 8px;

        padding: 12px 0 26px;
        box-sizing: content-box;

    }
    .cloud{
        background-image: url('../assets/phrase_cloude.svg');
        background-size: contain;
        background-repeat: no-repeat;

        display: flex;
        justify-content: center;
    }
    .cloudText {
        z-index: 2;
        position: relative;
        top: 17%;
        display: block;
        text-align: center;
        
        
        color: var(--black);
        font-size: 3.2vw;
    }
    .pictures{
        display: flex;
        flex-direction: row;
    }
    .buttons{
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
        
        width: 100%;

    }
    .reg-log-but{
        border: 2px solid var(--black);
        background-color: var(--brown);

        font-size: 1.5em;
        /* border-radius: 34px; */
    }

    

</style>