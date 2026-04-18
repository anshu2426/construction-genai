from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

vectorizer = TfidfVectorizer()

def build_vector_db(texts):
    tfidf_matrix = vectorizer.fit_transform(texts)
    return tfidf_matrix

def search_vector_db(query, texts, tfidf_matrix, top_k=2):
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = similarities.argsort()[-top_k:][::-1]
    return [texts[i] for i in top_indices]
