import pandas as pd
import numpy as np

def run_data_preprocessing(df):
    """
    Pipeline Tahap 1: Membersihkan dataset dari duplikasi, missing values,
    dan memformat data string finansial ke numerik float.
    """
    # Proteksi: Hapus data yang tidak memiliki value esensial
    df = df.dropna(subset=['product_name', 'clean_ingreds', 'product_type']).copy()
    
    # Normalisasi format teks kategori produk
    df['product_type'] = df['product_type'].str.strip().str.title()
    
    # Standarisasi kolom harga (Cleansing Simbol £, $ atau koma)
    if 'price' in df.columns:
        if df['price'].dtype == object:
            df['numeric_price'] = (
                df['price']
                .str.replace('£', '', regex=False)
                .str.replace('$', '', regex=False)
                .str.replace(',', '', regex=False)
                .str.strip()
            )
            df['numeric_price'] = pd.to_numeric(df['numeric_price'], errors='coerce')
        else:
            df['numeric_price'] = df['price'].astype(float)
            
        # Imputasi: Ganti data harga kosong dengan Median harga dari jenis produk sejenis
        df['numeric_price'] = df.groupby('product_type')['numeric_price'].transform(
            lambda x: x.fillna(x.median() if not x.dropna().empty else 12.0)
        )
    else:
        df['numeric_price'] = 15.0
        df['price'] = '£15.00'
        
    # Hapus duplikat nama produk agar hasil rekomendasi bervariasi dan kaya
    df = df.drop_duplicates(subset=['product_name']).reset_index(drop=True)
    
    return df