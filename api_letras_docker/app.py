from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Exercício Letras x Número")

# Permite que a interface HTML (aberta via file://) chame a API pelo navegador.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)


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
