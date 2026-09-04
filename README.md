# 🎯 Opinion Rater

A fun little AI web app: pick a random topic, write your honest opinion, and an LSTM neural network judges whether it reads as **positive** or **negative**.

## How it works
1. Hit **Shuffle** to get 3 random topics
2. Pick one and write your take
3. Hit **Rate my opinion**
4. The model scores your text and tells you if it's giving good or bad vibes

## Tech
- **Model:** LSTM (Bidirectional embedding + LSTM layer) trained on the IMDB 50k reviews dataset
- **Framework:** TensorFlow / Keras
- **Frontend:** Streamlit
- **Deployment:** Streamlit Community Cloud

## Try it live
[https://yasserwebsitefortextclass.streamlit.app/]

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
