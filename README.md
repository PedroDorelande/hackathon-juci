<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-3.1-000000?style=for-the-badge&logo=flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>
  <img src="https://img.shields.io/badge/Chart.js-4.4-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Conclu%C3%ADdo-00b894?style=for-the-badge"/>
</p>

<h1 align="center">👥 CadastroPro</h1>

<p align="center">
  <b>Sistema completo de cadastro de pessoas com interface moderna, dashboard interativo e integração com ViaCEP.</b>
</p>

<p align="center">
  <i>Desenvolvido para o Hackathon JUCI 2026</i>
</p>

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Pré-requisitos](#-pré-requisitos)
- [Como Instalar e Rodar](#-como-instalar-e-rodar)
- [Como Usar o Sistema](#-como-usar-o-sistema)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Diferenciais do Projeto](#-diferenciais-do-projeto)
- [Autor](#-autor)

---

## 💡 Sobre o Projeto

O **CadastroPro** é um sistema web CRUD (Create, Read, Update, Delete) desenvolvido em **Python** com o framework **Flask**. Ele permite o gerenciamento completo de cadastros de pessoas, com uma interface dark mode moderna, responsiva e intuitiva.

O sistema vai além de um CRUD básico, oferecendo funcionalidades inteligentes como **preenchimento automático de endereço via CEP**, **dashboard com gráficos interativos** e **exportação de dados em CSV**.

---

## ✨ Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| ✅ **Cadastrar Pessoa** | Nome completo, CPF, telefone, endereço, cidade, estado e CEP |
| ✅ **Listar Pessoas** | Tabela completa com todos os cadastros organizados |
| ✅ **Editar Cadastro** | Atualização de qualquer dado de uma pessoa |
| ✅ **Excluir Cadastro** | Remoção com confirmação de segurança |
| ✅ **Visualizar Detalhes** | Página dedicada com todas as informações |
| ✅ **Busca Inteligente** | Pesquisa por nome ou CPF em tempo real |
| ✅ **Validação de CPF** | Validação matemática real dos dígitos verificadores |
| ✅ **Máscaras de Input** | Formatação automática de CPF, telefone e CEP |
| 🌟 **Busca por CEP (ViaCEP)** | Preenche endereço, cidade e estado automaticamente |
| 📊 **Dashboard** | Cards de estatísticas + gráfico de cadastros por estado |
| 📁 **Exportar CSV** | Download de todos os cadastros em formato CSV |

---

## 🛠 Tecnologias Utilizadas

### Back-end
- **Python 3.10+** — Linguagem de programação principal
- **Flask 3.1** — Framework web leve e poderoso
- **SQLite** — Banco de dados relacional embutido (sem necessidade de instalação)

### Front-end
- **HTML5** — Estrutura semântica das páginas
- **CSS3** — Estilização com tema dark mode customizado
- **JavaScript** — Máscaras de input, integração ViaCEP e interatividade
- **Chart.js 4.4** — Gráficos interativos no dashboard
- **Font Awesome 6.5** — Ícones profissionais
- **Google Fonts (Inter)** — Tipografia moderna e legível

### API Externa
- **ViaCEP** — API gratuita para consulta de endereços brasileiros por CEP

---

## 📌 Pré-requisitos

Antes de começar, verifique se você possui instalado na sua máquina:

- ✅ **Python 3.10 ou superior** → [Download Python](https://www.python.org/downloads/)
- ✅ **pip** (gerenciador de pacotes do Python — já vem com o Python)
- ✅ **Git** (opcional, para clonar o repositório) → [Download Git](https://git-scm.com/)

Para verificar se o Python está instalado, abra o terminal e digite:

```bash
python --version
```

---

## 🚀 Como Instalar e Rodar

Siga o passo a passo abaixo para rodar o projeto na sua máquina:

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/PedroDorelande/hackathon-juci.git
```

### 2️⃣ Entre na pasta do projeto

```bash
cd hackathon-juci
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

> 💡 **Dica:** Isso irá instalar o Flask e todas as bibliotecas necessárias automaticamente.

### 4️⃣ Execute a aplicação

```bash
python app.py
```

### 5️⃣ Acesse no navegador

Abra o navegador e acesse:

```
http://localhost:5000
```

> 🎉 **Pronto!** O sistema estará rodando e pronto para uso.

### ⚠️ Para parar o servidor

Pressione `Ctrl + C` no terminal.

---

## 📖 Como Usar o Sistema

### 🏠 Página Inicial (Listar)

Ao acessar o sistema, você verá a **lista de todas as pessoas cadastradas**. A partir daqui você pode:
- 🔍 **Buscar** por nome ou CPF na barra de pesquisa
- 👁️ **Visualizar** detalhes clicando no ícone do olho
- ✏️ **Editar** clicando no ícone do lápis
- 🗑️ **Excluir** clicando no ícone da lixeira (com confirmação)

### ➕ Cadastrar Nova Pessoa

1. Clique no botão **"+ Novo"** no menu superior
2. Preencha os campos do formulário:
   - **Nome Completo** (obrigatório)
   - **CPF** (obrigatório — é validado automaticamente)
   - **Telefone** (obrigatório)
   - **CEP** — ao preencher e sair do campo, o endereço é buscado automaticamente!
   - **Endereço** (obrigatório)
   - **Cidade** e **Estado** (preenchidos automaticamente pelo CEP)
3. Clique em **"Cadastrar"**

> 🌟 **Destaque:** O campo CEP usa a **API ViaCEP** — basta digitar o CEP e o endereço, cidade e estado são preenchidos automaticamente!

### 📊 Dashboard

Clique em **"Dashboard"** no menu para ver:
- 📈 **Total de cadastros** no sistema
- 🗺️ **Quantidade de estados** representados
- 🕐 **Últimos cadastros** realizados
- 📊 **Gráfico de barras** mostrando a distribuição por estado

### 📁 Exportar Dados

Clique em **"Exportar"** no menu para baixar um arquivo **CSV** com todos os cadastros. Este arquivo pode ser aberto no **Excel** ou **Google Planilhas**.

---

## 📂 Estrutura do Projeto

```
hackathon-juci/
│
├── app.py                    # Aplicação principal (rotas, lógica, validações)
├── requirements.txt          # Dependências do projeto
├── .gitignore                # Arquivos ignorados pelo Git
├── README.md                 # Este arquivo :)
│
├── static/
│   └── style.css             # Estilização completa (dark mode)
│
├── templates/
│   ├── base.html             # Template base (navbar, footer, layout)
│   ├── index.html            # Página de listagem de pessoas
│   ├── form.html             # Formulário de cadastro/edição
│   ├── visualizar.html       # Página de detalhes da pessoa
│   └── dashboard.html        # Dashboard com gráficos
│
└── pessoas.db                # Banco de dados SQLite (criado automaticamente)
```

---

## 🌟 Diferenciais do Projeto

### 1. 🔍 Integração com ViaCEP
O sistema consulta a API pública **ViaCEP** em tempo real. Ao digitar um CEP válido, os campos de endereço, cidade e estado são preenchidos **automaticamente**, economizando tempo e evitando erros de digitação.

### 2. 📊 Dashboard Interativo
Uma página dedicada com **cards de estatísticas** e um **gráfico de barras** (Chart.js) mostrando a distribuição geográfica dos cadastros. Visualização de dados profissional e dinâmica.

### 3. 📁 Exportação de Dados
Funcionalidade para **exportar todos os cadastros em CSV**, permitindo análise em ferramentas como Excel, Google Sheets ou qualquer software de planilhas.

### 4. ✅ Validação Real de CPF
O CPF não é apenas verificado pelo formato — o sistema calcula os **dígitos verificadores** matematicamente, garantindo que apenas CPFs válidos sejam aceitos.

### 5. 🎨 Interface Premium
Design dark mode moderno com a fonte **Inter**, ícones **Font Awesome**, animações suaves e layout **100% responsivo** (funciona no celular e no desktop).

---

## 👨‍💻 Autor

Desenvolvido com dedicação por **Pedro Dorelande** para o **Hackathon JUCI 2026**.

---

<p align="center">
  <i>"A tecnologia move o mundo." — Steve Jobs</i>
</p>

---

> **P.S.:** Professor **Abraão Henrique**, o senhor é uma pessoa muito legal 
---

<p align="center">
  Feito em Python
</p>
