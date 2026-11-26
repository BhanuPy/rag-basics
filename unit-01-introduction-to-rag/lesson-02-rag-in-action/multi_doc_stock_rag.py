from scripts.llm import get_llm_response

# Simulated knowledge base containing historical stock data
KNOWLEDGE_BASE = {
    "AAPL": {
        "title": "AAPL Stock (April 2023)",
        "content": (
            "On 2023-04-13, AAPL opened at $160.50, closed at $162.30, with a high of $163.00 and a low of $159.90. "
            "Trading volume was 80 million shares. "
            "On 2023-04-14, AAPL opened at $161.10, closed at $162.80, with a high of $163.50 and a low of $160.50. "
            "Trading volume was 85 million shares."
        )
    },
    "MSFT": {
        "title": "MSFT Stock (April 2023)",
        "content": (
            "On 2023-04-13, MSFT opened at $285.00, closed at $288.50, with a high of $290.00 and a low of $283.50. "
            "Trading volume was 35 million shares. "
            "On 2023-04-14, MSFT opened at $286.00, closed at $289.00, with a high of $291.50 and a low of $284.70. "
            "Trading volume was 40 million shares."
        )
    },
    "TSLA": {
        "title": "TSLA Stock (April 2023)",
        "content": (
            "On 2023-04-13, TSLA opened at $185.00, closed at $187.00, with a high of $189.00 and a low of $184.50. "
            "Trading volume was 50 million shares. "
            "On 2023-04-14, TSLA opened at $186.00, closed at $188.50, with a high of $190.00 and a low of $185.50. "
            "Trading volume was 55 million shares."
        )
    }
}


def naive_generation(query):
    """Directly asks the LLM without external grounding (prone to hallucinations)."""
    prompt = f"Answer directly the following query: {query}"
    return get_llm_response(prompt)


def rag_retrieval(query, knowledge_base):
    """Retrieves and ranks relevant documents based on keyword overlap with the query."""
    # Extract lowercase words from the query for matching
    query_words = set(query.lower().split())
    scores = []
    
    # Calculate word overlap score for each document
    for doc_id, doc in knowledge_base.items():
        doc_words = set(doc["content"].lower().split())
        overlap = len(query_words.intersection(doc_words))
        
        # Keep documents that match query keywords
        if overlap > 0:
            scores.append((doc_id, overlap))
        
    # Sort documents by relevance (highest overlap first)
    scores.sort(key=lambda x: x[1], reverse=True)
    # Return the documents in ranked order
    return [knowledge_base[doc_id] for doc_id, _ in scores]    


def rag_generation(query, documents):
    """Grounds the LLM response using the retrieved context snippets."""
    if documents:
        snippets = " ".join([f"{doc['title']}: {doc['content']}" for doc in documents])
        prompt = f"Using the following information: '{snippets}', answer: {query}"
    else:
        prompt = f"No relevant information found. Answer directly: {query}"
    return get_llm_response(prompt)


if __name__ == "__main__":
    query = (
        "Write a short summary of the stock market performance on April 14, "
        "2023 for the following symbols: AAPL, MSFT, TSLA.\n"
        "Your summary should include:\n"
        "For each symbol:\n"
        "- The opening price\n"
        "- The closing price\n"
        "- The highest and lowest prices of the day\n"
        "- The trading volume"
    )
    # Naive approach hallucinates (generates plausible, but fabricated data)
    print("Naive approach:\n", naive_generation(query))
    
    # RAG approach grounds the response with factual knowledge base documents
    retrieved_docs = rag_retrieval(query, KNOWLEDGE_BASE)
    print("\n\nRAG approach:\n", rag_generation(query, retrieved_docs))