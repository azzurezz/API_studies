# Deploy no Ebino

Guia para quem **publica ou atualiza** a API no servidor Ebino. Para apenas usar a API, veja o [README](README.md).

## Pré-requisitos

- Usuário com acesso SSH ao Ebino (`ebino.mpes.gov.br`).
- VPN do MPES conectada (`vpn-mpes connect`).
- Permissão de `sudo` na VM (o usuário não está no grupo `docker`, então todo comando `docker` usa `sudo`).

## Passo a passo

1. **Copiar a pasta para a VM.** Rode na **raiz do repositório**, **fora do SSH**:
   ```bash
   scp -r api_letras_docker SEU_USUARIO@ebino.mpes.gov.br:~/
   ```
2. **Entrar na VM:**
   ```bash
   ssh SEU_USUARIO@ebino.mpes.gov.br
   ```
3. **Buildar a imagem** (na VM):
   ```bash
   cd ~/api_letras_docker
   sudo docker build -t exercicio-letras .
   ```
4. **Subir o container:**
   ```bash
   sudo docker run -d --restart unless-stopped -p 12345:12345 exercicio-letras
   ```
   O `--restart unless-stopped` faz o container subir sozinho se a VM reiniciar.
5. **Testar dentro da VM:**
   ```bash
   curl -X POST localhost:12345/ -H 'Content-Type: application/json' -d '{"nome":"Ana","numero":2}'
   ```
   Esperado: `{"nome":"Ana","letras":3,"numero":2.0,"resultado":6.0}`

## Atualizar uma versão já publicada

> Necessário sempre que o `app.py` mudar. Em especial, a [interface.html](interface.html) só funciona se o servidor rodar a versão com CORS liberado.

Se o código mudou, o container antigo continua na porta 12345 e impede o novo de subir (`port is already allocated`). Troque assim:

```bash
sudo docker ps                         # copie o ID do container antigo
sudo docker stop <ID>
sudo docker rm <ID>
cd ~/api_letras_docker
sudo docker build -t exercicio-letras .
sudo docker run -d --restart unless-stopped -p 12345:12345 exercicio-letras
```

## Liberar a porta para acesso direto (opcional)

Por padrão, pode ser que a porta 12345 só responda dentro da VM (`Connection refused` de fora). Para que outras pessoas na VPN acessem direto, sem túnel SSH, libere a porta no firewall da VM:

```bash
sudo firewall-cmd --list-ports
sudo firewall-cmd --permanent --add-port=12345/tcp
sudo firewall-cmd --reload
```

Se o `sudo` for negado, ou houver firewall de rede entre a VPN e a VM, peça ao administrador para liberar a porta TCP 12345.

> A API não tem autenticação. Liberar a porta permite que qualquer pessoa da rede interna a chame.

## Comandos úteis na VM

```bash
sudo docker ps                 # containers em execução
sudo docker logs <ID>          # logs da API
sudo docker stop <ID>          # parar
```

## Problemas comuns

| Erro | Causa / solução |
|------|-----------------|
| `permission denied ... docker.sock` | Use `sudo` antes do `docker`. |
| `cd: ... Arquivo ou diretório inexistente` | A pasta não foi copiada. Refaça o `scp` (passo 1). |
| `scp: stat local ...: No such file` | Você não está na raiz do repositório. Rode `cd ..` até ver a pasta `api_letras_docker`. |
| `port is already allocated` | Há um container na 12345. Veja "Atualizar uma versão já publicada". |
| `Permission denied` no SSH | Senha errada (ela não aparece ao digitar). Muitas falhas seguidas podem bloquear a conta. |
