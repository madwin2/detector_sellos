from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "status": "ok", 
        "message": "Detector de Sellos API - Vercel",
        "endpoints": {
            "health": "/api/health",
            "predict": "/api/predict"
        }
    }

def handler(request):
    return root()