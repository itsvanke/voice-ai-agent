
from fastapi import FastAPI
from backend.routes.voice_routes import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def health():
    return {"status": "Voice AI Agent Running"}
