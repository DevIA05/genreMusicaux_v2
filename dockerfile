# Utiliser une image de base avec Python
FROM python:3.10

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY src /app/src
COPY requirements.txt /app/requirements.txt

# Installer les dépendances
RUN pip install -r /app/requirements.txt

# Exposer le port utilisé par Streamlit
EXPOSE 8501

# Commande pour démarrer l'application Streamlit
CMD ["streamlit", "run", "/app/src/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
