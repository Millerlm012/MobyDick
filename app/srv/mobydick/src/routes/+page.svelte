<script>
    import { browser } from '$app/environment';

    let load = fetchTop100();
    let top100 = [];

    // fetching top100 results from the API
    // please note: we have to utilize browser because we're utilizing XMLHttpRequest() which is not available in Node
    // by default this function will try to run both server side and client side, the if (browser) ensures this only runs client side
    function fetchTop100() {
        if (browser) {
            let request = new XMLHttpRequest();
            request.open('GET', 'http://localhost/api/top_100')
            request.send();
            request.onload = () => {
                let data = JSON.parse(request.response);
                for (let i=0; i<data.length; i++) {
                    let obj = {};
                    obj.count = data[i][0];
                    obj.word = data[i][1];
                    top100.push(obj);
                }
                top100 = top100;
            }
        }
    }
</script>

<style>
    .page {
        position: relative;
        background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.9)), url(/moby_dick_whale.jpg) center center no-repeat;
        background-size: cover;
        width: 100%;
        height: 100vh;
        color: white;
    }

    .content {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        color: white;
        height: 100vh;
    }

    .data {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        height: 100%;
        overflow-y: scroll;
        padding: 10px 0px;
    }

    .headers {
        font-size: 24px;
        font-weight: bold;
    }

    @media screen and (max-width: 1000px) {
        h1 {
            padding: 0px 12px;
        }
    }
</style>

<div class="page">
    <div class="content">
        <h1>Top 100 Frequent Words from Moby Dick</h1>
        <div class="headers">Word # - Word - Count</div>
        {#await load}
            <p>Loading...</p>
        {:then}
            <div class="data">
                {#each top100 as {count, word}, i}
                    <div>#{i+1} --- {word} --- {count}</div>
                {/each}
            </div>
        {/await}
    </div>
</div>
