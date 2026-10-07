import asyncio
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, field_validator
import uvicorn

# Inicialização da aplicação FastAPI
app = FastAPI(
    title="API de Processamento de Números e Palavras",
    description="API que valida um número inteiro e uma palavra, eleva o número à 10ª potência, conta as letras da palavra e retorna os dois valores após 5 segundos.",
    version="1.0.0"
)


# Modelo de dados recebido na requisição POST
class ProcessRequest(BaseModel):
    numero: int = Field(
        ...,
        description="Número inteiro que será elevado à décima potência."
    )
    palavra: str = Field(
        ...,
        description="Palavra contendo apenas letras que terá seu comprimento contado."
    )

    @field_validator('palavra')
    @classmethod
    def validar_apenas_letras(cls, v: str) -> str:
        """
        Valida se a palavra fornecida contém exclusivamente caracteres alfabéticos.
        Retorna erro se houver números, espaços ou símbolos.
        """
        v_trimmed = v.strip()
        if not v_trimmed:
            raise ValueError("A palavra não pode estar vazia.")
        
        if not v_trimmed.isalpha():
            raise ValueError("A palavra deve conter apenas letras (sem números, espaços ou caracteres especiais).")
        
        return v_trimmed


# Modelo de dados retornado na resposta da API
class ProcessResponse(BaseModel):
    sucesso: bool
    numero_potencia_10: int = Field(..., description="O número informado elevado à 10ª potência.")
    quantidade_letras: int = Field(..., description="Quantidade de letras da palavra informada.")
    mensagem: str = Field(..., description="Mensagem de status do processamento.")


@app.post(
    "/processar",
    response_model=ProcessResponse,
    status_code=status.HTTP_200_OK,
    summary="Processa um número inteiro e uma palavra",
    description="Valida as entradas, calcula a 10ª potência do número, conta as letras da palavra, aguarda 5 segundos e retorna os resultados."
)
async def processar_dados(payload: ProcessRequest):
    # 1. Validação de dados é feita automaticamente pelo Pydantic:
    #    - 'numero' é validado como número inteiro.
    #    - 'palavra' é validada para conter apenas letras.

    # 2. Operações solicitadas
    potencia = payload.numero ** 10
    qtd_letras = len(payload.palavra)

    # 3. Espera assíncrona de 5 segundos
    await asyncio.sleep(5)

    # 4. Retorno dos dois valores calculados
    return ProcessResponse(
        sucesso=True,
        numero_potencia_10=potencia,
        quantidade_letras=qtd_letras,
        mensagem=f"Processamento concluído com sucesso após 5 segundos de espera."
    )


if __name__ == "__main__":
    # Permite rodar a API diretamente via `python main.py`
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
