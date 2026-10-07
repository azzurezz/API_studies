# API de Processamento de Números e Palavras (POST)

API em Python (FastAPI) que recebe um número inteiro e uma palavra via `POST`, valida os dados, calcula a 10ª potência do número, conta as letras da palavra, aguarda 5 segundos e retorna os resultados.

## 📋 Funcionalidades

1. **Endpoint `POST /processar`**: recebe um JSON com `numero` e `palavra`.
2. **Validações**:
   - `numero`: deve ser **inteiro** (`int`).
   - `palavra`: apenas letras (`isalpha()`), sem números, espaços ou caracteres especiais.
3. **Processamento**:
   - Calcula $numero^{10}$.
   - Conta as letras da palavra (`len(palavra)`).
   - Aguarda **5 segundos** de forma assíncrona (`await asyncio.sleep(5)`).
4. **Retorno**: JSON com `numero_potencia_10`, `quantidade_letras` e mensagem de status.

## 🛠️ Arquivos

- `main.py`: servidor da API com FastAPI e validações Pydantic.
- `client.py`: cliente em Python que consome a API (`requests`).
- `curl_examples.sh`: exemplos de requisição via `curl`.
- `test_main.py`: testes automatizados.
- `requirements.txt`: dependências.

## 🚀 Como Executar

Todos os comandos abaixo partem da pasta `api_potencia/`:

```bash
cd api_potencia
pip install -r requirements.txt
```

### 1. Iniciar a API

```bash
python3 main.py
```

A API roda em `http://127.0.0.1:8000`. Swagger em `http://127.0.0.1:8000/docs`.

### 2. Consumir via Python

Em outro terminal:

```bash
python3 client.py
```

### 3. Consumir via cURL

```bash
curl -X POST "http://127.0.0.1:8000/processar" \
     -H "Content-Type: application/json" \
     -d '{"numero": 2, "palavra": "Python"}'
```

Resposta (HTTP 200):

```json
{
  "sucesso": true,
  "numero_potencia_10": 1024,
  "quantidade_letras": 6,
  "mensagem": "Processamento concluído com sucesso após 5 segundos de espera."
}
```

### 4. Testes automatizados

```bash
python3 -m unittest test_main.py
```
