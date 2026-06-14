import streamlit as st
import pandas as pd
import ast
from utils.helper import load_raw_dataset, inject_neobrutalism_design
from models.preprocessing import run_data_preprocessing
from models.feature_engineering import run_feature_engineering
from models.recommender import SkincareHybridRecommender

# 1. Inject Style Neobrutalism yang Konsisten
inject_neobrutalism_design()

# Menyembunyikan teks navigasi bawaan "app" agar sidebar bersih dan rapi
st.markdown("<style>[data-testid='stSidebarNav'] ul li:first-child span { display: none; }</style>", unsafe_allow_html=True)

# 2. Inisialisasi Data & Model di Background
@st.cache_resource
def init_recommender_system():
    raw_df = load_raw_dataset()
    cleaned_df = run_data_preprocessing(raw_df)
    engineered_df = run_feature_engineering(cleaned_df)
    
    # Memakai class SkincareHybridRecommender dari models/recommender.py
    recommender = SkincareHybridRecommender(engineered_df)
    return recommender, engineered_df

try:
    recommender, dataset_df = init_recommender_system()
except Exception as e:
    st.error(f"❌ Gagal memuat database skincare: {e}")
    st.stop()

# 3. Header Halaman Utama (Tema Neobrutalisme)
st.markdown("""
    <div class="neo-card" style="background:#FFFDF0; margin-bottom:25px;">
        <h1 style="margin:0; font-weight:900; font-size:2.2rem; color:#000;">🎯 GlowPlan AI Engine</h1>
        <p style="margin:8px 0 0 0; font-size:1.1rem; color:#333; font-weight:500;">
            Dapatkan rekomendasi produk skincare yang dipetakan secara matematis menggunakan kecocokan bahan aktif 
            berbasis pembobotan matriks TF-IDF dan aturan fungsional kondisi kulit Anda.
        </p>
    </div>
""", unsafe_allow_html=True)

# 4. Form Input Parameter di Panel Utama
st.markdown("<h3 style='font-weight:800; color:#000; margin-bottom:10px;'>🛠️ Set Your Skin Preference</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    skin_cond = st.selectbox(
        "✨ Pilih Kondisi Utama Kulit Anda:",
        options=["Dry Skin", "Oily Skin", "Acne-Prone Skin", "Sensitive Skin"]
    )
    
    unique_types = sorted(dataset_df['product_type'].unique().tolist())
    prod_type = st.selectbox(
        "🧪 Pilih Kategori Produk Skincare:",
        options=unique_types
    )

with col2:
    max_budget = st.slider(
        "💰 Batas Finansial Maksimal (£):",
        min_value=1.0,
        max_value=150.0,
        value=50.0,
        step=0.5,
        help="Sistem cerdas akan menyaring produk yang harganya di bawah batas maksimal ini."
    )
    
    top_n = st.slider(
        "📊 Jumlah Rekomendasi yang Ditampilkan:",
        min_value=1,
        max_value=10,
        value=3,
        step=1
    )

st.markdown("<br>", unsafe_allow_html=True)

