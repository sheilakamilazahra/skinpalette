import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from config.skin_mapping import SKIN_MAPPING

class SkincareHybridRecommender:
    def __init__(self, processed_df):
        """Menerima dataframe yang telah melewati Preprocessing & Feature Engineering"""
        self.df = processed_df
        self._build_vector_space_model()

    def _build_vector_space_model(self):
        # Inisialisasi model TF-IDF Vectorizer pada fitur korpus hasil engineering
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.tfidf.fit_transform(self.df['tfidf_features'])

    def generate_recommendations(self, skin_cond, prod_type, max_budget, top_n=5):
        # 1. KNOWLEDGE-BASED FILTERING (Hard filtering kecocokan kategori tipe produk)
        filtered_df = self.df[self.df['product_type'].str.lower() == prod_type.lower()].copy()
        
        if filtered_df.empty:
            return pd.DataFrame()

        # Ambil daftar bahan aktif ideal dari knowledge base dictionary
        target_ingredients = SKIN_MAPPING.get(skin_cond, [])
        results = []
        
        for idx, row in filtered_df.iterrows():
            # Perhitungan interaksi formula: Skin Match Score
            ingreds_list_str = row['clean_ingreds'].lower()
            matched_ingreds = [ing for ing in target_ingredients if ing in ingreds_list_str]
            
            skin_match_score = (len(matched_ingreds) / len(target_ingredients)) if target_ingredients else 0.0
            
            # Filter Aturan Finansial: Budget Match Score
            budget_match = 1.0 if row['numeric_price'] <= max_budget else 0.0
            prod_match = 1.0  # Bernilai 1 karena sudah lolos hard filtering kategori di awal
            
            # 2. CONTENT-BASED FILTERING (Mengukur Kedekatan Vektor Cosine Similarity)
            profile_str = " ".join([ing.replace(" ", "_") for ing in target_ingredients])
            profile_vector = self.tfidf.transform([profile_str])
            
            # Ambil index matriks TF-IDF produk dari dataset utama
            prod_vector = self.tfidf_matrix[idx]
            cos_sim = cosine_similarity(profile_vector, prod_vector)[0][0]
            
            # IMPLEMENTASI FORMULA SCORING TERBOBOT (Sesuai instruksi master prompt):
            # Skin Match: 50%, Product Type Match: 20%, Budget Match: 10%, Cosine Similarity: 20%
            final_score = (
                (skin_match_score * 0.50) + 
                (prod_match * 0.20) + 
                (budget_match * 0.10) + 
                (cos_sim * 0.20)
            ) * 100.0
            
            results.append({
                'product_name': row['product_name'],
                'product_url': row['product_url'],
                'product_type': row['product_type'],
                'clean_ingreds': row['clean_ingreds'],
                'price': row['price'],
                'numeric_price': row['numeric_price'],
                'skin_match_score': round(skin_match_score * 100, 1),
                'similarity_score': round(cos_sim, 2),
                'budget_match': budget_match,
                'final_score': round(final_score, 1),
                'matched_ingredients': matched_ingreds
            })
            
        res_df = pd.DataFrame(results)
        
        # Pengurutan prioritas: Patuh budget (budget_match) dulu, dilanjutkan ke Skor Final Tertinggi
        res_df = res_df.sort_values(by=['budget_match', 'final_score'], ascending=[False, False])
        
        return res_df.head(top_n)