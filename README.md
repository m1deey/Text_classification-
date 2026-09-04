# 🎯 Opinion Rater

A fun little AI web app: pick a random topic, write your honest opinion, and an LSTM neural network judges whether it reads as **positive** or **negative**.

## How it works
1. Hit **Shuffle** to get 3 random topics
2. Pick one and write your take
3. Hit **Rate my opinion**
4. The model scores your text and tells you if it's giving good or bad vibes

## Tech
- **Model:** LSTM (Embedding + LSTM layer) trained on the IMDB 50k reviews dataset
- **Framework:** TensorFlow / Keras
- **Frontend:** Streamlit
- **Deployment:** Streamlit Community Cloud

## Try it live
[https://yasserwebsitefortextclass.streamlit.app/]

## Run locally
pip install -r requirements.txt
streamlit run app.py

## Model details
- Vocabulary size: 15,000
- Max sequence length: 200
- Trained on balanced binary sentiment data (positive/negative)
- ~85% validation accuracy

---
Built by [Yasser](https://github.com/m1deey)
