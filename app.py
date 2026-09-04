# app.py
import streamlit as st
import pickle
import random
import time
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

MAX_LEN = 200

st.set_page_config(page_title="Opinion Rater", page_icon="🎯", layout="centered")

@st.cache_resource
def load_assets():
    model = load_model("lstm_sentiment.h5")
    with open("tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)
    return model, tokenizer

model, tokenizer = load_assets()

TOPICS = {
    "🍕 Pizza": "🍕", "✈️ Your last vacation": "✈️", "🚗 Electric cars": "🚗",
    "💻 Remote work": "💻", "📱 Your phone": "📱", "☕ Coffee vs tea": "☕",
    "📲 Social media": "📲", "🏙️ Your city": "🏙️", "🎓 Online courses": "🎓",
    "👕 Fast fashion": "👕", "🎮 Video games": "🎮", "🎬 Netflix": "🎬"
}

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #1e1e2f, #2d2d44);
    color: white;
}
h1 {
    text-align: center;
    background: linear-gradient(90deg, #ff6ec4, #7873f5);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 3em !important;
}
div.stButton > button {
    background: linear-gradient(90deg, #7873f5, #ff6ec4);
    color: white;
    border-radius: 20px;
    border: none;
    padding: 10px 25px;
    font-weight: bold;
    transition: 0.3s;
}
div.stButton > button:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🎯 Opinion Rater</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Pick a topic, drop your take, get judged by AI 😈</p>", unsafe_allow_html=True)

if "topics" not in st.session_state:
    st.session_state.topics = random.sample(list(TOPICS.keys()), 3)

col1, col2 = st.columns([3, 1])
with col2:
    if st.button("🎲 Shuffle"):
        st.session_state.topics = random.sample(list(TOPICS.keys()), 3)

with col1:
    topic = st.radio("Choose your subject:", st.session_state.topics)

text = st.text_area("Write your opinion here 👇", height=120)

if st.button("🔥 Rate my opinion"):
    if text.strip():
        with st.spinner("Thinking..."):
            time.sleep(0.6)
            seq = tokenizer.texts_to_sequences([text])
            padded = pad_sequences(seq, maxlen=MAX_LEN, padding="post", truncating="post")
            pred = float(model.predict(padded)[0][0])

        if pred >= 0.5:
            st.success(f"✅ Positive vibes! ({pred*100:.0f}% confidence)")
            st.balloons()
        else:
            st.error(f"❌ Negative energy detected ({(1-pred)*100:.0f}% confidence)")

        st.progress(pred)
        st.caption(f"Raw score: {pred:.3f} — closer to 1 = positive, closer to 0 = negative")
    else:
        st.warning("Write something first, come on.")
