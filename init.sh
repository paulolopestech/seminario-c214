#!/bin/bash

nome_venv=".pyvenv"
if [ -d "$nome_venv" ]; then
  echo "O ambiente virtual '$nome_venv' já existe."
else
  python -m venv "$nome_venv"
  echo "Ambiente virtual '$nome_venv' criado."
fi

source "$nome_venv/Scripts/activate"
echo "O ambiente virtual '$nome_venv' está ativado."

if [ -f "requirements.txt" ]; then
  pip install -r requirements.txt
  echo "Os pacotes em 'requirements.txt' foram instalados."
else
  echo "Erro ao instalar dependências, nenhum 'requirements.txt' encontrado!"
fi