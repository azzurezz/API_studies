import time
import requests

# URL do endpoint da API
API_URL = "http://127.0.0.1:8000/processar"


def enviar_requisicao(numero, palavra):
    """
    Envia uma requisição POST para a API e exibe a resposta e o tempo decorrido.
    """
    print("=" * 60)
    print(f"Enviando dados para API:")
    print(f"   - Número: {numero} (tipo: {type(numero).__name__})")
    print(f"   - Palavra: '{palavra}'")
    
    payload = {
        "numero": numero,
        "palavra": palavra
    }

    inicio = time.time()
    try:
        resposta = requests.post(API_URL, json=payload, timeout=10)
        tempo_decorrido = time.time() - inicio

        print(f"Tempo total de resposta: {tempo_decorrido:.2f} segundos")
        print(f"Código HTTP: {resposta.status_code}")

        if resposta.status_code == 200:
            dados = resposta.json()
            print("Sucesso no processamento!")
            print(f"Número elevado à 10ª potência: {dados['numero_potencia_10']}")
            print(f"Quantidade de letras na palavra: {dados['quantidade_letras']}")
            print(f"Mensagem: {dados['mensagem']}")
        else:
            print("Erro de Validação/Requisição:")
            print(f"Detalhes: {resposta.json()}")

    except requests.exceptions.ConnectionError:
        print("Erro: Não foi possível conectar à API. Certifique-se de que a API esteja rodando em http://127.0.0.1:8000")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    print("=" * 60 + "\n")


def modo_interativo():

    try:
        entrada_num = input("Digite um número inteiro: ").strip()
        try:
            numero = int(entrada_num)
        except ValueError:
            # Caso o usuário digite um float ou texto, repassamos como float ou string para a API validar
            try:
                numero = float(entrada_num)
            except ValueError:
                numero = entrada_num

        palavra = input("Digite uma palavra (apenas letras): ").strip()
        print()
        enviar_requisicao(numero, palavra)
    except KeyboardInterrupt:
        print("Operação cancelada pelo usuário.")


def rodar_testes_predefinidos():
    print("Executando testes pré-definidos...")

    # 1. Caso de Sucesso 1
    print("TESTE 1: Dados válidos (Número: 2, Palavra: 'Python')")
    enviar_requisicao(numero=2, palavra="Python")

    # 2. Caso de Sucesso 2
    print("TESTE 2: Dados válidos (Número: 3, Palavra: 'Desenvolvimento')")
    enviar_requisicao(numero=3, palavra="Desenvolvimento")

    # 3. Caso de Erro: Palavra com números/espaços
    print("TESTE 3: Validação incorreta (Palavra contém número 'Python3')")
    enviar_requisicao(numero=5, palavra="Python3")

    # 4. Caso de Erro: Número não é inteiro (float ou string inválida)
    print("TESTE 4: Validação incorreta (Número não é inteiro '3.14')")
    enviar_requisicao(numero=3.14, palavra="Teste")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--auto":
        rodar_testes_predefinidos()
    else:
        while True:
            modo_interativo()
            opcao = input("Deseja fazer outro teste? (s/n): ").strip().lower()
            if opcao != 's':
                print("Obrigado!")
                break
            print("\n" + "-" * 60 + "\n")

