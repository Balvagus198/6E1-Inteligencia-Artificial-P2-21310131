# -*- coding: utf-8 -*-
"""
@author: Gustavo
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Corpus de documentos de ejemplo
corpus = [
    "Machine learning is the study of computer algorithms that improve automatically through experience.",
    "Natural language processing (NLP) is a subfield of artificial intelligence that focuses on the interaction between computers and humans using natural language.",
    "Deep learning is a subset of machine learning in artificial intelligence (AI) that has networks capable of learning unsupervised from data that is unstructured or unlabeled."
]

# Crear un vectorizador TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)

# Definir una consulta de ejemplo
query = "What is machine learning?"

# Transformar la consulta en un vector TF-IDF
query_vector = vectorizer.transform([query])

# Calcular la similitud coseno entre la consulta y los documentos del corpus
similarities = cosine_similarity(query_vector, tfidf_matrix)

# Obtener el índice del documento más relevante
most_similar_doc_index = similarities.argmax()

# Imprimir el documento más relevante
print("Documento más relevante:")
print(corpus[most_similar_doc_index])
