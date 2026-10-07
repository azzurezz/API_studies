# API em Container: letras do nome × número

API em FastAPI, empacotada com Docker. Recebe um `POST` com `nome` e `numero` e retorna a **quantidade de letras do nome × o número**.

> Quer publicar/atualizar a API no servidor? Veja [DEPLOY.md](DEPLOY.md).

## 📥 Requisição

`POST /` com JSON:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `nome` | texto | Nome a contar. Espaços e números não contam como letras. |
| `numero` | número | Multiplicador (aceita decimais). |

**Exemplo:**
```bash
curl -X POST http://localhost:12345/ \
     -H 'Content-Type: application/json' \
     -d '{"nome":"Ana","numero":2}'
```

**Resposta (HTTP 200):**
```json
{"nome":"Ana","letras":3,"numero":2.0,"resultado":6.0}
```

Se o JSON for inválido (ex.: `numero` em texto), a API responde HTTP `422` com o detalhe do erro.

## 🧪 Como testar

Escolha **uma** das formas abaixo.

### Opção 1: Usar a API que está no servidor (Ebino)

**Pré-requisito:** estar conectado na VPN do MPES.

**1a. Acesso direto** (funciona quando a porta 12345 está liberada no firewall):
```bash
curl -X POST http://ebino.mpes.gov.br:12345/ \
     -H 'Content-Type: application/json' \
     -d '{"nome":"Ana","numero":2}'
```
Se der `Connection refused` ou timeout, use a 1b.

**1b. Túnel SSH** (precisa de usuário no Ebino):

1. Abra o túnel e **deixe esse terminal aberto**:
   ```bash
   ssh -L 12345:localhost:12345 SEU_USUARIO@ebino.mpes.gov.br
   ```
   > Se aparecer `Address already in use`, a porta 12345 da sua máquina já está ocupada. Troque o primeiro número, por exemplo `-L 8080:localhost:12345`, e use `localhost:8080` nos passos seguintes.
2. Em **outro terminal**, chame a API:
   ```bash
   curl -X POST http://localhost:12345/ \
        -H 'Content-Type: application/json' \
        -d '{"nome":"Ana","numero":2}'
   ```
3. Ao terminar, digite `exit` no terminal do túnel.

### Opção 2: Rodar na sua máquina (sem VPN)

**Pré-requisito:** Docker instalado.

```bash
cd api_letras_docker
docker build -t exercicio-letras .
docker run -d -p 12345:12345 exercicio-letras
curl -X POST http://localhost:12345/ -H 'Content-Type: application/json' -d '{"nome":"Ana","numero":2}'
```

Para parar:
```bash
docker ps                # copie o ID do container
docker stop <ID>
```

### Documentação interativa

Com a API acessível, abra `http://localhost:12345/docs` no navegador (Swagger) e teste pela interface.

## 🖥️ Interface web (opcional)

Em vez de usar `curl`, você pode usar a página [interface.html](interface.html):

1. Deixe a API acessível em `localhost:12345` (Opção 1b ou Opção 2 acima).
2. Abra o arquivo `interface.html` no navegador (clique duas vezes ou arraste para a janela).
3. Digite o nome e o número e clique em **Calcular**.

Se a API estiver em outro endereço ou porta (ex.: túnel em `8080`), abra "Endereço da API" na página e troque a URL, por exemplo `http://localhost:8080/`.

> A página só funciona com a versão da API que libera CORS. Se aparecer "Não consegui falar com a API" mesmo com ela rodando, a versão do servidor está desatualizada. Veja [DEPLOY.md](DEPLOY.md).

## ❓ Problemas comuns

| Erro | Causa / solução |
|------|-----------------|
| `Could not resolve hostname` | Domínio digitado errado (é `.gov.br`) ou VPN desconectada. |
| `Connection refused` no acesso direto | Porta bloqueada no firewall. Use o túnel SSH (1b). |
| `Address already in use` no túnel | Porta local ocupada. Use outra, como `-L 8080:localhost:12345`. |
| `port is already allocated` ao rodar local | Já há um container na 12345. Veja com `docker ps` e pare com `docker stop <ID>`. |
| `Permission denied` no SSH | Senha errada ou sem acesso ao Ebino. Fale com o administrador. |
| Resposta de outra API / resultado estranho | Pode haver outro container na mesma porta. Confira com `docker ps`. |
| `command not found` com `^[[200~` ou `~` | Caracteres de colagem no terminal. Digite o comando à mão. |
| Interface: "Não consegui falar com a API" | API fora do ar, URL errada ou versão sem CORS. Teste com `curl` primeiro. |
