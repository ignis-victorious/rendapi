#  ##   ###
#  Import LIBRARIES
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date  # datetime
import locale
#  Import FILES
#  ##   ###
##  Website
# https://rendapi-ww38.onrender.com/

# use Italian settings
# locale.setlocale(
#     locale.LC_ALL, "it_IT.ISO8859-1"
# )  # using standard Language Code Identifier (LCID) Reference
# locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')
# locale.setlocale(locale.LC_ALL, 'ita_ita')  # using ISO country code, alpha-3
# locale.setlocale(locale.LC_ALL, 'ita_ITA')  # using ISO country code, alpha-3
# locale.setlocale(locale.LC_ALL , 'Italian')   # using language name
# use current setting
# locale.setlocale(locale.LC_ALL, None)
# for lang in locale.locale_alias.values():
#     print(lang)

app = FastAPI()


#  CLASSES
# IVA EE
class IvaEePercentages(BaseModel):
    date: date  # datetime
    iva: list[int]  # = [0, 10, 22]


# ivas: list[IvaPercentages] = []
iva_ee_pecentages: list[IvaEePercentages] = [
    IvaEePercentages(date=date(2024, 1, 1), iva=[0, 10, 22]),
    IvaEePercentages(date=date(2025, 1, 1), iva=[0, 10, 22]),
]


# ACCISE EE
class AcciseEePercentages(BaseModel):
    date: date  # datetime
    accise: list[int] = [227, 125, 75]


# accise_percentages: list[AccisePercentages] = []
accise_ee_percentages: list[AcciseEePercentages] = [
    AcciseEePercentages(date=date(2024, 1, 1), accise=[227, 125, 75]),
    AcciseEePercentages(date=date(2025, 1, 1), accise=[227, 125, 75]),
]


# IVA GAS
class IvaGasPercentages(BaseModel):
    date: date  # datetime
    scaglione: list[int] = [120, 480, 1560, 9999]
    accisa_nord: list[int] = [44, 175, 170, 186]


iva_gas_pecentages: list[IvaGasPercentages] = []
# iva_gas_pecentages: list[IvaGasPercentages] = [IvaGasPercentages(date=date(2024, 1, 1), iva=[0, 10, 22]), IvaGasPercentages(date=date(2025, 1, 1), iva=[0, 10, 22]),]


# ACCISE GAS CIVILE
class AcciseGasCivilePercentages(BaseModel):
    date: date  # datetime
    scaglione_civ: list[int]  # = [120, 480, 1560, 9999]
    accisa_nord: list[int]  # = [44, 175, 170, 186]
    accisa_mezz: list[int]  # = [38, 135, 120, 150]
    # accisa_sud: list[int] = [0, 0, 0, 0]


# accise_gas_civile_percentages: list[AcciseGasCivilePercentages] = []
accise_gas_civile_percentages: list[AcciseGasCivilePercentages] = [
    AcciseGasCivilePercentages(
        date=date(2024, 1, 1),
        scaglione_civ=[120, 480, 1560, 9999],
        accisa_nord=[44, 175, 170, 186],
        accisa_mezz=[38, 135, 120, 150],
    ),
    AcciseGasCivilePercentages(
        date=date(2025, 1, 1),
        scaglione_civ=[120, 480, 1560, 9999],
        accisa_nord=[44, 175, 170, 186],
        accisa_mezz=[38, 135, 120, 150],
    ),
]


# ACCISE GAS INDUSTRIALE
class AcciseGasIndustrialePercentages(BaseModel):
    date: date  # datetime
    scaglione_ind: list[int]  # [12, 9999]
    accisa_ind: list[int]  # [12498, 74988]


# accise_gas_industriale_percentages: list[AcciseGasIndustrialePercentages] = []
accise_gas_industriale_percentages: list[AcciseGasIndustrialePercentages] = [
    AcciseGasIndustrialePercentages(
        date=date(2024, 1, 1),
        scaglione_ind=[12, 9999],
        accisa_ind=[12498, 74988],
    ),
    AcciseGasIndustrialePercentages(
        date=date(2025, 1, 1),
        scaglione_ind=[12, 9999],
        accisa_ind=[12498, 74988],
    ),
]


