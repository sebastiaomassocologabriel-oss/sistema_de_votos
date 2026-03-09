# 🗳️ VotaAí — Sistema de Votação Eletrónica

> Projeto Final de Curso | Desenvolvido em VS Code

---

## 📌 O que é o VotaAí?

O **VotaAí** é um sistema de votação eletrónica completo que permite:

- Criar e gerir enquetes (votações)
- Registar e autenticar utilizadores com segurança
- Garantir que cada utilizador vote **apenas uma vez** por enquete
- Ver resultados em tempo real com gráficos e percentagens
- Ter um painel de administração para gerir tudo

O sistema tem dois tipos de utilizadores: **Administrador** (cria e gere enquetes) e **Utilizador** (vota e vê resultados).

---

## 🏗️ Arquitetura do Sistema

O projeto segue a arquitetura **MVC (Model-View-Controller)**:

```
UTILIZADOR (Browser)
       ↓ pede página
  FRONTEND (HTML/CSS/JS)  ← pasta: frontend/
       ↓ chama a API
  BACKEND (Node.js/Express)  ← pasta: backend/
       ↓ lê/escreve dados
  BASE DE DADOS (PostgreSQL)  ← gerida pelo pgAdmin 4
```

---

## 📁 Estrutura de Pastas

```
VotaAí/
│
├── 📂 frontend/                   ← Interface visual (o que o utilizador vê)
│   ├── index.html                  ← Página principal do sistema
│   ├── 📂 css/
│   │   └── style.css               ← Todos os estilos visuais (glassmorphism)
│   ├── 📂 js/
│   │   └── app.js                  ← Toda a lógica do frontend
│   └── 📂 assets/
│       ├── images/                 ← Imagens do projeto
│       └── icons/                  ← Ícones
│
├── 📂 backend/                    ← Servidor e lógica de negócio
│   ├── server.js                   ← Ponto de entrada — inicia o servidor
│   ├── package.json                ← Lista de dependências npm
│   ├── .env.example                ← Modelo do ficheiro de configuração
│   │
│   ├── 📂 config/
│   │   └── database.js             ← Ligação ao PostgreSQL
│   │
│   ├── 📂 routes/                 ← Define os caminhos (URLs) da API
│   │   ├── auth.routes.js          ← /api/auth/login, /api/auth/register
│   │   ├── enquete.routes.js       ← /api/enquetes
│   │   ├── voto.routes.js          ← /api/votos
│   │   ├── resultado.routes.js     ← /api/resultados
│   │   └── utilizador.routes.js    ← /api/utilizadores
│   │
│   ├── 📂 controllers/            ← Lógica de cada rota (o que fazer)
│   │   ├── auth.controller.js      ← Login, registo, logout
│   │   ├── enquete.controller.js   ← Criar, listar, editar, apagar enquetes
│   │   ├── voto.controller.js      ← Registar voto, verificar se votou
│   │   ├── resultado.controller.js ← Calcular resultados e percentagens
│   │   └── utilizador.controller.js← Ver e editar perfil
│   │
│   ├── 📂 models/                 ← Estrutura dos dados (tabelas)
│   │   ├── utilizador.model.js     ← Queries da tabela utilizadores
│   │   └── enquete.model.js        ← Queries das tabelas enquetes/opcoes
│   │
│   └── 📂 middleware/             ← Código que corre antes das rotas
│       └── auth.middleware.js      ← Verifica se o token JWT é válido
│
├── 📂 database/                   ← Scripts SQL para a base de dados
│   ├── 📂 migrations/
│   │   └── 001_criar_tabelas.sql   ← Cria todas as tabelas (executar 1x)
│   └── 📂 seeds/
│       └── dados_exemplo.sql       ← Insere dados de teste
│
├── 📂 docs/                       ← Documentação extra
├── 📂 tests/                      ← Testes automatizados
│
├── .gitignore                      ← Ficheiros ignorados pelo Git/GitHub
└── README.md                       ← Este ficheiro
```

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Para que serve |
|---|---|
| **HTML5** | Estrutura da página web |
| **CSS3** | Estilo visual (design glassmorphism, modo dark/light) |
| **JavaScript (Vanilla)** | Lógica do frontend, chamadas à API |
| **Node.js** | Executar JavaScript no servidor |
| **Express.js** | Framework para criar a API REST |
| **PostgreSQL** | Base de dados relacional |
| **pgAdmin 4** | Interface gráfica para gerir o PostgreSQL |
| **bcrypt** | Encriptar senhas dos utilizadores |
| **JWT** | Autenticação com tokens seguros |
| **dotenv** | Gerir variáveis de ambiente (.env) |
| **Git + GitHub** | Controlo de versões do código |
| **VS Code** | Editor de código |

