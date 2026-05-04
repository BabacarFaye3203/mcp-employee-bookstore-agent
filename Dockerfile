FROM python:3.13-slim

WORKDIR /app

# Installer uv
RUN pip install --no-cache-dir uv

# Copier uniquement les fichiers de dépendances d'abord (cache Docker )
COPY pyproject.toml uv.lock* /app/

# Installer les dépendances
RUN uv sync

# Copier le reste du projet
COPY . /app

# Exposer le port
EXPOSE 8000

# Lancer l'app
CMD ["uv", "run", "uvicorn", "mcp_server:app", "--host", "0.0.0.0", "--port", "8000"]