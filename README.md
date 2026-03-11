

🗳️ Sistema de Enquetes e Votação Online

Sobre o Projeto
O Sistema de Enquetes e Votação Online é uma aplicação web desenvolvida para permitir a criação, gestão e participação em enquetes digitais.
O sistema possibilita que administradores criem enquetes com várias opções de voto, enquanto utilizadores registados podem participar votando de forma simples e segura.
O objetivo principal é garantir:

✔️ Integridade dos votos

✔️ Controle do período de votação

✔️ Um voto por utilizador

✔️ Apresentação clara dos resultados
Este sistema pode ser utilizado em contextos como:
🎓 Instituições educacionais
🏢 Organizações
👥 Votações internas
🚀 Funcionalidades Principais
👤 Para Utilizadores
🔐 Registo e Autenticação
criação de conta
login seguro
🗳️ Participação em Enquetes
votar em enquetes ativas
🚫 Voto Único
apenas um voto por utilizador em cada enquete
📊 Visualização de Resultados
número de votos por opção
percentagem de votos
🛡️ Para Administradores
📝 Criação de Enquetes
criar novas enquetes
⚙️ Gestão de Opções de Voto
adicionar opções
editar opções
remover opções
🕒 Controle do Período de Votação
definir data de início
definir data de encerramento
📈 Acompanhamento dos Resultados
🔐 Segurança e Integridade
O sistema foi desenvolvido com mecanismos para garantir a confiabilidade do processo de votação:
Autenticação de utilizadores
Controle de permissões (Administrador e Utilizador)
Validação automática do período de votação
Bloqueio de votos duplicados
Uso de variáveis de ambiente (.env) para dados sensíveis
⚠️ Este sistema é indicado para votações institucionais ou educacionais, não substituindo eleições oficiais.
🧰 Tecnologias Utilizadas
Camada
Tecnologias
🎨 Frontend
TypeScript, HTML5, CSS3, JavaScript
⚙️ Backend
Django
🗄️ Banco de Dados
MySQL
🔧 Versionamento
Git e GitHub
📂 Estrutura do Projeto
Copiar código

sistema_de_votos



│   ├── frontend
│   ├── backend
│   └── database
│
├── README.md
├── LICENSE
└── .gitignore
⚙️ Instalação do Projeto
1-Clonar o repositório
Bash
Copiar código
git clone https://github.com/sebastiaomassocologabriel-oss/sistema_de_votos
2_Entrar na pasta do projeto
Bash
Copiar código
cd Projecto_Vota_Docs
3- Instalar dependências do backend
Bash
Copiar código
pip install -r requirements.txt
4-Executar o servidor
Bash
Copiar código
python manage.py runserver
📊 Exemplo de Funcionamento
Criação de Enquete
Administrador cria uma enquete com:
título
descrição
opções de voto
data de início
data de fim
Votação
Utilizadores registados podem:
visualizar enquetes ativas
votar apenas uma vez
Resultados
O sistema apresenta:
Opção votos percentagem
A      10    40%

B      15    60%

📂 Estado do Projeto
🚧 Em desenvolvimento
O sistema está a ser desenvolvido e novas funcionalidades estão a ser adicionadas progressivamente.

Contribuição

Sugestões, melhorias ou correções são bem-vindas.
Para contribuir:
Faça um fork do projeto
Crie uma nova branch
Envie um pull request
📄 Licença
Este projeto está sob a licença MIT.
👤 Autor
Grupo 4
🎓 Estudantes de Informática de Gestão
💻 Interessados em desenvolvimento de sistemas web e bases de dados.
