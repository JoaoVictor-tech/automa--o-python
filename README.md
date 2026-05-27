 # 🤖 Automação de Cadastro de Produtos (RPA)

Este projeto é uma automação desenvolvida em Python para otimizar e acelerar o processo de cadastro de produtos em um sistema web. Utilizando conceitos de RPA (Robotic Process Automation), o script lê uma base de dados estruturada e simula a interação humana com o mouse e o teclado para preencher os formulários automaticamente.

---

## 🛠️ Tecnologias Utilizadas

* **Python**: Linguagem principal do projeto.
* **PyAutoGUI**: Biblioteca responsável por controlar o mouse e o teclado, automatizando os cliques e a digitação.
* **Pandas**: Biblioteca utilizada para leitura, manipulação e extração dos dados do arquivo CSV.
* **Time**: Utilizado para gerenciar as pausas (delays) necessárias entre as ações do robô e o tempo de carregamento das telas.

---

## 📂 Estrutura dos Arquivos

* `código.py`: É o script principal. Ele contém a lógica de abrir o navegador, fazer login no sistema, ler a base de dados e criar o loop de repetição que cadastra cada produto.
* `position.py`: Script auxiliar rápido que captura e exibe no terminal as coordenadas (X, Y) exatas do mouse na tela. Essencial para mapear onde o robô deve clicar.
* `produtos.csv`: A base de dados contendo as informações (códigos, marcas, tipos, categorias, preços, etc.) que serão inseridas no sistema.

---

## ⚙️ Pré-requisitos e Instalação

Antes de executar o projeto, você precisa ter o Python instalado em sua máquina e instalar as bibliotecas necessárias. Abra o terminal e rode o seguinte comando:

```bash
pip install pyautogui pandas openpyxl
