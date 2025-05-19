# 📘 Gesthub 
<img src="https://img.shields.io/github/last-commit/M1n-0/gesthub?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">  

<em>Construit avec les outils et les technologies nécessaires :</em>
<div style="display: flex; flex-wrap: wrap; gap: 5px;">
   <img src="https://img.shields.io/badge/Flask-000000.svg?style=flat&logo=Flask&logoColor=white" alt="Flask">
   <img src="https://img.shields.io/badge/JSON-000000.svg?style=flat&logo=JSON&logoColor=white" alt="JSON">
   <img src="https://img.shields.io/badge/Keycloak-4D4D4D.svg?style=flat&logo=Keycloak&logoColor=white" alt="Keycloak">
   <img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
   <img src="https://img.shields.io/badge/MariaDB-003545.svg?style=flat&logo=MariaDB&logoColor=white" alt="MariaDB">
   <br>
   <img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
   <img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
   <img src="https://img.shields.io/badge/Mattermost-0058CC.svg?style=flat&logo=Mattermost&logoColor=white" alt="Mattermost">
</div>

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
