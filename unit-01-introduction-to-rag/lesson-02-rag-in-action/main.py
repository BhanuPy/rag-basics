from src.scripts.llm import get_llm_response

# In-memory knowledge base acting as our indexed document store
KNOWLEDGE_BASE = {
    "doc1": {
        "title": "Project Chimera Overview",
        "content": (
            "research initiative focused on developing novel bio-integrated "
            "interfaces, aiming at merging biological systems with advanced "
            "computing technologies."
        )
    },
    "doc2": {
        "title": "Chimera's Core Component",
        "content": (
            "a neural interface that allows for bidirectional communication "
            "between the brain and external devices, using biocompatible "
            "nanomaterials."
        )
    },
    "doc3": {
        "title": "Applications of Chimera",
        "content": (
            "advanced prosthetics, treatment of neurological disorders, "
            "enhanced human-computer interaction."
        )
    }
}


def naive_generation(query):
    """Generates an answer directly using the LLM without external context."""
    prompt = f"Answer directly the following query: {query}"
    return get_llm_response(prompt)


def rag_retrieval(query, documents):
    """Retrieves the most relevant document based on keyword overlap with title and content."""
    query_words = set(query.lower().split())
    best_doc_id = None
    best_score = 0
    
    for doc_id, doc in documents.items():
        # Combine words from both title and content for retrieval matching
        doc_words = set(doc["content"].lower().split() + doc["title"].lower().split())
        score = len(query_words.intersection(doc_words))
        
        # Track the document with the highest word overlap
        if score > best_score:
            best_score = score
            best_doc_id = doc_id
            
    return documents.get(best_doc_id)


def rag_generation(query, document):
    """Augments the query with retrieved context and generates a grounded response."""
    if document:
        snippet = f"{document['title']}: {document['content']}"
        prompt = f"Using the following information: '{snippet}', answer: {query}"
    else:
        prompt = f"No relevant information found. Answer directly: {query}"
    return get_llm_response(prompt)


if __name__ == "__main__":
    query = "What are the applications of Project Chimera?"
    
    # 1. Naive generation without retrieval context
    print("Naive approach:", naive_generation(query))
    
    # 2. RAG generation with context retrieval
    retrieved_doc = rag_retrieval(query, KNOWLEDGE_BASE)
    print("RAG approach:", rag_generation(query, retrieved_doc))