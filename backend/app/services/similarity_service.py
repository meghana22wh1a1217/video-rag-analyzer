from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def compare_embeddings(embeddings_a, embeddings_b):

    similarities = cosine_similarity(
        embeddings_a,
        embeddings_b
    )

    best_score = np.max(similarities)

    return float(best_score)