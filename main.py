from fastapi import FastAPI

app = FastAPI(
    title="User Management IDaaS Platform"
)

@app.get("/")
def health():
    return {"status": "Welcome to User Management IDaaS Platform!"}