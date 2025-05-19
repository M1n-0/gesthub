# 📘 Gesthub 
<img src="https://img.shields.io/github/last-commit/M1n-0/gesthub?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">  

<em>Construit avec les outils et les technologies nécessaires :</em>

<img src="https://img.shields.io/badge/Flask-000000.svg?style=flat&logo=Flask&logoColor=white" alt="Flask">
<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat&logo=JSON&logoColor=white" alt="JSON">
<img src="https://img.shields.io/badge/Keycloak-4D4D4D.svg?style=flat&logo=Keycloak&logoColor=white" alt="Keycloak">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
<img src="https://img.shields.io/badge/MariaDB-003545.svg?style=flat&logo=MariaDB&logoColor=white" alt="MariaDB">
<br>
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Mattermost-0058CC.svg?style=flat&logo=Mattermost&logoColor=white" alt="Mattermost">


## 🧱 Objectif

Créer un site web multi-services (extranet/intranet) avec :
- Authentification centralisée via **Keycloak**
- Reverse proxy **Caddy**
- Frontend/backend **Flask**
- Chat & Gestion de tâches via **Mattermost**
- Gestion d’annonces via JSON avec droits `/admin` (a faire)

---

## 🐳 Démarrage du projet

### 1. **Structure Docker**

Les services sont définis dans `docker-compose.yml` :
- `caddy`: Reverse proxy + HTTPS automatique
- `flask`: Application web backend
- `mariadb`: Base de données
- `keycloak`: SSO + gestion utilisateurs
- `mattermost`: Chat et gestion de tâches (type Trello)

Réseau utilisé : `gesthub_gesthub`

---

## 🔐 Authentification Keycloak

### ✅ Étapes :

1. Création du **realm `Gesthub`**
2. Ajout des clients (Flask et Mattermost)
3. Activation `OpenID Connect`
4. Configuration des **Redirect URIs**
   - Exemples :
     - Flask → `https://dashboard.ninolbt.com/login/callback`
     - Mattermost → `https://mattermost.ninolbt.com/signup/openid/complete`

5. Pour les utilisateurs `/admin`, on utilise le **groupe `/admin`** dans Keycloak.

---

## 🌐 Reverse Proxy Caddy

### 🛠️ `Caddyfile` :

```caddyfile
https://dashboard.ninolbt.com {
    reverse_proxy flask:5000
}

https://keycloak.ninolbt.com {
    reverse_proxy keycloak:8080
}

https://mattermost.ninolbt.com {
    reverse_proxy mattermost:8065
}
```

**Volumes persistants** :  
`caddy_data` et `caddy_config` montés dans `/data` et `/config`

---

## 🧩 Flask 
- back du dashboard
- Permet la création/modification/suppression d’annonces en JSON (en test)
- Accessible uniquement pour les utilisateurs avec le rôle `/admin` (via token) (en test)
- Chargement des assets statiques corrigé avec Caddy

---

## 🗂️ Gestion des droits

- Auth via Keycloak pour Flask, Mattermost, Wekan
- Vérification des groupes dans Flask (`/admin`)
- Redirections correctes avec URLs HTTPS Caddy

---

## 📌 Bugs et corrections

- ⚠️ Redirection Keycloak incorrecte → Corrigé avec bon `redirect_uri`
- ⚠️ Assets statiques Flask → corrigé via URL absolue en HTTPS
- ✅ Reverse proxy fonctionne avec tous les services
- ✅ HTTPS opérationnel via Caddy avec certificats Let's Encrypt

---

## 🚀 Démarrage

```bash
docker compose up --build -d
```

Si besoin :
```bash
docker compose logs -f [service]
```

---

## 📤 Export complet

Pour rendre le projet exportable :
- Tout est containerisé (Docker)
- Config Keycloak exporté (JSON disponible dans le dossier `export_keycloak`)
- `docker-compose.yml`, `Caddyfile`, fichier disponible dans le repo


<!-- BADGES -->

<img src="https://img.shields.io/github/languages/top/M1n-0/gesthub?style=flat&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/M1n-0/gesthub?style=flat&color=0080ff" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Flask-000000.svg?style=flat&logo=Flask&logoColor=white" alt="Flask">
<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat&logo=JSON&logoColor=white" alt="JSON">
<img src="https://img.shields.io/badge/Keycloak-4D4D4D.svg?style=flat&logo=Keycloak&logoColor=white" alt="Keycloak">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
<img src="https://img.shields.io/badge/MariaDB-003545.svg?style=flat&logo=MariaDB&logoColor=white" alt="MariaDB">
<br>
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Mattermost-0058CC.svg?style=flat&logo=Mattermost&logoColor=white" alt="Mattermost">
<img src="https://img.shields.io/badge/bat-31369E.svg?style=flat&logo=bat&logoColor=white" alt="bat">

</div>
<br>

---

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Testing](#testing)
- [Contributing](#contributing)
- [Acknowledgment](#acknowledgment)

---

## Overview

Gesthub is a powerful developer tool designed to streamline the setup and management of full-stack applications by integrating essential services into a cohesive environment.

**Why Gesthub?**

This project simplifies the development process, allowing developers to focus on building features rather than managing infrastructure. The core features include:

- 🚀 **Docker Compose Configuration:** Simplifies orchestration of multiple services, reducing setup complexity.
- 🌐 **Local Domain Management:** Scripts to add local domain entries streamline access to services, enhancing the development experience.
- 🔒 **Integrated User Authentication:** Utilizes Keycloak for secure user management, addressing security concerns.
- ⚙️ **Seamless Routing and Load Balancing:** Caddyfile configuration ensures efficient request handling, improving performance.
- 🎨 **User-Friendly Interface:** Responsive design enhances collaboration and user experience.
- 📊 **Centralized Data Management:** Structured storage for advertisements improves data handling capabilities.

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Shell
- **Package Manager:** Bash
- **Container Runtime:** Docker

### Installation

Build gesthub from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/M1n-0/gesthub
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd gesthub
    ```

3. **Install the dependencies:**

**Using [docker](https://www.docker.com/):**

```sh
❯ docker build -t M1n-0/gesthub .
```
**Using [bash](https://www.gnu.org/software/bash/):**

```sh
❯ chmod +x {entrypoint}
```

### Usage

Run the project with:

**Using [docker](https://www.docker.com/):**

```sh
docker run -it {image_name}
```
**Using [bash](https://www.gnu.org/software/bash/):**

```sh
./{entrypoint}
```

### Testing

Gesthub uses the {__test_framework__} test framework. Run the test suite with:

**Using [docker](https://www.docker.com/):**

```sh
echo 'INSERT-TEST-COMMAND-HERE'
```
**Using [bash](https://www.gnu.org/software/bash/):**

```sh
bats *.bats
```

---

## Contributing

- **💬 [Join the Discussions](https://github.com/M1n-0/gesthub/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/M1n-0/gesthub/issues)**: Submit bugs found or log feature requests for the `gesthub` project.
- **💡 [Submit Pull Requests](https://github.com/M1n-0/gesthub/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/M1n-0/gesthub
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/M1n-0/gesthub/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=M1n-0/gesthub">
   </a>
</p>
</details>

---

## Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="left"><a href="#top">⬆ Return</a></div>

---
