from fastapi import FastAPI

app = FastAPI(title="Jobboard", varion="0.1.0")

@app.get("/")
def hello_api():
    return {"detail": "Hello World"}
    