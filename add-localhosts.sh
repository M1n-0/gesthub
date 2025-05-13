#!/bin/bash

HOSTS_FILE="/etc/hosts"
DOMAINS=("flask.localhost" "keycloak.localhost" "chat.localhost" "wekan.localhost")

echo "[🔧] Mise à jour de : $HOSTS_FILE"

for domain in "${DOMAINS[@]}"; do
  if grep -q "$domain" "$HOSTS_FILE"; then
    echo "[=] Déjà présent : $domain"
  else
    echo "127.0.0.1 $domain" | sudo tee -a "$HOSTS_FILE" > /dev/null
    echo "[+] Ajouté : $domain"
  fi
done

echo "[✅] Terminé."
