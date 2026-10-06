from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Exercício Letras x Número")


class Entrada(BaseModel):
    nome: str
    numero: float


@app.post("/")
def calcular(entrada: Entrada):
    letras = sum(1 for c in entrada.nome if c.isalpha())
    return {
        "nome": entrada.nome,
        "letras": letras,
        "numero": entrada.numero,
        "resultado": letras * entrada.numero,
    }
