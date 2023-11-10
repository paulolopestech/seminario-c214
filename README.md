# 🐍🤖 Seminário

API para geração de gráficos para análise de dados.  
![unit-tests](https://github.com/paulolopestech/seminario-c214/actions/workflows/unit-tests.yaml/badge.svg)

## 🛠️ Tecnologias utilizadas
- [Python](https://www.python.org) - Linguagem de programação que permite trabalhar de forma eficaz e integrar sistemas.
- [Robot Framework](https://robotframework.org/) - Framework aberta e genérica para automação e testes automatizados.

## ✨ Funcionalidades da API - Visualure

- Pode aceitar dados em formato de array.
- Valida os dados de entrada automaticamente.
- Retorna uma página estática contendo o gráfico em formato de imagem.
- Retorna uma página de erro tratando quando a entrada estiver errada.

### Requisitos

- Python 3.8 ou superior instalado localmente, para geração do ambiente virtual.  
O instalador do `Python` pode ser encontrado no [link](https://www.python.org).

### Instruções de Uso

1. **Clone o Repositório:**
   ```bash
   git clone https://github.com/paulolopestech/seminario-c214
   cd seminario-c214
   ```

2. **Execute o Script de Inicialização:**
   ```bash
   sh init.sh
   ```
   O script `init.sh` automatiza o processo de criação de um ambiente virtual Python e a instalação das bibliotecas necessárias.

3. **Ative o Ambiente Virtual:**
   ```bash
   .pyvenv/Scripts/activate
   ```
   Isso ativará o ambiente virtual. Certifique-se de fazer isso antes de executar seu código para garantir que as dependências corretas estejam sendo usadas.

4. **Execute Seu Código:**
   ```bash
   python src/api.py
   ```

### Notas Adicionais

- Certifique-se de ter o Python 3.8 ou uma versão superior instalada no seu sistema antes de executar o script.
- O script cria um ambiente virtual chamado `.pyvenv` no diretório do projeto.
- Para sair do ambiente virtual, basta digitar:
  ```bash
  deactivate
  ```
- Certifique-se que o diretório `.pyvenv` permaneça no seu arquivo `.gitignore` para evitar que o ambiente virtual seja incluído no repositório Git.
- Caso ocorram problemas durante a execução do script, verifique se as permissões são adequadas e se o Python 3.8 ou superior está instalado no sistema.

## 🟦 TESTES:

### Requisitos
- Python 3.8 ou superior instalado

### Estrutura do Projeto

- **src/:** Contém os arquivos fontes do projeto.
- **src/test/unit/:** Contém os casos de teste escritos com o Robot Framework.

### Instruções de Uso
1. **Ative o Ambiente Virtual:**
   ```bash
   .pyvenv/Scripts/activate
   ```
   Isso ativará o ambiente virtual. Certifique-se de fazer isso antes de executar seu código para garantir que as dependências corretas estejam sendo usadas.

2. **Execute os Testes com o Robot Framework:**
    ```bash
    robot src/test/unit/
    ```
    Isso executará todos os testes na pasta `src/test/unit/` usando o Robot Framework.

## 👥 Equipe

<div style="display: flex; justify-content: space-between;">
  <a href="https://github.com/DIEGOVZK" style="margin-right: 10px;">
    <img src="https://avatars.githubusercontent.com/u/45247817?v=4" alt="Diego Anestor Coutinho" width="150" height="auto">
    <p> Diego Anestor Coutinho </p>
  </a>
  <a href="https://github.com/dioic3" style="margin-right: 10px;">
    <img src="https://avatars.githubusercontent.com/u/82656277?v=4" alt="Joyce da Costa" width="150" height="auto">
    <p> Joyce da Costa </p>
  </a>
  <a href="https://github.com/NathanAtaliba" style="margin-right: 10px;">
    <img src="https://avatars.githubusercontent.com/u/100451579?v=4" alt="Nathan Ataliba" width="150" height="auto">
    <p> Nathan Ataliba </p>
  </a>
  <a href="https://github.com/paulolopestech">
    <img src="https://avatars.githubusercontent.com/u/68427914?v=4" alt="Paulo Lopes" width="150" height="auto">
    <p> Paulo Lopes </p>
  </a>
</div>