---

## ⚙️ Como Instalar e Executar

### Pré-requisitos

Instala estas ferramentas antes de começar:

| Ferramenta | Download |
|---|---|
| Node.js (v18+) | https://nodejs.org |
| PostgreSQL + pgAdmin 4 | https://www.postgresql.org |
| Git | https://git-scm.com |
| VS Code | https://code.visualstudio.com |

---

### Passo 1 — Obter o Projeto

```bash
# Clonar do GitHub:
git clone https://github.com/teu-usuario/VotaAi.git

# OU descompactar o ZIP e abrir a pasta no VS Code
```

---

### Passo 2 — Criar a Base de Dados no pgAdmin 4

1. Abre o **pgAdmin 4**
2. Clica com o botão direito em **Databases → Create → Database**
3. Nome: `votaai_db` → clica **Save**
4. Clica com botão direito em `votaai_db` → **Query Tool**
5. Abre o ficheiro `database/migrations/001_criar_tabelas.sql`
6. Cola o conteúdo no Query Tool e clica em **▶ Execute (F5)**
7. *(Opcional)* Faz o mesmo com `database/seeds/dados_exemplo.sql` para ter dados de teste

✅ Deves ver a mensagem: *"Tabelas criadas com sucesso!"*

---

### Passo 3 — Configurar o Backend

Abre o **terminal do VS Code** (`Ctrl + '`) e executa:

```bash
# Entrar na pasta do backend
cd backend

# Instalar todas as dependências
npm install

# Criar o ficheiro de configuração
copy .env.example .env
```

Abre o ficheiro `.env` e preenche com os teus dados do PostgreSQL:

```env
PORT=3000
DB_HOST=localhost
DB_PORT=5432
DB_NAME=votaai_db
DB_USER=postgres
DB_PASSWORD=COLOCA_AQUI_A_TUA_SENHA_DO_POSTGRES
JWT_SECRET=votaai_chave_secreta_2024
```

---

### Passo 4 — Iniciar o Servidor

```bash
# Dentro da pasta backend/, executa:
npm start
```

Se tudo estiver correto, vais ver:

```
===========================================
   VotaAí - Servidor iniciado com sucesso
   URL: http://localhost:3000
   API: http://localhost:3000/api
===========================================
✅ Conectado ao PostgreSQL com sucesso!
```

---

### Passo 5 — Abrir o Frontend

**No VS Code:**
1. Instala a extensão **Live Server** (se não tiveres)
2. Clica com botão direito em `frontend/index.html`
3. Seleciona **"Open with Live Server"**
4. O browser abre em `http://localhost:5500` ✅

---

### Contas de Acesso (dados de exemplo)

| Tipo | Email | Senha |
|---|---|---|
| **Admin** | admin@votaai.com | admin123 |
| **Utilizador** | user@votaai.com | user123 |

---

## 🔌 API REST — Endpoints Disponíveis

### Autenticação (`/api/auth`)
| Método | URL | Descrição |
|---|---|---|
| POST | `/api/auth/register` | Criar nova conta |
| POST | `/api/auth/login` | Entrar (recebe token JWT) |
| POST | `/api/auth/logout` | Sair |

