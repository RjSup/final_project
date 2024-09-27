<script>
    import { slide } from "svelte/transition";

    // for text input
    let userText = '';
    let returnedText = '';

    // for slider input
    let sliderValue = 5;
    let returnedSliderValue = '';

    async function sendText() {
        const response = await fetch('http://localhost:5000', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: userText })
        });

        const data = await response.json();
        returnedText = data.text;
    }

    async function sendSlider() {
        const response = await fetch('http://localhost:5000', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ value: sliderValue })
        });

        const data = await response.json();
        returnedSliderValue = data.message;
    }
</script>

<h1>text sender</h1>
<form on:submit|preventDefault={sendText}>
    <label for="userText">
        Enter some text:
    </label>
    <input id="userText" type="text" bind:value={userText} />
    <button type="submit">Submit</button>
</form>

{#if returnedText}
    <p>The server returned: {returnedText}</p>
{/if}

<h1>slider</h1>
<label for="slider">
    Choose a number: {sliderValue}
    <input id="slider" type="range" min="1" max="10" bind:value={sliderValue} />
</label>

<button on:click={sendSlider}>Submit</button>

{#if returnedSliderValue}
    <p>The server returned: {returnedSliderValue}</p>
{/if}