<script lang="ts">
  import { getRandomInt } from "./lib/util"
  import Emojis from "./lib/Emojis.svelte";

  const spot_coords = [[0, 0], [100, 70], [-10, 100]]

  let score_elem: HTMLSpanElement;

  let emoji_update = 0;
  let score = 0;
  let score_width = 100;

  function onMainClick() {
    score++;
    emoji_update = emoji_update + 1;
    score_elem.style.color = `hsl(${getRandomInt(0, 256)} 120% 70%)`
    if (score.toString().length > (score - 1).toString().length) {
      score_width += 56
      score_elem.style.width = `${score_width}px`
    }
    score_elem = score_elem
  }
  function onLeadeboardClick() {
    alert("TBA")
  }
  function onClaimClick() {
    alert("Well done! However, it seems you've been scammed...")
    score = 0;
  }
</script>

{#each spot_coords as xy}
<div class="blurry-gradient" style="top: {xy[0]}%; left: {xy[1]}%"></div>
{/each}
<Emojis update_value={emoji_update}></Emojis>
<header>
    <button on:click={onLeadeboardClick} class="reg-button header-button invert-bg">leaderboard</button>
    <h1 id="title">CRPT 
        <span class="score" bind:this={score_elem}>{score}</span>
    CLCK</h1>
    <button on:click={onClaimClick} id="finish" class="reg-button header-button invert-bg">claim</button>
</header>

<button on:click={onMainClick} class="center-button reg-button">Exec</button>

<style>
header {
    background: linear-gradient(0.25turn, rgba(165, 42, 42, 0), var(--accent-col), rgba(165, 42, 42, 0));

    margin: 0;
    transform: translate(0, 23vh);

    display: flex;
    justify-content: center;
    transition: 1000ms all ease;

}

#title {
    margin: 0 50px;
    font-family: barndoms;
    font-size: 6em;
    white-space: nowrap;
}

.blurry-gradient {
    position: fixed;
    transform: translate(-50%, -50%);
    width: 800px;
    height: 800px;
    border-radius: 50% 22% 40% 80%;  
    filter: blur(100px);
    background: radial-gradient(circle at 50% 50%,rgba(76, 0, 255, 1), rgba(76, 0, 255, 0));
    opacity: 0.2;

    z-index: -1;
}

.center-button {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
}

.center-button:hover {
    /* background-color: var(--accent-col-darker); */
    filter: invert(1);
    transition: 100ms all ease-out;
}

.reg-button {
    box-sizing: border-box;
    border: 0;
    text-align: center;
    text-decoration: none;
    color: white;
    background-color:  var(--accent-col);
    /* border-radius: 5px; */

    font-size: 20px;
    padding: 10px 20px;
    z-index: 1;
}

.header-button {
    width: 160px;

    background-color: #FFFBFBD9;
    color: black;

    font-family: 'Times New Roman', Times, serif;
    display: flex;
    align-items: center;
    justify-content: center;
}

.invert-bg {
    mix-blend-mode: soft-light;
    filter: grayscale(1);
}

.header-button:hover {
    transition: 100ms all ease-out;
    mix-blend-mode: exclusion;
}

.score {
    width: 1em;
    display: inline-block;
    text-align: center;
}
</style>
