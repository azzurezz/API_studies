#!/bin/bash

# Script de exemplo para consumir a API via cURL

echo "============================================================"
echo "1. Requisição com DADOS VÁLIDOS (Número: 2, Palavra: 'Exemplo')"
echo "Esperando 5 segundos pela resposta..."
echo "============================================================"

curl -X POST "http://127.0.0.1:8000/processar" \
     -H "Content-Type: application/json" \
     -d '{"numero": 2, "palavra": "Exemplo"}' \
     -w "\nTempo total: %{time_total}s\n\n"

echo "============================================================"
echo "2. Requisição INVÁLIDA (Palavra com número: 'Teste123')"
echo "============================================================"

curl -X POST "http://127.0.0.1:8000/processar" \
     -H "Content-Type: application/json" \
     -d '{"numero": 5, "palavra": "Teste123"}' \
     -w "\n\n"

echo "============================================================"
echo "3. Requisição INVÁLIDA (Número com vírgula/ponto: 7.89)"
echo "============================================================"

curl -X POST "http://127.0.0.1:8000/processar" \
     -H "Content-Type: application/json" \
     -d '{"numero": 7.89, "palavra": "Validar"}' \
     -w "\n\n"
