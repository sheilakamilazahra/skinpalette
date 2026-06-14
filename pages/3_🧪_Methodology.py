import streamlit as st
from models.evaluation import calculate_system_metrics
from utils.helper import inject_neobrutalism_design

inject_neobrutalism_design()

st.markdown("<h1 style='font-weight: 800; color:#000;'>🧪 System Architecture & Evaluation</h1>", unsafe_allow_html=True)
st.markdown("<span class='brand-tagline'>Documentation of system metrics algorithms and deployment validations.</span>", unsafe_allow_html=True)

# TAMPILAN FLOWCHART ARCHITECTURE DENGAN BLOK CSS NEOBRUTALISM
st.markdown("""
    <div class='neo-box'>
        <h4 style='margin-top:0; color:#000;'>📌 End-to-End Core System Architecture Flowchart</h4>
        <div style='display: flex; flex-direction: column; align-items: center; gap: 8px; font-weight: 800; margin: 20px 0; color:#000;'>
            <div style='background:#fff; border:2px solid #000; padding:8px 16px; border-radius:6px;'>Raw Dataset (skincare_products_clean.csv)</div>
            <div>↓</div>
            <div style='background:#FFFDF0; border:2px solid #000; padding:8px 16px; border-radius:6px;'>Data Preprocessing (Handling Price Symbol & Missing Val)</div>
            <div>↓</div>
            <div style='background:#FFF9D6; border:2px solid #000; padding:8px 16px; border-radius:6px;'>Feature Engineering (Ingredient Tokenization)</div>
            <div>↓</div>
            <div style='background:#FFE9EC; border:2px solid #000; padding:8px 16px; border-radius:6px;'>Knowledge-Based Sifting Rule Matrix</div>
            <div>↓</div>
            <div style='background:#E6F2FF; border:2px solid #000; padding:8px 16px; border-radius:6px;'>Vektor Space Model TF-IDF Extract</div>
            <div>↓</div>
            <div style='background:#fff; border:2px solid #000; padding:8px 16px; border-radius:6px;'>Mathematical Hybrid Scoring Formula Execution</div>
            <div>↓</div>
            <div style='background:#000; color:#fff; padding:8px 16px; border-radius:6px;'>Top-N Explainable Recommendation Output UI</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# EVALUATION SYSTEM INTEGRATION
st.markdown("<h3 style='font-weight: 800;'>📊 Automated Evaluation Metrics Validation</h3>", unsafe_allow_html=True)

if 'recommender' in st.session_state:
    skins_test = ["Dry Skin", "Oily Skin", "Acne-Prone Skin", "Sensitive Skin"]
    types_test = st.session_state.recommender.df['product_type'].dropna().unique().tolist()[:4]
    
    # Hitung metrik evaluasi kuantitatif secara otomatis
    eval_res = calculate_system_metrics(st.session_state.recommender, skins_test, types_test)
    
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    with col_m1:
        st.markdown(f"<div class='neo-box'><small>🎯 PRECISION@5</small><h2 style='margin:0; font-weight:800;'>{eval_res['precision']}%</h2></div>", unsafe_allow_html=True)
    with col_m2:
        st.markdown(f"<div class='neo-box'><small>📈 RECALL@5</small><h2 style='margin:0; font-weight:800;'>{eval_res['recall']}%</h2></div>", unsafe_allow_html=True)
    with col_m3:
        st.markdown(f"<div class='neo-box'><small>⚖️ F1-SCORE</small><h2 style='margin:0; font-weight:800;'>{eval_res['f1_score']}%</h2></div>", unsafe_allow_html=True)
    with col_m4:
        st.markdown(f"<div class='neo-box'><small>🌐 GLOBAL COVERAGE</small><h2 style='margin:0; font-weight:800;'>{eval_res['coverage']}%</h2></div>", unsafe_allow_html=True)

st.markdown("""
    <div class='neo-box-pink'>
        <h4 style='margin-top:0;'>📖 Mathematical Matrix Weighing Formula Detail</h4>
        <p>Sistem kalkulasi bobot linear gabungan yang dijalankan menggunakan formula interaksi:</p>
        <div style='background:#ffffff; border:2px solid #000; padding:12px; border-radius:8px; font-family:monospace; margin-bottom:12px; font-weight:bold; color:#000;'>
            Final Score = (SkinMatch * 0.50) + (ProductTypeMatch * 0.20) + (BudgetMatch * 0.10) + (CosineSimilarity * 0.20)
        </div>
        <ul>
            <li><b>Skin Match Score (50%):</b> Mengukur proporsi kemunculan bahan aktif krusial yang terkandung dalam basis knowledge ideal.</li>
            <li><b>Cosine Similarity (20%):</b> Mengukur kedekatan kemiripan semantik antar-vektor teks fitur kosmetik hasil pembobotan TF-IDF.</li>
            <li><b>Product Type & Budget (30%):</b> Menjamin akurasi kecocokan jenis kategori serta batas toleransi finansial finansial konsumen.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)