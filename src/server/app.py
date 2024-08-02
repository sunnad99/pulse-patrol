import uvicorn
from fastapi import FastAPI

from customer.api import router as customer_router

app = FastAPI()

app.include_router(customer_router, prefix="/api/v1")


@app.get("/")
def health():
    return {"message": "Welcome to gym management system"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
