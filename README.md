# Enterprise Hybrid Retrieval System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Deployment: Render/Railway](https://img.shields.io/badge/Deployment-Live-green.svg)](https://render.com)

## 📋 Overview
The **Enterprise Hybrid Retrieval System** is a production-oriented internal knowledge intelligence platform. It is designed to provide citation-grounded answers from enterprise documentation by leveraging **hybrid search** (dense + lexical) and **cross-encoder reranking**.

This system simulates a real-world enterprise infrastructure where reliability, precision, and evaluation safeguards are mission-critical.

---

## 🏗️ Architecture
The system implements a modern enterprise retrieval pipeline to ensure high-fidelity responses and minimize hallucinations.



### Core Components
* **FastAPI Backend:** Orchestration layer for retrieval, ranking, and generation.
* **PostgreSQL with pgvector:** A unified database solution for both dense vector embeddings and lexical full-text indexing.
* **Cross-Encoder Reranker:** A precision-focused layer that re-scores top candidates to filter out noise.
* **Evaluation Module:** Tracks retrieval quality (NDCG, Hit Rate) and integrates with CI/CD.
* **GitHub Actions:** Automates regression checks to ensure indexing updates don't degrade performance.

---

## 🎯 Business Problem
Enterprises maintain massive volumes of internal documentation (SOPs, HR policies, Engineering docs, Compliance manuals). Traditional search methods often fall short:

* **Keyword Search:** Struggles with semantic understanding (e.g., missing "parental leave" when searching "family benefits").
* **Naive Vector Search:** May miss critical exact-match technical terms or specific document IDs.
* **General Risks:** Inaccurate retrieval, hallucinated responses, and a lack of clear citation tracking.

### Why Hybrid Retrieval?
1.  **Semantic + Lexical:** Combines the "meaning" of a query with "exact keyword" matches.
2.  **Precision:** Cross-encoder reranking improves the final answer quality significantly compared to base retrieval.
3.  **Reliability:** Mirrors modern enterprise RAG architectures used in production environments.

---

## ✨ Key Features
* **Hybrid Scoring:** Configurable weights between semantic and lexical results.
* **Citation Enforcement:** Strict grounding to ensure every claim points back to a source chunk.
* **Modular Ingestion:** Clean pipeline for document processing and chunking.
* **Dockerized:** Ready for containerized deployment (Local/Cloud).
* **Evaluation Integration:** Built-in metrics for continuous quality monitoring.

---

## 🛠️ Tech Stack
| Category | Technology |
| :--- | :--- |
| **Language** | Python |
| **Framework** | FastAPI |
| **Database** | PostgreSQL + `pgvector` |
| **Embeddings** | SentenceTransformers |
| **LLM Provider** | OpenAI API (or custom provider) |
| **Infrastructure** | Docker, GitHub Actions |
| **Deployment** | Render / Railway / Supabase |

---

## 🔧 Future Improvements
* **RBAC:** Role-based document access control for sensitive HR/Legal files.
* **Multi-tenancy:** Isolated indexing for different departments or clients.
* **Observability:** Monitoring for retrieval "drift" and latency optimization.
* **Caching:** Intelligent query caching to reduce LLM costs.

---

## 📦 Deployment
* **Backend API:** Render / Railway
* **Database:** Supabase (Postgres + `pgvector`)
* **Frontend:** Vercel (Next.js)

---

## 🗓️ Project Board & Milestones

### Milestone 1 (Week 1)
- [x] FastAPI skeleton + deployed
- [x] Supabase schema created
- [x] Ingestion v1: chunk + store
- [x] Vector search v1 working

### Milestone 2 (Week 2)
- [ ] Full-text search + hybrid scoring
- [ ] Hybrid retrieval endpoint

### Milestone 3 (Week 3)
- [ ] Cross-encoder reranker
- [ ] Citation enforcement

### Milestone 4 (Week 4)
- [ ] Evaluation + CI gate
- [ ] Deployment polish + demo
---

## 📦 Deployment
* **Backend API:** Render / Railway
* **Database:** Supabase (Postgres + `pgvector`)
* **Frontend:** Vercel (Next.js)
