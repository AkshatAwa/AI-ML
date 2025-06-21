import streamlit as st
import pickle

model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.set_page_config(page_title="Email Spam Classifier", page_icon="📬", layout="centered")

st.markdown("""
    <style>
        .main-title {
            font-size: 36px;
            font-weight: 600;
            color: #00d4ff;
            text-align: center;
            margin-top: 10px;
        }
        .sub-text {
            text-align: center;
            color: #555;
            font-size: 16px;
            margin-bottom: 30px;
        }
        .footer {
            text-align: center;
            font-size: 13px;
            color: gray;
            margin-top: 60px;
        }
        .stTextArea textarea {
            background-color: #1e1e1e;   /* Dark grey */
            color: white;                /* Text white */
            font-size: 15px;
            border: 0.3px solid #00d4ff;  
        }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title(" Project Info")
    st.markdown("""
     Email Spam Classifier 

    This tool uses Machine Learning to classify emails into:
    - ✅ Ham (Legit)
    - 🚫 Spam (Scam)

    ---
     Pro Tip:
    _If you have to pay for the internship, it's likely to be a scam._
    """)
st.markdown('<div class="main-title">Email Spam Classifier</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Check whether an email is safe or spam using ML.</div>', unsafe_allow_html=True)

# Input
user_input = st.text_area(" Paste your email content here:")

# Predict
if st.button(" Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some content to analyze.")
    else:
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)[0]

        st.markdown("### Result:")
        if prediction == 1:
            st.success("✅ This email is **safe (Ham)**.")
        else:
            st.error("🚫 This email is **Spam**. Be cautious!")
            st.markdown("> 💡 _If you have to pay for the internship, it's likely to be a scam._")

st.markdown('<div class="footer">Made with ❤️ by Akshat Awasthi | Bennett University</div>', unsafe_allow_html=True)