# ADDIZIONALE REGIONALE CIVILE
class AddizionaleGasCivilePercentages(BaseModel):
    date: date  # datetime
    region: list[str]
    scaglione_civ: list[int]  # [120, 480, 1560, 9999]
    addizionale_120: list[int]  # >120m3,
    addizionale_480: list[int]  # 120-480 m3
    addizionale_1560: list[int]  # 480-1.560 m3
    addizionale_9999: list[int]  # > 1.560 m3


# addizionale_gas_civile_percentages: list[AddizionaleGasCivilePercentages] = []
addizionale_gas_civile_percentages: list[AddizionaleGasCivilePercentages] = [
    AddizionaleGasCivilePercentages(
        date=date(2024, 1, 1),
        region=[
            "Abruzzo",
            "Abruzzo (fascia e ed f)",
            "Basilicata",
            "Calabria",
            "Emilia-romagna",
            "Friuli v.g.",
            "Lazio",
            "Lazio (ex casmez)",
            "Liguria (fascia climatica e)",
            "Liguria (fascia climatica f)",
            "Liguria (fascia climatica c/d)",
            "Lombardia",
            "Molise",
            "Marche",
            "Puglia",
            "Piemonte",
            "Sardegna",
            "Sicilia",
            "Trentino aa.",
            "Toscana",
            "UmbriaV.d'aosta",
            "Veneto",
        ],
        scaglione_civ=[120, 480, 1560, 9999],
        addizionale_120=[
            19000,
            10330,
            19000,
            19000,
            22000,
            0,
            22000,
            19000,
            15500,
            10300,
            22000,
            0,
            19000,
            15500,
            19000,
            22000,
            0,
            0,
            0,
            0,
            5165,
            0,
            7747,
        ],
        addizionale_480=[
            23241,
            10330,
            25823,
            25820,
            30987,
            0,
            30990,
            30990,
            15500,
            10300,
            258000,
            0,
            30987,
            18100,
            30980,
            25800,
            0,
            0,
            0,
            30987,
            5165,
            0,
            23241,
        ],
        addizionale_1560=[
            25823,
            10330,
            25823,
            25820,
            30987,
            0,
            30990,
            30990,
            15500,
            10300,
            258000,
            0,
            30987,
            18100,
            30980,
            25800,
            0,
            0,
            0,
            30987,
            5165,
            0,
            25823,
        ],
        addizionale_9999=[
            25823,
            10330,
            25823,
            30990,
            30987,
            0,
            30990,
            30990,
            15500,
            10300,
            258000,
            0,
            30987,
            25800,
            30980,
            25800,
            0,
            0,
            0,
            30987,
            5165,
            0,
            30987,
        ],
    ),
    AddizionaleGasCivilePercentages(
        date=date(2025, 1, 1),
        region=[
            "Abruzzo",
            "Abruzzo (fascia e ed f)",
            "Basilicata",
            "Calabria",
            "Emilia-romagna",
            "Friuli v.g.",
            "Lazio",
            "Lazio (ex casmez)",
            "Liguria (fascia climatica e)",
            "Liguria (fascia climatica f)",
            "Liguria (fascia climatica c/d)",
            "Lombardia",
            "Molise",
            "Marche",
            "Puglia",
            "Piemonte",
            "Sardegna",
            "Sicilia",
            "Trentino aa.",
            "Toscana",
            "UmbriaV.d'aosta",
            "Veneto",
        ],
        scaglione_civ=[120, 480, 1560, 9999],
        addizionale_120=[
            19000,
            10330,
            19000,
            19000,
            22000,
            0,
            22000,
            19000,
            15500,
            10300,
            22000,
            0,
            19000,
            15500,
            19000,
            22000,
            0,
            0,
            0,
            0,
            5165,
            0,
            7747,
        ],
        addizionale_480=[
            23241,
            10330,
            25823,
            25820,
            30987,
            0,
            30990,
            30990,
            15500,
            10300,
            258000,
            0,
            30987,
            18100,
            30980,
            25800,
            0,
            0,
            0,
            30987,
            5165,
            0,
            23241,
        ],
        addizionale_1560=[
            25823,
            10330,
            25823,
            25820,
            30987,
            0,
            30990,
            30990,
            15500,
            10300,
            258000,
            0,
            30987,
            18100,
            30980,
            25800,
            0,
            0,
            0,
            30987,
            5165,
            0,
            25823,
        ],
        addizionale_9999=[
            25823,
            10330,
            25823,
            30990,
            30987,
            0,
            30990,
            30990,
            15500,
            10300,
            258000,
            0,
            30987,
            25800,
            30980,
            25800,
            0,
            0,
            0,
            30987,
            5165,
            0,
            30987,
        ],
    ),
]


