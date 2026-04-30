from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
import pandas as pd

app = FastAPI()

@app.post("/IMC")
async def calcola_imc(dati: dict):
    nome = dati.get("nome", "")
    peso = float(dati.get("peso", 0))
    altezza = float(dati.get("altezza", 0))
    imc = peso / (altezza ** 2) if peso > 0 and altezza > 0 else None
    risultato = {"Nome": nome, "Peso": peso, "Altezza": altezza, "IMC": round(imc, 2) if imc is not None else None}

    file_path = "imc.xlsx"
    if os.path.exists(file_path):
        df = pd.read_excel(file_path)
        df = pd.concat([df, pd.DataFrame([risultato])], ignore_index=True)
    else:
        df = pd.DataFrame([risultato])

    df.to_excel(file_path, index=False)
    return {"imc": risultato["IMC"]}

app.mount("/", StaticFiles(directory="static", html=True), name="static")
