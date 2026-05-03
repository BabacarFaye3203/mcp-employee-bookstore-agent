
# mcp-employee-bookstore-agent (MCP Server for n8n & LangChain Ecosystem)

Ce projet implémente un serveur **Model Context Protocol (MCP)** robuste conçu pour étendre les capacités des agents IA. Il permet une intégration fluide entre des outils locaux (gestion d'employés), des bases de données externes, et des orchestrateurs comme **n8n** ou des frameworks comme **LangChain**.

## 🏗️ Architecture Technique

Le projet exploite les dernières avancées de l'écosystème IA :
*   **Transport :** Utilisation de `FastAPI` et `Uvicorn` pour un transport via SSE (Server-Sent Events), permettant une communication asynchrone fiable entre le client et le serveur.
*   **Abstraction :** Utilisation de `langchain-mcp-adapters` pour convertir facilement les outils MCP en outils compatibles avec les agents LangChain.
*   **Modèles Locaux :** Intégration native avec `Ollama` via `langchain-ollama` pour l'exécution locale de modèles comme Llama 3.2.
*   **Recherche Augmentée :** Support de `langchain-tavily` pour fournir des capacités de recherche web en temps réel à l'agent.

---

## 🛠️ Installation

Le projet utilise `uv` pour une gestion optimale des dépendances et de l'environnement Python.

### Prérequis
*   Python **>= 3.12**
*   [Ollama](https://ollama.com/) installé et configuré.Ou un LLM de votre choix
*   [n8n](https://n8n.io/) (version auto-hébergée recommandée pour l'utilisation locale).

### Configuration
1. Clonez le dépôt :
   ```bash
   git clone <url-du-repo>
   cd mcp-employee-bookstore-agent
   ```

2. Installez les dépendances :
   
```bash
   uv sync
   ```

3. Configurez vos variables d'environnement dans un fichier `.env` :
   ```env
   TAVILY_API_KEY=votre_cle_ici
   API_KEY=si non Ollama
   ```

---

## 🚀 Utilisation

### Lancer le serveur MCP
Pour exposer vos outils à n8n ou à l'inspecteur MCP :
```bash
uv run uvicorn mcp_server:app --port 2400
```

### Intégration n8n
Dans votre workflow n8n (voir `n8n.jpg`), utilisez le nœud **AI Agent** :
1.  Ajoutez un outil **MCP Tool**.
2.  Configurez l'URL vers `http://localhost:2400/mcp`.
3.  L'agent détectera automatiquement les fonctions comme `list_employees` ou `get_employee_by_name`.

---

## 📦 Dépendances Principales

| Package | Usage |
| :--- | :--- |
| `fastapi` | Interface API pour le transport MCP. |
| `langchain-mcp-adapters` | Pont entre le protocole MCP et l'écosystème LangChain. |
| `langchain-ollama` | Connecteur pour les modèles LLM locaux. |
| `mcp[cli]` | SDK officiel du Model Context Protocol. |
| `pydantic` | Validation stricte des schémas de données des outils. |

---

## 📂 Structure des fichiers référencés

*   `inspector.png` : Interface de test pour valider les schémas d'outils.
*   `mongo.png` : Visualisation de la base de données `bookstore` intégrée.
*   `n8n.jpg` : Schéma du workflow d'orchestration de l'agent.
*   `server.jpg` : Logs et exécution du serveur Python en temps réel.

---

**Développé par Babacar Faye**
<img width="1918" height="975" alt="n8n" src="https://github.com/user-attachments/assets/7caabb4e-68b3-4cd4-9eb7-255ee6023abf" />
<img width="1918" height="981" alt="inspector" src="https://github.com/user-attachments/assets/a71f3c41-0ed9-42b1-9e0c-4b0f7ba9ca0f" />
<img width="1896" height="437" alt="tavily" src="https://github.com/user-attachments/assets/9449cbbc-0f62-451e-b4af-b0b657fd39c5" />



