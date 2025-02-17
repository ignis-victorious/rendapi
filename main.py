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
# IVA
class IvaPercentages(BaseModel):
    date: date  # datetime
    iva: list[int] = [0, 10, 22]


# ivas: list[IvaPercentages] = []
iva_pecentages: list[IvaPercentages] = [
    IvaPercentages(date=date(2024, 1, 1), iva=[0, 10, 22]),
    IvaPercentages(date=date(2025, 1, 1), iva=[0, 10, 22]),
]


# ACCISE
class AccisePercentages(BaseModel):
    date: date  # datetime
    accise: list[int] = [227, 125, 75]


# accise_percentages: list[AccisePercentages] = []
accise_percentage: list[AccisePercentages] = [
    AccisePercentages(date=date(2024, 1, 1), accise=[227, 125, 75]),
    AccisePercentages(date=date(2025, 1, 1), accise=[227, 125, 75]),
]

# print(IvaPercentages(date=date.today(), iva=[0, 10, 22]))
# print(AccisePercentages(date=date.today(), iva=[227, 125, 75]))


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
    iva_pecentages.append(iva)
    return iva


@app.get("/ee/ivas", response_model=list[IvaPercentages])
async def read_ivas() -> list[IvaPercentages]:
    return iva_pecentages


#  ACCISE
@app.post("/ee/accises", response_model=AccisePercentages)
async def add_accise(accise: AccisePercentages) -> AccisePercentages:
    accise.date = date.today()  # datetime.now()
    accise_percentages.append(accise)
    return accise


@app.get("/ee/accises", response_model=list[AccisePercentages])
async def read_accises() -> list[AccisePercentages]:
    return accise_percentages


#  ---  Gas  ---
@app.get("/gas/")
async def gas() -> dict[str, str]:
    return {"message": "You are inside GAS"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