### Enquetes (`/api/enquetes`)
| Método | URL | Quem pode usar |
|---|---|---|
| GET | `/api/enquetes` | Todos |
| GET | `/api/enquetes/:id` | Todos |
| POST | `/api/enquetes` | Só admin |
| PUT | `/api/enquetes/:id` | Só admin |
| DELETE | `/api/enquetes/:id` | Só admin |

### Votação (`/api/votos`)
| Método | URL | Descrição |
|---|---|---|
| POST | `/api/votos` | Registar voto |
| GET | `/api/votos/meu/:pollId` | Verificar se já votou |

### Resultados (`/api/resultados`)
| Método | URL | Descrição |
|---|---|---|
| GET | `/api/resultados/:pollId` | Ver resultados com % |

> **Como usar rotas protegidas:** Enviar o token no header:
> `Authorization: Bearer <token_recebido_no_login>`

---

## 🗄️ Diagrama da Base de Dados

```
┌─────────────────────┐       ┌──────────────────────┐
│     utilizadores    │       │       enquetes        │
├─────────────────────┤       ├──────────────────────┤
│ id (PK)             │       │ id (PK)              │
│ name                │◄──────│ created_by (FK)      │
│ email (UNIQUE)      │       │ title                │
│ password (hash)     │       │ description          │
│ role (user/admin)   │       │ start_date           │
│ avatar_color        │       │ end_date             │
│ created_at          │       │ created_at           │
└─────────────────────┘       └──────────────────────┘
          │                              │
          │                              │ 1:N
          │                    ┌─────────▼──────────┐
          │                    │       opcoes        │
          │                    ├────────────────────┤
          │                    │ id (PK)            │
          │                    │ poll_id (FK)       │
          │                    │ text               │
          │                    └────────────────────┘
          │                              │
          │ 1:N                          │ N:1
          │        ┌─────────────────────▼──────────┐
          │        │            votos               │
          │        ├────────────────────────────────┤
          └───────►│ user_id (FK)                   │
                   │ poll_id (FK)                   │
                   │ option_id (FK)                 │
                   │ created_at                     │
                   │ UNIQUE(poll_id, user_id) ← 1 voto só! │
                   └────────────────────────────────┘
```

---

## 🔒 Segurança do Sistema

| Medida | Como funciona |
|---|---|
| **Senhas encriptadas** | bcrypt transforma a senha num hash de 60 caracteres. Mesmo que alguém aceda à BD, não consegue ler as senhas. |
| **Autenticação JWT** | Após login, o servidor gera um token assinado. Sem ele, não é possível aceder a rotas protegidas. |
| **1 voto por utilizador** | A tabela `votos` tem `UNIQUE(poll_id, user_id)` — a própria base de dados rejeita segundos votos. |
| **Roles (admin/user)** | O middleware `verificarAdmin` bloqueia utilizadores normais de aceder a funções de administração. |
| **Variáveis de ambiente** | Senhas e chaves secretas ficam no `.env` (nunca no código ou no GitHub). |

---

## 🐛 Problemas Comuns e Soluções

**❌ "Cannot connect to PostgreSQL"**
→ Verifica se o PostgreSQL está a correr no pgAdmin 4 e se a senha no `.env` está correta.

**❌ "Port 3000 already in use"**
→ Muda `PORT=3001` no `.env` e tenta de novo.

**❌ "Cannot find module"**
→ Certifica-te de que executaste `npm install` dentro da pasta `backend/`.

**❌ O browser abre mas diz "Cannot GET /"**
→ Usa o Live Server do VS Code para abrir o `frontend/index.html`.

**❌ "node não é reconhecido como comando"**
→ O Node.js não está instalado. Instala em https://nodejs.org

---

## 👤 Autor

Desenvolvido como projeto final de curso.

**Ferramentas:** VS Code · Node.js · PostgreSQL · pgAdmin 4 · Git · GitHub · HTML · CSS · JavaScript
