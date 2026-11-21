# RAG Basics

**A hands-on journey into Retrieval-Augmented Generation (RAG) using Python.**

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Learning](https://img.shields.io/badge/Learning-RAG-brightgreen)](https://codesignal.com/learn/courses/introduction-to-rag)
[![Course](https://img.shields.io/badge/Platform-CodeSignal-orange)](https://codesignal.com/learn/courses/introduction-to-rag)
[![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)]()

## Overview

This repository documents my journey of learning and implementing **Retrieval-Augmented Generation (RAG)** through practical exercises, experiments, and independent Python implementations.

The learning path follows CodeSignal's [Introduction to RAG](https://codesignal.com/learn/courses/introduction-to-rag) course.

Rather than simply completing course exercises, the objective is to understand the underlying concepts, explore how individual components work, experiment with different approaches, and build reusable implementations.

This repository will evolve alongside my learning journey.

## What is RAG?

Retrieval-Augmented Generation (RAG) is an approach that combines information retrieval with Large Language Models (LLMs).

Instead of relying exclusively on the knowledge encoded in an LLM, a RAG system retrieves relevant information from an external knowledge source and provides that information as context when generating a response.

### Basic RAG Architecture

```text
             KNOWLEDGE BASE
                   |
                   v
             Document Loading
                   |
                   v
              Text Chunking
                   |
                   v
             Embedding Model
                   |
                   v
              Vector Storage
                   |
                   |
USER QUESTION     |
      |           |
      v           |
 Query Embedding  |
      |           |
      v           |
  Similarity Search
      |
      v
 Retrieved Context
      |
      v
 Prompt Augmentation
      |
      v
      LLM
      |
      v
 Generated Answer
```

*This is the conceptual architecture we will explore. Individual implementations may use simplified approaches.*

## Learning Objectives

The primary objectives of this repository are:

- Understand the fundamentals of Retrieval-Augmented Generation.
- Understand traditional Information Retrieval and its limitations.
- Explore how LLMs interact with external knowledge sources.
- Learn document ingestion and text preprocessing.
- Understand text chunking strategies.
- Explore text representation and embeddings.
- Understand vector representations and similarity search.
- Implement document retrieval mechanisms.
- Learn how retrieved information is incorporated into prompts.
- Understand the complete RAG workflow.
- Experiment with different retrieval strategies and evaluate their results.

## Learning Roadmap

The repository is organized around course units and practical lessons.

### Unit 01 – Introduction to RAG

Focus: Understanding RAG fundamentals and implementing a simple RAG workflow.

Topics:
- Information Retrieval (IR)
- Introduction to RAG
- Traditional retrieval approaches
- Knowledge bases
- Document retrieval
- Prompt augmentation
- Context-aware generation

### Unit 02 – Text Representation

Focus: Understanding how text is represented for retrieval.

Planned areas of exploration:
- Text preprocessing
- Text representation techniques
- Numerical representations
- Embeddings
- Semantic similarity

### Unit 03 – Retrieval and Search

Focus: Understanding how relevant information is retrieved.

Planned areas of exploration:
- Search strategies
- Similarity measures
- Vector search
- Retrieval techniques
- Ranking relevant documents

*Future units and topics will be updated according to the actual course curriculum and additional experiments.*

## Repository Structure

```text
rag-basics/
│
├── README.md
│
├── unit-01-introduction-to-rag/
│   │
│   ├── lesson-01-rag-fundamentals/
│   │
│   └── lesson-02-rag-in-action/
│       ├── README.md
│       ├── notes.md
│       ├── main.py
│       ├── main.sh
│       │
│       └── src/
│           ├── data/
│           ├── scripts/
│           │   └── llm.py
│           │
│           └── vector_db/
│               ├── __init__.py
│               └── handler.py
│
├── unit-02-text-representation/
│
├── unit-03-retrieval/
│
├── experiments/
│
├── resources/
│
└── .gitignore
```

Each practical lesson will have its own documentation and implementation.

## Learning Methodology

Every lesson will follow a consistent learning process.

| Phase | Activities |
|---|---|
| Learn | Complete the corresponding CodeSignal lesson. |
| Understand | Analyze concepts, algorithms, and implementation details. |
| Implement | Write independent Python implementations. |
| Experiment | Test different inputs, parameters, and approaches. |
| Document | Record findings, architecture, and observations. |
| Review | Test the implementation and review the concepts. |

## Technology Stack

The initial learning environment focuses on:

| Technology | Purpose |
|---|---|
| Python | Core implementation language |
| NumPy | Numerical computing and vector operations |
| Jupyter Notebook | Interactive experiments, where useful |
| Git | Version control |
| GitHub | Source code and portfolio documentation |

Additional libraries and technologies will be introduced as required by the course and practical experiments.

## Development Philosophy

This project follows a few important principles:

1. Understand the fundamentals before using high-level frameworks.
2. Prefer practical implementation over passive learning.
3. Understand what happens internally rather than treating libraries as black boxes.
4. Keep experiments reproducible and documented.
5. Write modular, readable, and testable Python code.
6. Maintain a Git history that reflects actual learning progress.

## Progress Tracker

- [ ] Introduction to RAG
- [ ] RAG fundamentals and Information Retrieval
- [ ] Simple RAG workflow
- [ ] Text representation
- [ ] Embeddings
- [ ] Vector representations
- [ ] Similarity search
- [ ] Document retrieval
- [ ] Prompt augmentation
- [ ] End-to-end RAG implementation
- [ ] Experiments and evaluation

Progress will be updated as individual lessons and implementations are completed.

## Resources

**Primary learning resource**

- [CodeSignal – Introduction to RAG](https://codesignal.com/learn/courses/introduction-to-rag)

Additional documentation, research papers, tutorials, and references will be collected here as the project progresses.

## Project Status

**Currently learning:** Introduction to RAG

**Current focus:** RAG in Action – A Simple Workflow

This repository is a continuous learning project. Implementations, experiments, and documentation will be added incrementally.

## Author

**Bhanu Pratap Khuntia**

GitHub: [@BhanuPy](https://github.com/BhanuPy)

---

*Learning by understanding, implementing, experimenting, and building.*