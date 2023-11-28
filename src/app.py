import fastapi
import uvicorn

app = fastapi.FastAPI()

@app.get("/")
def health_check():
    return {"health": "OK"}

if __name__ == "__main__":
    uvicorn.run("src.app:app", host="0.0.0.0", port=5000, reload=True)
