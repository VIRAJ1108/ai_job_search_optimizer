# from sklearn.metrics.pairwise import cosine_similarity

# from backend.embeddings.embedding_model import generate_embedding

# def compute_similarity(text1: str, text2: str) -> float:
#     """
#     Compute semantic similarity between two texts
#     """

#     embeddings = generate_embedding.encode([text1, text2])

#     similarity_score = cosine_similarity(
#         [embeddings[0]],
#         [embeddings[1]]
#     )[0][0]

#     return round(float(similarity_score * 100), 2)

from sklearn.metrics.pairwise import cosine_similarity
from backend.embeddings.embedding_model import generate_embedding

def compute_similarity(text1: str, text2: str) -> float:
    """
    Compute semantic similarity between two texts.
    Returns a percentage score between 0 and 100.
    """
    emb1 = generate_embedding(text1)
    emb2 = generate_embedding(text2)

    similarity_score = cosine_similarity([emb1], [emb2])[0][0]

    return round(float(similarity_score * 100), 2)