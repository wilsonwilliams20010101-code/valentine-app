import streamlit as st

st.set_page_config(page_title="Valentine 💘", layout="centered")

st.markdown("""
<style>
body { background-color: #ffe6eb; text-align: center; }
h1 { color: #ff3366; }

#no-btn {
    position: absolute;
    background-color: gray;
    color: white;
    border: none;
    padding: 12px 25px;
    border-radius: 10px;
}

#yes-btn {
    background-color: #ff3366;
    color: white;
    border: none;
    padding: 12px 25px;
    border-radius: 10px;
}
</style>

<h1>Will you be my Valentine? 💖</h1>

<button id="yes-btn" onclick="sendYes()">Yes ❤️</button>
<button id="no-btn">No 💀</button>

<script>
const noBtn = document.getElementById("no-btn");
noBtn.addEventListener("mouseover", () => {
  const x = Math.random() * 300;
  const y = Math.random() * 200;
  noBtn.style.transform = `translate(${x}px, ${y}px)`;
});

function sendYes() {
  window.location.href = "?yes=true";
}
</script>
""", unsafe_allow_html=True)

if st.experimental_get_query_params().get("yes"):
    st.image("https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif")
    st.success("YAYYYY 💕 I knew it 😍")
