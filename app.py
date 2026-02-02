import streamlit as st
import streamlit.components.v1 as components
import numpy as np

st.set_page_config(
    page_title="Valentine 💘",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Python-side sanity check (forces rerun & state) ---
if "seed" not in st.session_state:
    st.session_state.seed = int(np.random.randint(1, 10_000))

np.random.seed(st.session_state.seed)

# --- Embed FULL WEB APP ---
components.html(
f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Valentine</title>

<style>
html, body {{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
}}

body {{
    background: linear-gradient(135deg, #ffe6eb, #ffd1dc);
    font-family: Arial, Helvetica, sans-serif;
    overflow: hidden;
    text-align: center;
}}

h1 {{
    margin-top: 80px;
    color: #ff3366;
}}

button {{
    padding: 16px 34px;
    font-size: 20px;
    border-radius: 14px;
    border: none;
    cursor: pointer;
}}

#yes {{
    background: #ff3366;
    color: white;
}}

#no {{
    background: #777;
    color: white;
    position: absolute;
}}

#loader {{
    display: none;
    font-size: 30px;
    color: #ff3366;
    margin-top: 120px;
}}

#celebration {{
    display: none;
}}

.confetti {{
    position: fixed;
    width: 10px;
    height: 10px;
    background: hsl(calc(360 * var(--h)), 90%, 60%);
    animation: fall linear infinite;
}}

.heart {{
    position: fixed;
    font-size: 26px;
    animation: fall linear infinite;
}}

@keyframes fall {{
    0% {{
        transform: translateY(-10vh);
        opacity: 1;
    }}
    100% {{
        transform: translateY(110vh);
        opacity: 0.7;
    }}
}}
</style>
</head>

<body>

<h1 id="question">Will you be my Valentine? 💖</h1>

<div id="buttons">
    <button id="yes">Yes ❤️</button>
    <button id="no">No 💀</button>
</div>

<div id="loader">Loading love… 💕</div>

<div id="celebration">
    <img src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif" width="360">
    <h2>YAYYYY 💘 I knew it 😍</h2>
    <audio id="music" loop>
        <source src="https://www.bensound.com/bensound-music/bensound-love.mp3" type="audio/mpeg">
    </audio>
</div>

<script>
// --------- STATE ----------
const noBtn = document.getElementById("no");
const yesBtn = document.getElementById("yes");
const loader = document.getElementById("loader");
const celebration = document.getElementById("celebration");
const question = document.getElementById("question");
const music = document.getElementById("music");

let scale = 1;

// --------- NO BUTTON BEHAVIOR ----------
function moveNoButton() {{
    scale -= 0.08;
    if (scale < 0.35) scale = 0.35;

    const x = Math.random() * window.innerWidth * 0.6;
    const y = Math.random() * window.innerHeight * 0.5;

    noBtn.style.transform =
        `translate(${x}px, ${y}px) scale(${scale})`;
}}

noBtn.addEventListener("mouseenter", moveNoButton);
noBtn.addEventListener("touchstart", moveNoButton);

// --------- YES BUTTON ----------
yesBtn.addEventListener("click", () => {{
    question.style.display = "none";
    document.getElementById("buttons").style.display = "none";

    loader.style.display = "block";

    setTimeout(() => {{
        loader.style.display = "none";
        celebration.style.display = "block";
        music.play();
        launchConfetti();
        launchHearts();
    }}, 2000);
}});

// --------- CONFETTI ----------
function launchConfetti() {{
    for (let i = 0; i < 60; i++) {{
        const c = document.createElement("div");
        c.className = "confetti";
        c.style.left = Math.random() * 100 + "vw";
        c.style.animationDuration = (Math.random() * 3 + 2) + "s";
        c.style.setProperty("--h", Math.random());
        document.body.appendChild(c);
    }}
}}

// --------- HEART RAIN ----------
function launchHearts() {{
    for (let i = 0; i < 40; i++) {{
        const h = document.createElement("div");
        h.className = "heart";
        h.innerHTML = "💖";
        h.style.left = Math.random() * 100 + "vw";
        h.style.animationDuration = (Math.random() * 3 + 3) + "s";
        document.body.appendChild(h);
    }}
}}
</script>

</body>
</html>
""",
height=900,
scrolling=False
)