# 5. Blok Eksekusi Tombol Rekomendasi & Output Visual Rapi
if st.button("🎯 Generate Recommendation"):
    with st.spinner("Processing chemical similarity vectors via TF-IDF..."):
        recs_df = recommender.generate_recommendations(skin_cond, prod_type, max_budget, top_n)
        
        if recs_df.empty:
            st.markdown(f"""
                <div style="background:#FFCCD2; border: 3px solid #000; padding:15px; border-radius:8px; color:#000; font-weight:700; box-shadow: 4px 4px 0px 0px #000;">
                    ⚠️ No Products Found: Tidak ditemukan produk dengan kombinasi preferensi tersebut. 
                    Coba naikkan batas maksimal budget Anda atau ubah kategori produk!
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("<br><h2 style='font-weight:800; color:#000;'>✨ Highly-Compatible Recommendations</h2>", unsafe_allow_html=True)
            
            for rank, (_, row) in enumerate(recs_df.iterrows(), 1):
                card_bg = "#FFE9EC" if rank == 1 else "#FFFDF0"
                medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else "✨"
                
                try:
                    ing_list = ast.literal_eval(row['clean_ingreds'])
                    displayed_ings = ", ".join(ing_list[:7]) + "..." if len(ing_list) > 7 else ", ".join(ing_list)
                except:
                    displayed_ings = str(row['clean_ingreds'])

                # Bloks 1: Bagian Atas Kartu (Nama Produk & Skor) beserta Lencana Atribut (Pills)
                st.markdown(f"""
                <div style="background: {card_bg}; border: 3px solid #000000; border-radius: 12px; padding: 22px; box-shadow: 5px 5px 0px 0px #000000; margin-bottom: 5px; color:#000;">
                    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; border-bottom:2px solid #000; padding-bottom:8px; margin-bottom:12px;">
                        <h3 style="margin:0; font-weight:800; color:#000;">{medal} Recommendation #{rank}: {row['product_name']}</h3>
                        <span style="background:#000; color:#fff; padding:4px 12px; border-radius:6px; font-weight:800;">Score: {row['final_score']}%</span>
                    </div>
                    <div style="margin-bottom:15px; display: flex; gap: 8px; flex-wrap: wrap;">
                        <span style="background:#E2F0D9; border:2px solid #000; padding:3px 8px; border-radius:5px; font-weight:700; font-size:0.85rem; color:#000;">💰 Price: {row['price']}</span>
                        <span style="background:#FCE4D6; border:2px solid #000; padding:3px 8px; border-radius:5px; font-weight:700; font-size:0.85rem; color:#000;">🏷️ Type: {row['product_type']}</span>
                        <span style="background:#FFF2CC; border:2px solid #000; padding:3px 8px; border-radius:5px; font-weight:700; font-size:0.85rem; color:#000;">📈 Similarity: {row['similarity_score']}</span>
                        <span style="background:#E1F5FE; border:2px solid #000; padding:3px 8px; border-radius:5px; font-weight:700; font-size:0.85rem; color:#000;">⭐ Skin Match: {row['skin_match_score']}%</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Bloks 2: Kotak Putih Penjelasan "Why We Recommend This"
                matched_text = ", ".join(row['matched_ingredients']) if row['matched_ingredients'] else 'Formulasi Dasar yang Aman'
                st.markdown(f"""
                <div style="background:#ffffff; border:3px solid #000; padding:15px; border-radius:8px; margin-top:-20px; margin-bottom:10px; font-size:0.95rem; color:#000; line-height: 1.5; box-shadow: 3px 3px 0px 0px #000;">
                    <strong>🌟 Why We Recommend This Product:</strong><br>
                    <span style="color: green; font-weight:bold;">✓</span> Mengandung bahan aktif ideal utama: <b>{matched_text}</b> yang sangat direkomendasikan untuk tipe kulit <b>{skin_cond}</b>.<br>
                    <span style="color: green; font-weight:bold;">✓</span> Akurasi kategori produk tepat 100% sesuai dengan preferensi pencarian kategori <b>{row['product_type']}</b> Anda.<br>
                    <span style="color: green; font-weight:bold;">✓</span> Lolos aturan finansial: Dijual dengan harga {row['price']}, di bawah ambang batas budget maksimal Anda (£{max_budget}).
                </div>
                """, unsafe_allow_html=True)

                # Bloks 3: Bahan Baku Komplit & Tombol Tautan Keluar
                st.markdown(f"""
                <div style="margin-bottom:30px; text-align:right;">
                    <div style="font-size:0.85rem; color:#444; margin-bottom:12px; text-align:left;">
                        <b>Full Material Formulation:</b> <i>{displayed_ings}</i>
                    </div>
                    <a href="{row['product_url']}" target="_blank" style="background:#000; color:#fff; text-decoration:none; padding:8px 16px; border-radius:6px; font-weight:800; display:inline-block; border:2px solid #000; font-size:0.9rem; box-shadow: 3px 3px 0px 0px #444;">🔗 View Product Link</a>
                </div>
                <hr style="border:1px dashed #000; margin-bottom:25px;">
                """, unsafe_allow_html=True)