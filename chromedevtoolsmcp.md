# Chrome Headless avec MCP sur WSL - Guide d'installation

## 1. Prérequis système

### Installation de Node.js et npm

```bash
sudo apt update
sudo apt install -y nodejs npm
```

### Vérification des versions

```bash
node --version
npm --version
```

### Installation de la bibliothèque audio ALSA

```bash
sudo apt install -y libasound2t64
```

## 2. Installation de Chrome

### Téléchargement et extraction

```bash
npx @puppeteer/browsers install chrome@stable
```

## 3. Tests de Chrome Headless

### Test basique

```bash
/home/hedredo/chrome/chrome/linux-142.0.7444.61/chrome-linux64/chrome --headless --disable-gpu --no-sandbox
```

### Test avec remote debugging

```bash
/home/hedredo/chrome/chrome/linux-142.0.7444.61/chrome-linux64/chrome \
  --headless \
  --disable-gpu \
  --no-sandbox \
  --remote-debugging-port=9222 \
  --disable-dev-shm-usage
```

### Test de navigation

```bash
/home/hedredo/chrome/chrome/linux-142.0.7444.61/chrome-linux64/chrome \
  --headless \
  --disable-gpu \
  --no-sandbox \
  --remote-debugging-port=9222 \
  'https://www.google.com'
```

## 4. Configuration MCP pour VSCode

### Localisation du fichier mcp.json

```bash
find ~/.vscode-server -name "mcp.json" -type f 2>/dev/null
```

Chemins possibles :
- `~/.vscode-server/data/User/mcp.json`
- `~/.vscode-server/extensions/*/resources/mcp/mcp.json`

### Contenu du fichier mcp.json

```json
{
  "servers": {
    "chrome-devtools": {
      "type": "stdio",
      "command": "npx",
      "args": [
        "chrome-devtools-mcp@latest",
        "--executablePath",
        "/home/hedredo/chrome/chrome/linux-142.0.7444.61/chrome-linux64/chrome",
        "--no-sandbox",
        "--headless",
        "--disable-setuid-sandbox",
        "--disable-gpu",
        "--disable-dev-shm-usage"
      ],
      "env": {}
    }
  }
}
```

### Création du fichier

```bash
mkdir -p ~/.vscode-server/data/User
cat > ~/.vscode-server/data/User/mcp.json << 'EOF'
{
  "servers": {
    "chrome-devtools": {
      "type": "stdio",
      "command": "npx",
      "args": [
        "chrome-devtools-mcp@latest",
        "--executablePath",
        "/home/hedredo/chrome/chrome/linux-142.0.7444.61/chrome-linux64/chrome",
        "--no-sandbox",
        "--headless",
        "--disable-setuid-sandbox",
        "--disable-gpu",
        "--disable-dev-shm-usage"
      ],
      "env": {}
    }
  }
}
EOF
```

## 5. Activation dans VSCode

### Rechargement de la fenêtre

- Ouvrir la palette de commandes : `Ctrl+Shift+P`
- Exécuter : `Developer: Reload Window`

### Vérification

Les outils Chrome DevTools MCP doivent être disponibles dans GitHub Copilot après le rechargement.
