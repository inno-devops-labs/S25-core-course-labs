<script lang="ts">
    import { getRandomInt } from "./util"

    export let update_value = 0;

    // [9986, 10160] stripped range
    const emoji_range = [
        [128513, 128591], [10000, 10160], [128640, 128704]
    ];

    // TODO: set values depending on screen size
    const rows = 5, cols = 11
</script>

{#key update_value}
<div class="container {update_value == 0 ? "perp-end" : "perp-animated"}">
{#each {length: rows} as _, i}
    {@const lim = i % 2 == 0 ? cols : Math.ceil(cols * 0.8)}
    <div class="emoji-row">
    {#each {length: lim} as _, j}
        {@const dist = Math.sqrt(Math.pow(((lim - 1) / 2 - j) * 1, 2) + Math.pow(((rows - 1) / 2 - i) * 0.5, 2))}
        {@const emoji = String.fromCodePoint(getRandomInt(emoji_range[1][0], emoji_range[1][1]))}
        {#if Math.floor(lim / 2) == j && Math.floor(rows / 2) == i}
            <span class="emoji-img" style="transform: translateZ({Math.round(dist * 100)}px); visibility: hidden;">{emoji}</span>
        {:else}
            <span class="emoji-img" style="transform: translateZ({Math.round(dist * 100)}px);">{emoji}</span>
        {/if}
    {/each}
    </div>
{/each}
</div>
{/key}

<style>
    @keyframes -global-perpAnimation {
        0% {
            perspective: 0px;
        }
        100% {
            perspective: 1500px;
        }
    }

    @keyframes -global-opacityAnimation {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    .perp-animated {
        animation: 10s ease-out 0s 1 perpAnimation both;
        animation-timing-function: cubic-bezier(0,.78,.54,1.21);
        perspective: 1500px;
    }

    .perp-end {
        perspective: 1500px;
    }

    .container {
        width: 100%;
        height: 100%;
        position: fixed;
        left: 0px;
        right: 0px;
        z-index: -1;

        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-around;
        
        perspective-origin: 50% 50%;
    }

    .emoji-row {
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: space-around;
        transform: translateZ(0px) !important;
        perspective: inherit;
    }

    .emoji-img {
        min-width: fit-content;
        font-size: 3em;
    }
</style>