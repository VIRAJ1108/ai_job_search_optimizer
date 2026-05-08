from sklearn.metrics.pairwise import cosine_similarity

from backend.embeddings.embedding_model import model

def compute_similarity(text1: str, text2: str) -> float:
    """
    Compute semantic similarity between two texts
    """

    embeddings = model.encode([text1, text2])

    similarity_score = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return round(float(similarity_score * 100), 2)