# ADDIZIONALE REGIONALE INDUSTRIALE
# A statuto speciale: FRIULI V.G. , SARDEGNA, SICILIA, TRENTINO AA., V.D'AOSTA
class AddizionaleGasIndustrialePercentages(BaseModel):
    date: date
    region: list[str]
    scaglione_ind: list[int]  # [12, 9999]
    addizionale_12: list[int]  # < 1,2 M(m3)
    addizionale_99: list[int]  # > 1,2 M(m3)


# addizionale_gas_civile_percentages: list[AddizionaleGasIndustrialePercentages] = []
addizionale_gas_industriale_percentages: list[AddizionaleGasIndustrialePercentages] = [
    AddizionaleGasIndustrialePercentages(
        date=date(2024, 1, 1),
        region=[
            "Abruzzo",
            "Abruzzo (fascia e ed f)",
            "Basilicata",
            "Calabria",
            "Emilia-romagna",
            "Friuli v.g.",
            "Lazio",
            "Lazio (ex casmez)",
            "Liguria (fascia climatica e)",
            "Liguria (fascia climatica f)",
            "Liguria (fascia climatica c/d)",
            "Lombardia",
            "Molise",
            "Marche",
            "Puglia",
            "Piemonte",
            "Sardegna",
            "Sicilia",
            "Trentino aa.",
            "Toscana",
            "UmbriaV.d'aosta",
            "Veneto",
        ],
        scaglione_ind=[12, 9999],
        addizionale_12=[
            6249,
            6249,
            6249,
            6249,
            6249,
            0,
            6249,
            6249,
            6249,
            6249,
            6249,
            0,
            6200,
            6249,
            6249,
            6249,
            0,
            0,
            0,
            6000,
            5165,
            0,
            6249,
        ],
        addizionale_99=[
            5160,
            5160,
            5165,
            5165,
            5165,
            0,
            5160,
            5160,
            5200,
            5200,
            5200,
            0,
            5200,
            5200,
            5165,
            5200,
            0,
            0,
            0,
            5200,
            5165,
            0,
            5165,
        ],  # > 1,2 M(m3)
    ),
    AddizionaleGasIndustrialePercentages(
        date=date(2025, 1, 1),
        region=[
            "Abruzzo",
            "Abruzzo (fascia e ed f)",
            "Basilicata",
            "Calabria",
            "Emilia-romagna",
            "Friuli v.g.",
            "Lazio",
            "Lazio (ex casmez)",
            "Liguria (fascia climatica e)",
            "Liguria (fascia climatica f)",
            "Liguria (fascia climatica c/d)",
            "Lombardia",
            "Molise",
            "Marche",
            "Puglia",
            "Piemonte",
            "Sardegna",
            "Sicilia",
            "Trentino aa.",
            "Toscana",
            "UmbriaV.d'aosta",
            "Veneto",
        ],
        scaglione_ind=[12, 9999],
        addizionale_12=[
            6249,
            6249,
            6249,
            6249,
            6249,
            0,
            6249,
            6249,
            6249,
            6249,
            6249,
            0,
            6200,
            6249,
            6249,
            6249,
            0,
            0,
            0,
            6000,
            5165,
            0,
            6249,
        ],
        addizionale_99=[
            5160,
            5160,
            5165,
            5165,
            5165,
            0,
            5160,
            5160,
            5200,
            5200,
            5200,
            0,
            5200,
            5200,
            5165,
            5200,
            0,
            0,
            0,
            5200,
            5165,
            0,
            5165,
        ],  # > 1,2 M(m3)
    ),
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
@app.post("/ee/ivas", response_model=IvaEePercentages)
async def add_ee_iva(iva: IvaEePercentages) -> IvaEePercentages:
    iva.date = date.today()  # datetime.now()
    iva_ee_pecentages.append(iva)
    return iva


@app.get("/ee/ivas", response_model=list[IvaEePercentages])
async def read_ee_ivas() -> list[IvaEePercentages]:
    return iva_ee_pecentages


#  ACCISE
@app.post("/ee/accises", response_model=AcciseEePercentages)
async def add_ee_accise(accise: AcciseEePercentages) -> AcciseEePercentages:
    accise.date = date.today()  # datetime.now()
    accise_ee_percentages.append(accise)
    return accise


@app.get("/ee/accises", response_model=list[AcciseEePercentages])
async def read_ee_accises() -> list[AcciseEePercentages]:
    return accise_ee_percentages


#  ---  Gas  ---
@app.get("/gas/")
async def gas() -> dict[str, str]:
    return {"message": "You are inside GAS"}


# IVA
@app.post("/gas/ivas", response_model=IvaGasPercentages)
async def add_gas_iva(iva: IvaGasPercentages) -> IvaGasPercentages:
    iva.date = date.today()  # datetime.now()
    iva_gas_pecentages.append(iva)
    return iva


@app.get("/gas/ivas", response_model=list[IvaGasPercentages])
async def read_gas_ivas() -> list[IvaGasPercentages]:
    return iva_gas_pecentages


#  ACCISE
@app.post("/gas/accises", response_model=AcciseGasCivilePercentages)
async def add_gas_accise(
    accise: AcciseGasCivilePercentages,
) -> AcciseGasCivilePercentages:
    accise.date = date.today()  # datetime.now()
    accise_gas_civile_percentages.append(accise)
    return accise


@app.get("/gas/accises", response_model=list[AcciseGasCivilePercentages])
async def read_gas_accises() -> list[AcciseGasCivilePercentages]:
    return accise_gas_civile_percentages


#  ADDIZIONALE CIVILE
@app.post("/gas/addizi_civ", response_model=AddizionaleGasCivilePercentages)
async def add_gas_addiz_civ(
    addiz_civ: AddizionaleGasCivilePercentages,
) -> AddizionaleGasCivilePercentages:
    addiz_civ.date = date.today()  # datetime.now()
    addizionale_gas_civile_percentages.append(addiz_civ)
    return addiz_civ


@app.post("/gas/addizi_civ", response_model=AddizionaleGasCivilePercentages)
async def read_gas_addiz_civ() -> list[AddizionaleGasCivilePercentages]:
    return addizionale_gas_civile_percentages


#  ADDIZIONALE INDUSTRIALE
@app.post("/gas/addizi_ind", response_model=AddizionaleGasIndustrialePercentages)
async def add_gas_addiz_ind(
    addiz_ind: AddizionaleGasIndustrialePercentages,
) -> AddizionaleGasIndustrialePercentages:
    addiz_ind.date = date.today()  # datetime.now()
    addizionale_gas_industriale_percentages.append(addiz_ind)
    return addiz_ind


@app.post("/gas/addizi_ind", response_model=AddizionaleGasIndustrialePercentages)
async def read_gas_addiz_ind() -> list[AddizionaleGasIndustrialePercentages]:
    return addizionale_gas_industriale_percentages


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
