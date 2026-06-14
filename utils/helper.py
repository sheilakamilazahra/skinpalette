import streamlit as st
import pandas as pd
import os

@st.cache_data
def load_raw_dataset():
    """Membaca file CSV dari jalur folder yang ditentukan"""
    paths = ["data/skincare_products_clean.csv", "skincare_products_clean.csv"]
    for p in paths:
        if os.path.exists(p):
            return pd.read_csv(p)
    return pd.DataFrame(columns=['product_name', 'product_url', 'product_type', 'clean_ingreds', 'price'])

def inject_neobrutalism_design():
    """Menyuntikkan CSS Kustom Bertema Soft Neobrutalism Premium Startup"""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
        
        /* Global Canvas Background */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
            background-color: #F0F8FF !important; /* Bright Sky Blue */
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }
        
        /* Sidebar Styling */
        [data-testid="stSidebar"], [data-testid="stSidebarNav"] {
            background-color: #FFFDF0 !important; /* Butter Cream Cream */
            border-right: 3px solid #000000 !important;
        }
        
        /* Neobrutalist Base Card Component */
        .neo-box {
            background: #FFFDF0 !important; 
            border: 3px solid #000000 !important;
            border-radius: 12px !important;
            padding: 24px !important;
            box-shadow: 6px 6px 0px 0px #000000 !important;
            margin-bottom: 25px !important;
            color: #000000 !important;
        }
        
        /* Neobrutalist Premium Highlight Card */
        .neo-box-pink {
            background: #FFE9EC !important; /* Soft Pastel Pink / Peach */
            border: 3px solid #000000 !important;
            border-radius: 12px !important;
            padding: 24px !important;
            box-shadow: 6px 6px 0px 0px #000000 !important;
            margin-bottom: 25px !important;
            color: #000000 !important;
        }

        /* Typography Controls */
        .brand-title {
            font-size: 2.6rem !important;
            font-weight: 800 !important;
            color: #000000 !important;
            line-height: 1.2 !important;
        }
        
        .brand-tagline {
            font-size: 1.2rem !important;
            font-weight: 600 !important;
            color: #000000 !important;
            background-color: #FFF9D6;
            display: inline-block;
            padding: 6px 14px;
            border: 2px solid #000000;
            box-shadow: 3px 3px 0px #000000;
            margin-bottom: 20px;
        }

        /* Global Streamlit Buttons Override */
        .stButton > button {
            background: #FFF9D6 !important;
            color: #000000 !important;
            border: 3px solid #000000 !important;
            border-radius: 8px !important;
            padding: 12px 24px !important;
            font-weight: 800 !important;
            font-size: 1.1rem !important;
            box-shadow: 4px 4px 0px 0px #000000 !important;
            transition: transform 0.1s ease, box-shadow 0.1s ease !important;
            width: 100%;
        }
        
        .stButton > button:hover {
            transform: translate(2px, 2px) !important;
            box-shadow: 2px 2px 0px 0px #000000 !important;
            background: #FFE9EC !important;
            border-color: #000000 !important;
        }
        
        /* Badges Component */
        .neo-pill {
            background: #E6F2FF;
            border: 2px solid #000000;
            border-radius: 6px;
            padding: 4px 12px;
            font-weight: 600;
            display: inline-block;
            margin-right: 8px;
            margin-bottom: 8px;
            color: #000000;
        }
        
        /* Floating Cloud Banner Decorative */
        .cloud-banner {
            background: #E6F2FF;
            border: 2px dashed #000000;
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 25px;
            text-align: center;
            font-weight: 600;
            color: #000000;
        }
        </style>
    """, unsafe_allow_html=True)