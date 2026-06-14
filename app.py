import streamlit as st

st.set_page_config(
    page_title="Smart Skincare Recommender",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

from utils.helper import load_raw_dataset, inject_neobrutalism_design
from models.preprocessing import run_data_preprocessing
from models.feature_engineering import run_feature_engineering
from models.recommender import SkincareHybridRecommender

# Terapkan Tema Visual Soft Neobrutalism Premium
inject_neobrutalism_design()

# AUTOMATION ENGINE: Pipeline Preprocessing & Feature Engineering Berjalan Otomatis di Sini
if 'recommender' not in st.session_state:
    raw_df = load_raw_dataset()
    if not raw_df.empty:
        # Step 1: Preprocessing Data Cleaning
        cleaned_df = run_data_preprocessing(raw_df)
        # Step 2: Feature Engineering Fitur Tekstual
        engineered_df = run_feature_engineering(cleaned_df)
        # Step 3: Bangun Instance Vektor Space Model Utama
        st.session_state.recommender = SkincareHybridRecommender(engineered_df)

# Identity Header Sidebar
st.sidebar.markdown("""
    <div style='text-align: center; padding: 12px; border: 3px solid #000; background:#FFE9EC; border-radius:10px; box-shadow: 3px 3px 0px #000;'>
        <h2 style='margin:0; font-size:1.4rem; color:#000;'>🌸 GlowPlan AI</h2>
        <small style='font-weight:600; color:#000;'>Next-Gen Rec Framework</small>
    </div>
    <br>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# VISUAL RENDERING: PREMIUM PRODUCT LANDING PAGE
# ----------------------------------------------------
st.markdown("""
    <div class='cloud-banner'>
        ☁️ 🕊️ <i>"Discovering perfect skincare, cloud by cloud, ingredient by ingredient."</i> 🕊️ ☁️
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class='neo-box-pink' style='text-align: center; padding: 45px 20px;'>
        <h1 class='brand-title'>🌸 Smart Skincare Recommendation System</h1>
        <div class='brand-tagline'>Discover skincare products that truly match your skin.</div>
        <p style='font-size: 1.15rem; max-width: 850px; margin: 0 auto 25px auto; color: #000; font-weight: 500;'>
            Stop guessing and start choosing skincare based on your skin condition, preferred product type, and budget. 
            Powered by an advanced hybrid Content-Based & Knowledge-Based Recommendation Framework.
        </p>
    </div>
""", unsafe_allow_html=True)

# Feature Highlights 3 Cards
st.markdown("<h3 style='font-weight:800; color:#000; margin-bottom:15px;'>🚀 Core Platform Features</h3>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <div class='neo-box' style='height: 220px;'>
            <h3 style='margin-top:0;'>✨ Personalized Recs</h3>
            <p>Dapatkan rekomendasi instan berakurasi tinggi yang dipetakan sesuai profil biologi kulit Anda.</p>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class='neo-box' style='height: 220px;'>
            <h3 style='margin-top:0;'>🧪 Ingredient Analysis</h3>
            <p>Pemrosesan data kosmetik menggunakan metode pembobotan teks TF-IDF untuk mencocokkan kemiripan bahan aktif.</p>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
        <div class='neo-box' style='height: 220px;'>
            <h3 style='margin-top:0;'>💰 Budget-Friendly</h3>
            <p>Sistem cerdas menyaring produk berkinerja tinggi tanpa melewati ambang batas kemampuan finansial Anda.</p>
        </div>
    """, unsafe_allow_html=True)

# User Flow Interactive Progress Section
st.markdown("""
    <div class='neo-box' style='background:#FFF9D6 !important; text-align:center;'>
        <h3 style='margin-top:0; margin-bottom:20px;'>💡 How It Works (Skin Journey Flow)</h3>
        <div style='display: flex; justify-content: space-around; flex-wrap: wrap; font-weight:800; gap: 10px; color:#000;'>
            <div style='padding:12px; border:2px solid #000; background:#fff; border-radius:8px;'>1️⃣ Tell us about your skin</div>
            <div style='padding:12px; border:2px solid #000; background:#fff; border-radius:8px;'>2️⃣ Choose your preferred product</div>
            <div style='padding:12px; border:2px solid #000; background:#fff; border-radius:8px;'>3️⃣ Set your budget</div>
            <div style='padding:12px; border:2px solid #000; background:#fff; border-radius:8px;'>4️⃣ Receive personalized recommendations</div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; font-weight:800; font-size:1.1rem; color:#000;'>Silakan gunakan menu navigasi bawaan pada sidebar samping untuk memulai perjalananmu! 🚀</p>", unsafe_allow_html=True)