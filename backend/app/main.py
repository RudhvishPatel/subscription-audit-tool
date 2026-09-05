from fastapi import FastAPI

app = FastAPI()

def health():
  return {"status": "ok"}
