#  Portal Escolar com Flask

> Um portal web completo e moderno construído com Flask para gestão de anúncios e comunicação em um ambiente escolar.

Este projeto foi desenvolvido como uma solução robusta para comunicação interna, permitindo a criação de posts, gestão de usuários e exibição de anúncios fixos, com uma arquitetura serverless pronta para produção.

---

### 🖼️ Visualização


![Screenshot do Projeto](.//escolaJAC/screenshots/image.png)

---

## 📋 Índice

* [Sobre o Projeto](#-sobre-o-projeto)
* [Funcionalidades](#-funcionalidades)
* [Stack de Tecnologia](#-stack-de-tecnologia)
* [Agradecimentos](#-agradecimentos)

---

## 📖 Sobre o Projeto

O Portal Escolar é uma aplicação full-stack que serve como um quadro de avisos digital. Ele permite que usuários autorizados (professores, administradores) publiquem anúncios, que podem ser visualizados por todos os membros da comunidade escolar. O sistema conta com autenticação de usuários, perfis, e uma funcionalidade para fixar anúncios importantes, garantindo que a informação mais relevante esteja sempre em destaque.

O projeto foi construído do zero usando Python e o microframework Flask, e foi implantado na plataforma serverless Vercel, utilizando um banco de dados PostgreSQL na nuvem e armazenamento de imagens no Cloudinary.

---

## ✨ Funcionalidades

* ✅ **Sistema de Autenticação Completo:** Registro, Login e Logout.
* 🔑 **Registro Seguro por Chave Única:** Apenas usuários com uma chave secreta podem se registrar.
* 👤 **Gestão de Contas de Usuário:** Atualização de perfil com troca de foto.
* 📝 **CRUD de Publicações:** Usuários logados podem criar, visualizar, atualizar e deletar seus próprios posts.
* 📌 **Anúncios Fixos:** Funcionalidade para administradores fixarem posts importantes, que aparecem em destaque em todas as páginas.
* 🖼️ **Upload de Imagens na Nuvem:** As imagens de perfil e dos posts são enviadas para o Cloudinary, otimizando o carregamento e o armazenamento.
* 📧 **Reset de Senha por E-mail:** Funcionalidade para recuperação de senha de forma segura.
* 📱 **Design Responsivo:** Interface adaptável para desktops e dispositivos móveis graças ao Bootstrap 5.

---

## 🛠️ Stack de Tecnologia


#### 🎨 **Frontend:**
* **HTML5 / CSS3**
* **Bootstrap 5:** Framework CSS para estilização e responsividade.
* **Jinja2:** Motor de templates para renderização dinâmica do HTML no servidor.

#### ⚙️ **Backend:**
* **Python:** Linguagem de programação principal.
* **Flask:** Microframework web para a lógica da aplicação.
* **Flask-SQLAlchemy:** ORM para interação com o banco de dados.
* **Flask-Migrate (Alembic):** Para gerenciamento de migrações de schema do banco de dados.
* **Flask-Login:** Para gerenciamento de sessões de usuários.
* **Flask-WTF:** Para criação e validação de formulários.
* **Flask-Bcrypt:** Para criptografia de senhas.
* **Flask-Mail:** Para envio de e-mails.

#### 🗃️ **Banco de Dados:**
* **PostgreSQL (Produção):** Banco de dados relacional robusto.
* **SQLite (Desenvolvimento):** Banco de dados local para testes.

#### 🚀 **Infraestrutura e Deploy:**
* **Vercel:** Plataforma de hospedagem serverless.
* **Git & GitHub:** Para controle de versão e integração contínua.

#### ☁️ **Serviços Externos:**
* **Neon:** Provedor do banco de dados PostgreSQL serverless.
* **Cloudinary:** Serviço de nuvem para armazenamento e otimização de imagens.

---




## 🙏 Agradecimentos

Este projeto é o resultado de um esforço colaborativo e não teria sido possível sem a dedicação e contribuição dos seguintes membros da equipe:

* Pedro Henrique
* Kueren Hazlen
* André
* Luann
* Tarcisio
* Danilo
* Guilherme Monteiro Duarte
* Thiago Andrade
* João Gabriel

Desenvolvido por **Emídio** - [GitHub](https://github.com/emid1-o)