#!/bin/bash

PROJECT_DOMAIN="gesthub"
HOSTS_LINE="127.0.0.1 flask.$PROJECT_DOMAIN wekan.$PROJECT_DOMAIN chat.$PROJECT_DOMAIN"

echo "🔧 Vérification des droits (sudo peut être requis pour modifier /etc/hosts)..."

# Ajout dans /etc/hosts si absent
if ! grep -q "$PROJECT_DOMAIN" /etc/hosts; then
  echo "✅ Ajout de $PROJECT_DOMAIN dans /etc/hosts..."
  echo "$HOSTS_LINE" | sudo tee -a /etc/hosts > /dev/null
else
  echo "✔️ Domaine $PROJECT_DOMAIN déjà présent dans /etc/hosts."
fi

echo "🚀 Lancement des services Docker..."
docker compose up --build
