
---

### `notes.md`
```markdown
# Lesson Notes: RAG in Action

## Key Concepts
- **Naive Generation vs. RAG**: Naive prompting can lead to hallucinations when querying private or domain-specific data. RAG grounds the model's output in authoritative sources.
- **Pipeline Stages**:
  - **Indexing**: Structuring reference documents for lookup.
  - **Retrieval**: Identifying relevant context for a query.
  - **Augmentation**: Combining context and query into a targeted prompt.
  - **Generation**: Producing context-backed responses via an LLM.

## Limitations & Next Steps
- **Keyword Overlap**: Does not handle synonyms, context, or semantic similarity.
- **Future Improvements**: Using embeddings, vector databases, and document chunking for robust retrieval.