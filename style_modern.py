
import streamlit as st

def set_modern_style():
    st.markdown("""
    <style>
    body { background-color: #f4f7fa; margin: 0; }
    .stApp { font-family: 'Segoe UI', sans-serif; color: #2c3e50; }
    header { display: none; }
    h1, h2, h3 { color: #2c3e50; }
    .stButton > button {
        background-color: #1a73e8;
        color: white;
        padding: 0.5em 1.5em;
        border-radius: 6px;
        border: none;
        font-weight: 600;
        font-size: 15px;
    }
    .stButton > button:hover {
        background-color: #1558b0;
    }
    .stTextInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: #f0f4f8;
        border-radius: 5px;
    }
    .stDataFrame { font-size: 0.9rem; }
    .welcome-banner {
        background: linear-gradient(90deg, #2c7be5, #48a0f8);
        color: white;
        padding: 1rem 2rem;
        border-radius: 6px;
        margin-bottom: 1.5rem;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)
