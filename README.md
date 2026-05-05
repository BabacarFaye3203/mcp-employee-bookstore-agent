
# mcp-employee-bookstore-agent
### MCP Server for n8n & LangChain Ecosystem

Ce projet implémente un serveur **Model Context Protocol (MCP)** robuste conçu pour étendre les capacités des agents IA. Il permet une intégration fluide entre des outils locaux (gestion d'employés), des bases de données externes (PostgreSQL/MongoDB), et des orchestrateurs comme **n8n** ou des frameworks comme **LangChain**.

## 🏗️ Architecture Technique

Le projet exploite les dernières avancées de l'écosystème IA :
*   **Transport :** Utilisation du transport natif **streamable-http** pour le serveur MCP.
*   **Abstraction :** Emploi de `langchain-mcp-adapters` pour convertir les outils MCP en outils compatibles LangChain.
*   **Modèles Locaux :** Intégration native avec **Ollama** via `langchain-ollama` (ex: Llama 3.2).
*   **Persistance Hybride :** **PostgreSQL** (via SQLAlchemy) pour la gestion RH et **MongoDB** pour le catalogue de livres.

## 📁 Structure du Projet

```text
project/
├── agents/
│   └── agent.py          # API FastAPI + Logique LangChain
├── database/
│   └── database.py       # Config DB PostgreSQL & Modèles ORM
├── data/
│   └── employees.py      # Schémas de données Pydantic
├── mcp_server.py         # Serveur MCP (Tools & Stdio Transport)
├── Dockerfile.api        # Build de l'Agent API
├── Dockerfile.mcp        # Build du Serveur MCP
├── docker-compose.yml    # Orchestration multi-services
└── pyproject.toml        # Configuration UV & Dépendances
```

## 🛠️ Outils à Installer

Avant de commencer, assurez-vous d'avoir installé les outils suivants :
1.  **Python >= 3.12** : Langage de base du projet.
2.  **UV** : Gestionnaire de paquets et d'environnements ultra-rapide.
3.  **Docker & Docker Compose** : Pour le déploiement conteneurisé.
4.  **Ollama** : Pour faire tourner les LLM localement.
5.  **DBeaver ou MongoDB Compass** : Pour visualiser vos bases de données (optionnel).

## 🚀 Démarrage Rapide

### 1. Configuration initiale
```bash
# Cloner le projet
git clone https://github.com/BabacarFaye3203/mcp-employee-bookstore-agent.git
cd mcp-employee-bookstore-agent

# Installer les dépendances localement avec UV
uv sync
```

### 2. Variables d'environnement
Créez un fichier `.env` à la racine :
```env
TAVILY_API_KEY=votre_cle_tavily
```

### 3. Lancement avec Docker (Recommandé)
Pour démarrer l'ensemble de la stack (Bases de données + MCP Server + API Agent) :
```bash
docker-compose up --build
```
*Cette commande lance automatiquement PostgreSQL, MongoDB, le serveur MCP et l'API de l'agent.*

### 4. Utilisation locale (Sans Docker)
Si vous préférez lancer les composants séparément :
*   **Serveur MCP :** `uv run mcp_server.py`
*   **Agent API :** `uv run uvicorn agents.agent:app --port 8000`

## 🧩 Intégration n8n

Dans votre workflow n8n (référence : **n8n.jpg**) :
1.  Ajoutez un nœud **AI Agent**.
2.  Connectez un **Outil MCP** configuré sur `http://localhost:2400/mcp`.
3.  L'agent pourra alors exécuter des fonctions comme `list_employees` ou `get_employee_by_name` directement dans n8n.

## 📦 Dépendances Principales

#### Détail des packages installés :

| Package | Usage |
| :--- | :--- |
| **mcp[cli]** | SDK officiel pour implémenter le Model Context Protocol et outils de test. |
| **langchain-mcp-adapters** | Adaptateur permettant d'utiliser les outils MCP comme des outils LangChain standards. |
| **langchain-ollama** | Connecteur pour l'utilisation de modèles de langage locaux (ex: Llama 3.2). |
| **langchain-tavily** | Intégration de l'outil de recherche web Tavily pour la recherche augmentée. |
| **fastapi & uvicorn** | Framework et serveur pour exposer l'API de l'agent. |
| **sqlalchemy & psycopg2** | ORM et driver pour la communication avec la base de données PostgreSQL. |
| **pydantic** | Validation stricte des schémas de données pour les employés et les outils. |
| **asyncio & dotenv** | Gestion de l'asynchronisme et des variables d'environnement confidentielles. |
| **ipykernel & ipython** | Support pour l'exécution et le test de scripts dans des notebooks Jupyter. |

---

## 📂 Structure des fichiers référencés

*   `inspector.png` : Interface de test pour valider les schémas d'outils.
*   `mongo.png` : Visualisation de la base de données `bookstore` intégrée.
*   `n8n.jpg` : Schéma du workflow d'orchestration de l'agent.
*   `server.jpg` : Logs et exécution du serveur Python en temps réel.

---

**Développé par Babacar Faye**
<img width="1918" height="975" alt="n8n" src="https://github.com/user-attachments/assets/7caabb4e-68b3-4cd4-9eb7-255ee6023abf" />

<img width="1915" height="962" alt="inspector" src="https://github.com/user-attachments/assets/5c152297-943a-47c9-8e55-eab3eab15d13" />




