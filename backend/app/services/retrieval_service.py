from app.services.vector_store import collection


def retrieve_chunks(query_embedding, n_results=3):

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results