<script>
    import { slide } from "svelte/transition";

    // for initial investment value
    let initalAmount = '';
    let returnedAmount = '';

    // for slider input
    let sliderValue = 5;
    let returnedSliderValue = '';

    async function sendInvestmentAmout() {
        const response = await fetch('http://localhost:5000', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ investmentAmount: initalAmount })
        });

        const data = await response.json();
        returnedAmount = data.message;
    }

    async function sendSlider() {
        const response = await fetch('http://localhost:5000', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ sliderValue: sliderValue })
        });

        const data = await response.json();
        returnedSliderValue = data.message;
    }
</script>

<h1>Inital investment</h1>
<label for="initialAmount">
    Enter inital investment:
    <input id="initialAmount" type="number" bind:value={initalAmount}>
</label>

<button on:click={sendInvestmentAmout}>Submit</button>

{#if returnedAmount}
    <p>The server returned: {returnedAmount}</p>
{/if}

<h1>Risk slider</h1>
<label for="slider">
    Choose a number: {sliderValue}
    <input id="slider" type="range" min="1" max="10" bind:value={sliderValue} />
</label>

<button on:click={sendSlider}>Submit</button>

{#if returnedSliderValue}
    <p>The server returned: {returnedSliderValue}</p>
{/if}