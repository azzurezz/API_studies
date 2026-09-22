import time
import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestAPIProcessamento(unittest.TestCase):

    def test_processamento_sucesso(self):
        """Testa o envio de dados válidos e a resposta com 5s de espera."""
        inicio = time.time()
        payload = {"numero": 2, "palavra": "Python"}
        
        response = client.post("/processar", json=payload)
        tempo_decorrido = time.time() - inicio

        # Verifica código de status HTTP
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertTrue(data["sucesso"])
        self.assertEqual(data["numero_potencia_10"], 2 ** 10)  # 1024
        self.assertEqual(data["quantidade_letras"], 6)          # "Python" -> 6
        
        # Verifica que esperou no mínimo 5 segundos
        self.assertGreaterEqual(tempo_decorrido, 5.0)

    def test_palavra_com_numeros_deve_falhar(self):
        """Testa se a validação rejeita palavras contendo números."""
        payload = {"numero": 5, "palavra": "Python123"}
        response = client.post("/processar", json=payload)
        
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity
        data = response.json()
        self.assertIn("detail", data)

    def test_palavra_com_espacos_deve_falhar(self):
        """Testa se a validação rejeita palavras com espaços."""
        payload = {"numero": 5, "palavra": "Ola Mundo"}
        response = client.post("/processar", json=payload)
        
        self.assertEqual(response.status_code, 422)

    def test_numero_nao_inteiro_deve_falhar(self):
        """Testa se a validação rejeita números com ponto flutuante (decimal)."""
        payload = {"numero": 4.5, "palavra": "Teste"}
        response = client.post("/processar", json=payload)
        
        self.assertEqual(response.status_code, 422)

    def test_numero_string_invalida_deve_falhar(self):
        """Testa se a validação rejeita strings não numéricas no campo número."""
        payload = {"numero": "abc", "palavra": "Teste"}
        response = client.post("/processar", json=payload)
        
        self.assertEqual(response.status_code, 422)


if __name__ == "__main__":
    unittest.main()
