from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="FitMe Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://fitme-tryon.vercel.app",
        "http://localhost:3000",
        "http://127.0.0.1:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "FitMe backend",
        "message": "Step 2 backend is live!",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
