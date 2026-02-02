import streamlit as st

st.set_page_config(page_title="Valentine 💘", layout="centered")

st.markdown("""
<style>
body {
    background-color: #ffe6eb;
    text-align: center;
}

h1 {
    color: #ff3366;
    margin-top: 60px;
}

#no {
    position: absolute;
    background-color: #999;
    color: white;
    border: none;
    padding: 14px 28px;
    border-radius: 10px;
    cursor: pointer;
}

#yes {
    background-color: #ff3366;
    color: white;
    border: none;
    padding: 14px 28px;
    border-radius: 10px;
    cursor: pointer;
}

#gif {
    display: none;
    margin-top: 30px;
}
</style>

<h1 id="question">Will you be my Valentine? 💖</h1>

<div style="margin-top:40px;">
    <button id="yes">Yes ❤️</button>
    <button id="no">No 💀</button>
</div>

<div id="gif">
    <img src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif" width="350">
    <h2>YAYYYY 💕 I knew it 😍</h2>
</div>

<script>
const noBtn = document.getElementById("no");
const yesBtn = document.getElementById("yes");
const gif = document.getElementById("gif");
const question = document.getElementById("question");

noBtn.addEventListener("mouseover", () => {
    const x = Math.random() * 300 - 150;
    const y = Math.random() * 200 - 100;
    noBtn.style.transform = `translate(${x}px, ${y}px)`;
});

yesBtn.addEventListener("click", () => {
    question.style.display = "none";
    yesBtn.style.display = "none";
    noBtn.style.display = "none";
    gif.style.display = "block";
});
</script>
""", unsafe_allow_html=True)
