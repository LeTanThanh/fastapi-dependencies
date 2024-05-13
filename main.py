from fastapi import FastAPI
from fastapi import Depends

from typing import Annotated

app = FastAPI()

# Create a dependency, or "dependable"
async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
  return {"q": q, "skip": skip, "limit": limit}

@app.get("/items")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
  return commons

@app.get("/users")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
  return commons
