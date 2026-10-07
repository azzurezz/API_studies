# API Studies

Estudos de APIs em Python (FastAPI). O repositório tem duas APIs independentes, cada uma na sua pasta com README próprio.

| Pasta | O que faz | Como roda |
|-------|-----------|-----------|
| [`api_potencia/`](api_potencia/README.md) | `POST /processar`: recebe número inteiro e palavra, retorna número¹⁰ e a quantidade de letras (com espera de 5 s). | Python local, porta 8000 |
| [`api_letras_docker/`](api_letras_docker/README.md) | `POST /`: recebe nome e número, retorna letras do nome × número. | Docker, porta 12345 (deploy no Ebino) |

## Estrutura

```
API_studies/
├── api_potencia/          # API 1 (main.py, client.py, testes, curl)
├── api_letras_docker/     # API 2 (app.py, Dockerfile, README.md, DEPLOY.md)
├── LICENSE
└── README.md
```

Cada API tem o passo a passo de uso no README da sua pasta. Para publicar a `api_letras_docker` no servidor Ebino, veja o [DEPLOY.md](api_letras_docker/DEPLOY.md).
