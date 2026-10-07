# API em Container: letras do nome × número (porta 12345)

API em FastAPI, empacotada com Docker. Recebe um `POST` com `nome` e `numero` e retorna a **quantidade de letras do nome × o número**.

**Exemplo:** `{"nome": "Ana", "numero": 2}` → `{"nome":"Ana","letras":3,"numero":2.0,"resultado":6.0}`

## 🛠️ Arquivos

- `app.py`: API (`POST /`). Espaços e números no nome não contam como letras.
- `Dockerfile`: imagem `python:3.12-slim`, uvicorn em `0.0.0.0:12345`.

## A. Rodar localmente

```bash
cd api_letras_docker
docker build -t exercicio-letras .
docker run -d -p 12345:12345 exercicio-letras
curl -X POST localhost:12345/ -H 'Content-Type: application/json' -d '{"nome":"Ana","numero":2}'
```

Para parar: `docker ps` (veja o ID) e `docker stop <ID>`.

## B. Subir no Ebino (passo a passo)

1. **Conectar na VPN do MPES** (na sua máquina):
   ```bash
   vpn-mpes connect
   ```
2. **Copiar a pasta para a VM** (na raiz do repositório, **fora do SSH**):
   ```bash
   scp -r api_letras_docker acarmo@ebino.mpes.gov.br:~/
   ```
3. **Entrar na VM**:
   ```bash
   ssh acarmo@ebino.mpes.gov.br
   ```
4. **Buildar a imagem** (na VM; precisa de `sudo`, pois o usuário não está no grupo `docker`):
   ```bash
   cd ~/api_letras_docker
   sudo docker build -t exercicio-letras .
   ```
5. **Subir o container**:
   ```bash
   sudo docker run -d --restart unless-stopped -p 12345:12345 exercicio-letras
   ```
   > Se aparecer `port is already allocated`, já existe um container na porta 12345. Veja com `sudo docker ps` e pare com `sudo docker stop <ID>` para recriar.
6. **Testar dentro da VM**:
   ```bash
   curl -X POST localhost:12345/ -H 'Content-Type: application/json' -d '{"nome":"Ana","numero":2}'
   ```
7. **Testar da sua máquina** (VPN ligada):
   ```bash
   curl -X POST http://ebino.mpes.gov.br:12345/ -H 'Content-Type: application/json' -d '{"nome":"Ana","numero":2}'
   ```
   Se der timeout, a porta está bloqueada no firewall. Use um túnel SSH:
   ```bash
   ssh -L 12345:localhost:12345 acarmo@ebino.mpes.gov.br
   ```
   Com o túnel aberto, em outro terminal: `curl -X POST localhost:12345/ -H 'Content-Type: application/json' -d '{"nome":"Ana","numero":2}'`

## Problemas comuns

| Erro | Causa / solução |
|------|-----------------|
| `Could not resolve hostname` | Domínio digitado errado (é `.gov.br`) ou VPN desconectada. |
| `permission denied ... docker.sock` | Use `sudo` antes do `docker`. |
| `cd: ... Arquivo ou diretório inexistente` | A pasta não foi copiada. Refaça o `scp` (passo 2). |
| `port is already allocated` | Já há um container na porta 12345 (`sudo docker ps`). |
| `command not found` com `^[[200~` ou `~` | Caracteres de colagem no terminal. Digite o comando à mão. |
