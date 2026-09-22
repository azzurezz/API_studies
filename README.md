# API de Processamento de Números e Palavras (POST)

Esta API em Python (FastAPI) recebe um número inteiro e uma palavra através de uma requisição `POST`, valida os dados recebidos, calcula a 10ª potência do número, conta as letras da palavra, aguarda 5 segundos e retorna os resultados.

---

## 📋 Funcionalidades

1. **Endpoint `POST /processar`**: Recebe um JSON com `numero` e `palavra`.
2. **Validações**:
   - `numero`: Deve ser obrigatoriamente um número **inteiro** (`int`).
   - `palavra`: Deve conter **apenas letras** (`isalpha()`), sem números, espaços ou caracteres especiais.
3. **Processamento**:
   - Calcula $numero^{10}$ (número elevado à décima potência).
   - Conta a quantidade de letras da palavra (`len(palavra)`).
   - Aguarda **5 segundos** de forma assíncrona (`await asyncio.sleep(5)`).
4. **Retorno**: JSON com `numero_potencia_10`, `quantidade_letras` e mensagem de status.

---

## 🛠️ Arquivos do Projeto

- [main.py](file:///home/azzure/%C3%81rea%20de%20Trabalho/estudos/API_studies/main.py): Código servidor da API com FastAPI e validações Pydantic.
- [client.py](file:///home/azzure/%C3%81rea%20de%20Trabalho/estudos/API_studies/client.py): Script cliente em Python que consome a API (`requests`).
- [curl_examples.sh](file:///home/azzure/%C3%81rea%20de%20Trabalho/estudos/API_studies/curl_examples.sh): Script Shell com exemplos de requisição via `curl`.
- [test_main.py](file:///home/azzure/%C3%81rea%20de%20Trabalho/estudos/API_studies/test_main.py): Testes automatizados da API.

---

## 🚀 Como Executar

### 1. Iniciar a API Server

No terminal, dentro do diretório do projeto, execute:

```bash
python3 main.py
```

*A API estará rodando em `http://127.0.0.1:8000`.*
*Você pode acessar a documentação interativa Swagger no navegador em:* `http://127.0.0.1:8000/docs`

---

### 2. Consumir a API via Python Client

Em outro terminal, execute o cliente:

```bash
python3 client.py
```

---

### 3. Consumir a API via cURL (Terminal)

```bash
curl -X POST "http://127.0.0.1:8000/processar" \
     -H "Content-Type: application/json" \
     -d '{"numero": 2, "palavra": "Python"}'
```

**Exemplo de Resposta (HTTP 200):**

```json
{
  "sucesso": true,
  "numero_potencia_10": 1024,
  "quantidade_letras": 6,
  "mensagem": "Processamento concluído com sucesso após 5 segundos de espera."
}
```

---

### 4. Executar os Testes Automatizados

```bash
python3 -m unittest test_main.py
```
