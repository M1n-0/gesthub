@echo off
set HOSTS_FILE=%SystemRoot%\System32\drivers\etc\hosts

set DOMAINS=flask.gesthub keycloak.gesthub chat.gesthub wekan.gesthub

echo [🔧] Mise à jour de %HOSTS_FILE%

for %%D in (%DOMAINS%) do (
    findstr /C:"%%D" %HOSTS_FILE% >nul
    if errorlevel 1 (
        echo 127.0.0.1 %%D >> %HOSTS_FILE%
        echo [+] Ajouté : %%D
    ) else (
        echo [=] Déjà présent : %%D
    )
)

echo [✅] Terminé.
pause
