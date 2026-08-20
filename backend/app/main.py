from fastapi import FastAPI

app = FastAPI(
    title="UrjaShield API",
    description="AI-powered energy supply chain resilience platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "name": "UrjaShield",
        "status": "online",
        "version": "0.1.0",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }