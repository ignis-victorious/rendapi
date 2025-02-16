#  ##   ###
#  Import LIBRARIES
from fastapi import FastAPI
#  Import FILES
#  ##   ###

app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> dict[str, str | None]:
    return {"item_id": item_id, "q": q}
