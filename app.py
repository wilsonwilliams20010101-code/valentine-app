import streamlit as st

st.set_page_config(page_title="Valentine 💘", layout="centered")

st.markdown("""
<style>
body {
    background: #ffe6eb;
    overflow: hidden;
    text-align: center;
    font-family: sans-serif;
}

h1 {
    color: #ff3366;
    margin-top: 80px;
}

button {
    padding: 14px 28px;
    font-size: 18px;
    border-radius: 12px;
    border: none;
    cursor: pointer;
}

#yes {
    background-color: #ff3366;
    color: white;
}

#no {
    background-color: gray;
    color: white;
    position: absolute;
}

#loader {
    display: none;
    font-size: 28px;
    color: #ff3366;
    margin-top: 100px;
}

#celebration {
    display: none;
}

.confetti, .heart {
    position: fixed;
    animation: fall 5s linear infinite;
}

.confetti {
    width: 10px;
    height: 10px;
    background: red;
}

.heart {
    font-size: 24px;
}

@keyframes fall {
    0% { top: -10%; }
    100% { top: 110%; }
}
</style>

<h1 id="question">Will you be my Valentine? 💖</h1>

<div id="buttons">
    <button id="yes">Yes ❤️</button>
    <button id="no">No 💀</button>
</div>

<div id="loader">Loading love... 💕</div>

<div id="celebration">
    <img src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif" width="350">
    <h2>YAYYYY 💘 I knew it 😍</h2>
    <audio autoplay loop>
        <source src="https://www.bensound.com/bensound-music/bensound-love.mp3" type="audio/mpeg">
    </audio>
</div>

<script>
const noBtn = document.getElementById("no");
const yesBtn = document.getElementById("yes");
const loader = document.getElementById("loader");
const celebration = document.getElementById("celebration");
const question = document.getElementById("question");
let scale = 1;

// NO button runs away + shrinks
noBtn.addEventListener("mouseover", () => {
    scale -= 0.1;
    if (scale < 0.4) scale = 0.4;
    noBtn.style.transform =
        `translate(${Math.random()*300-150}px, ${Math.random()*200-100}px) scale(${scale})`;
});

// YES click
yesBtn.addEventListener("click", () => {
    question.style.display = "none";
    document.getElementById("buttons").style.display = "none";
    loader.style.display = "block";

    setTimeout(() => {
        loader.style.display = "none";
        celebration.style.display = "block";
        startConfetti();
        startHearts();
    }, 2000);
});

// Confetti
function startConfetti() {
    for (let i = 0; i < 40; i++) {
        const c = document.createElement("div");
        c.className = "confetti";
        c.style.left = Math.random() * 100 + "vw";
        c.style.animationDuration = (Math.random()*3 + 2) + "s";
        document.body.appendChild(c);
    }
}

// Heart rain
function startHearts() {
    for (let i = 0; i < 30; i++) {
        const h = document.createElement("div");
        h.className = "heart";
        h.innerHTML = "💖";
        h.style.left = Math.random() * 100 + "vw";
        h.style.animationDuration = (Math.random()*3 + 2) + "s";
        document.body.appendChild(h);
    }
}
</script>
""", unsafe_allow_html=True)
