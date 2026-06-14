import streamlit as st
import plotly.express as px
import pandas as pd
from collections import Counter
import ast
from utils.helper import inject_neobrutalism_design

inject_neobrutalism_design()

st.markdown("<h1 style='font-weight: 800; color:#000;'>📊 Business Analytics Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<span class='brand-tagline'>High-level macro statistical analytics of corporate skincare products.</span>", unsafe_allow_html=True)

if 'recommender' not in st.session_state:
    st.error("Gagal memuat visualisasi data. Harap jalankan file app.py terlebih dahulu.")
else:
    df = st.session_state.recommender.df
    
    # Ekstraksi seluruh list bahan aktif secara global
    all_ings = []
    for _, row in df.iterrows():
        try:
            items = ast.literal_eval(row['clean_ingreds'])
            all_ings.extend([i.strip().lower() for i in items])
        except:
            pass
    unique_ing_count = len(set(all_ings))

    # TAMPILAN KPI METRIC CARDS NEOBRUTALISM
    col_k1, col_k2, col_k3, col_k4 = st.columns(4)
    with col_k1:
        st.markdown(f"<div class='neo-box' style='text-align:center; padding:15px;'><small>📦 TOTAL PRODUCTS</small><h2 style='margin:0; font-weight:800;'>{len(df)}</h2></div>", unsafe_allow_html=True)
    with col_k2:
        st.markdown(f"<div class='neo-box' style='text-align:center; padding:15px;'><small>🏷️ PRODUCT TYPES</small><h2 style='margin:0; font-weight:800;'>{df['product_type'].nunique()}</h2></div>", unsafe_allow_html=True)
    with col_k3:
        st.markdown(f"<div class='neo-box' style='text-align:center; padding:15px;'><small>🧪 UNIQUE INGREDS</small><h2 style='margin:0; font-weight:800;'>{unique_ing_count}</h2></div>", unsafe_allow_html=True)
    with col_k4:
        st.markdown(f"<div class='neo-box' style='text-align:center; padding:15px;'><small>💰 AVERAGE PRICE</small><h2 style='margin:0; font-weight:800;'>£{round(df['numeric_price'].mean(), 2)}</h2></div>", unsafe_allow_html=True)

    # BARIS GRAFIK 1
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.markdown("<div class='neo-box'><h4>Product Type Distribution</h4>", unsafe_allow_html=True)
        type_counts = df['product_type'].value_counts().reset_index()
        fig1 = px.pie(type_counts, values='count', names='product_type', color_discrete_sequence=px.colors.qualitative.Pastel)
        fig1.update_layout(margin=dict(t=15, b=15, l=15, r=15), height=280, paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig1, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_c2:
        st.markdown("<div class='neo-box'><h4>Price Distribution Histogram</h4>", unsafe_allow_html=True)
        fig2 = px.histogram(df, x='numeric_price', nbins=30, color_discrete_sequence=['#FFE9EC'])
        fig2.update_layout(margin=dict(t=15, b=15, l=15, r=15), height=280, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', showlegend=False)
        fig2.update_xaxes(showline=True, linewidth=2, linecolor='black', title_text='Price (£)')
        fig2.update_yaxes(showline=True, linewidth=2, linecolor='black')
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # BARIS GRAFIK 2
    col_c3, col_c4 = st.columns([3, 2])
    with col_c3:
        st.markdown("<div class='neo-box'><h4>Top 15 Most Frequent Skincare Ingredients</h4>", unsafe_allow_html=True)
        counts = Counter(all_ings)
        top_df = pd.DataFrame(counts.most_common(15), columns=['Ingredient', 'Count'])
        fig3 = px.bar(top_df, x='Count', y='Ingredient', orientation='h', color_discrete_sequence=['#FFF9D6'])
        fig3.update_layout(margin=dict(t=15, b=15, l=15, r=15), height=320, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', yaxis={'categoryorder':'total ascending'})
        fig3.update_xaxes(showline=True, linewidth=2, linecolor='black')
        fig3.update_yaxes(showline=True, linewidth=2, linecolor='black')
        st.plotly_chart(fig3, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_c4:
        st.markdown("<div class='neo-box'><h4>Average Price by Product Type</h4>", unsafe_allow_html=True)
        avg_p = df.groupby('product_type')['numeric_price'].mean().reset_index().sort_values(by='numeric_price', ascending=False)
        fig4 = px.bar(avg_p, x='product_type', y='numeric_price', color_discrete_sequence=['#E6F2FF'])
        fig4.update_layout(margin=dict(t=15, b=15, l=15, r=15), height=320, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        fig4.update_xaxes(showline=True, linewidth=2, linecolor='black', title_text='')
        fig4.update_yaxes(showline=True, linewidth=2, linecolor='black', title_text='Avg Price (£)')
        st.plotly_chart(fig4, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)