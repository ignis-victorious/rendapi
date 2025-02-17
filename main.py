#  ##   ###
#  Import LIBRARIES
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date  # datetime
#  Import FILES
#  ##   ###
##  Website
# https://rendapi-ww38.onrender.com/

app = FastAPI()


#  CLASSES
class IvaPercentages(BaseModel):
    date: date  # datetime
    iva: list[int] = [0, 10, 22]


ivas: list[IvaPercentages] = []


#  FUNCTIONS


#  ---  Root  ---
@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "This is UDXI - Navigate freely through the website."}


#  ---  Electric Energy  ---
@app.get("/ee/")
async def ee() -> dict[str, str]:
    return {"message": "You are inside EE"}


# IVA
@app.post("/ee/ivas", response_model=IvaPercentages)
async def add_iva(iva: IvaPercentages) -> IvaPercentages:
    iva.date = date.today()  # datetime.now()
    ivas.append(iva)
    return iva


@app.get("/ee/ivas", response_model=list[IvaPercentages])
async def read_ivas() -> list[IvaPercentages]:
    return ivas


#  ---  Gas  ---
@app.get("/gas/")
async def gas() -> dict[str, str]:
    return {"message": "You are inside GAS"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
