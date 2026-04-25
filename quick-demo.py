from fastapi import FastAPI, Path
from enum import Enum
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


# With FastAPI, you don't need to use a "if __name__ == 'main'" block.
app = FastAPI()

# FastAPI handles the server externally using ASGI - Asynchronous Server Gateway Interface.
# Unlike Flask, which uses WSGI - Web Server Gateway Interface (Not Asynchronous)


# "/" is the index route.
@app.get("/")
async def read_root():
    return {"Hello": "World"}


# Dynamic URLs - Param Functions like Path are great.
# Try using a regex pattern for finer control.
pattern = r"^[a-zA-Z0-9]+$"


@app.get("/items/{item_id}")
async def read_item(item_id: str = Path(..., pattern=pattern), q: Optional[str] = None):
    # Returns {item_id	"<item_id>"}
    if q:
        return {"item_id": item_id, "q": q}
    # This just returns whatever param we pass in i.e. 4, 5, etc.
    # Example URL: http://127.0.0.1:8000/items/4

    return {"item_id": item_id}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    return item_dict

