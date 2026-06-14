import ast

def run_feature_engineering(df):
    """
    Pipeline Tahap 2: Ekstraksi Fitur Tekstual. Mengubah representasi string list
    menjadi korpus kalimat ter-tokenisasi dengan penghubung underscore (contoh: 'tea_tree').
    """
    def flatten_ingredients_to_tokens(val):
        try:
            # Mengubah struktur teks string array kosmetik menjadi objek list asli python
            actual_list = ast.literal_eval(val)
            # Normalisasi spasi antar kata agar digabung dengan underscore
            processed_tokens = [ing.strip().lower().replace(" ", "_") for ing in actual_list]
            return " ".join(processed_tokens)
        except:
            # Fallback jika terjadi kegagalan pembacaan struktur teks data asli
            cleaned_str = str(val).lower().replace("[", "").replace("]", "").replace("'", "")
            return cleaned_str
            
    df['tfidf_features'] = df['clean_ingreds'].apply(flatten_ingredients_to_tokens)
    return df