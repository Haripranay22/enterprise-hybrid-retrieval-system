from fastapi import FastAPI
app= FastAPI(title="Enterprise Hybrid Retrieval System")

@app.get("/health")
def health():
    return {"message": "Enterprise Hybrid Retrieval System API. Visit /docs"}