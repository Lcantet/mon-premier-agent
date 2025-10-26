# 🤖 Mon Premier Agent Conversationnel

Un agent conversationnel intelligent utilisant Google Gemini AI. Cet agent maintient l'historique de vos conversations et fournit des réponses contextuelles.

## ✨ Fonctionnalités

- 💬 Interface conversationnelle en ligne de commande
- 🧠 Utilise le modèle Google Gemini Pro
- 📝 Maintient l'historique complet de la conversation
- 🔐 Gestion sécurisée des clés API via fichier .env
- 🎯 Simple à utiliser et à configurer

## 📋 Prérequis

- Python 3.8 ou supérieur
- Un compte Google Cloud avec accès à l'API Gemini
- Une clé API Google AI Studio

## 🚀 Installation

### 1. Cloner le repository

```bash
git clone https://github.com/Lcantet/mon-premier-agent.git
cd mon-premier-agent
```

### 2. Créer un environnement virtuel (recommandé)

```bash
# Sur Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Sur Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

## 🔑 Configuration

### 1. Obtenir une clé API Google

1. Rendez-vous sur [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Connectez-vous avec votre compte Google
3. Créez une nouvelle clé API
4. Copiez la clé générée

### 2. Configurer le fichier .env

```bash
# Copier le fichier exemple
cp .env.example .env
```

Ouvrez le fichier `.env` et remplacez `votre_cle_api_ici` par votre véritable clé API :

```env
GOOGLE_API_KEY=AIzaSy...
```

⚠️ **Important** : Ne partagez jamais votre fichier `.env` ou votre clé API !

## 💻 Utilisation

### Lancer l'agent

```bash
python agent.py
```

### Exemple de conversation

```
============================================================
🤖 Agent Conversationnel Gemini
============================================================
Tapez 'quit' ou 'exit' pour quitter.
============================================================

Vous: Bonjour ! Comment vas-tu ?

🤖 Agent: Bonjour ! Je vais très bien, merci de demander. 
En tant qu'IA, je n'ai pas d'émotions au sens humain, 
mais je suis opérationnel et prêt à vous aider. 
Comment puis-je vous assister aujourd'hui ?

Vous: Peux-tu m'expliquer ce qu'est un agent conversationnel ?

🤖 Agent: Bien sûr ! Un agent conversationnel, aussi appelé 
chatbot ou assistant virtuel, est un programme informatique 
conçu pour simuler une conversation avec des utilisateurs humains...

Vous: quit

👋 Au revoir !
```

### Commandes disponibles

- Tapez votre message et appuyez sur Entrée pour converser
- Tapez `quit`, `exit` ou `q` pour quitter l'application
- Appuyez sur `Ctrl+C` pour interrompre à tout moment

## 📁 Structure du projet

```
mon-premier-agent/
│
├── agent.py              # Code principal de l'agent
├── requirements.txt      # Dépendances Python
├── .env.example         # Template pour les variables d'environnement
├── .gitignore           # Fichiers à ignorer par Git
└── README.md            # Documentation (ce fichier)
```

## 🛠️ Personnalisation

### Changer le modèle Gemini

Dans `agent.py`, vous pouvez modifier la ligne :

```python
model = genai.GenerativeModel('gemini-pro')
```

Par un autre modèle disponible :
- `gemini-pro` : Modèle de texte performant
- `gemini-pro-vision` : Pour le traitement d'images

### Modifier les paramètres de génération

Vous pouvez ajouter des paramètres de configuration :

```python
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

model = genai.GenerativeModel(
    'gemini-pro',
    generation_config=generation_config
)
```

## 🐛 Résolution des problèmes

### Erreur : GOOGLE_API_KEY non trouvée

- Vérifiez que le fichier `.env` existe dans le répertoire du projet
- Vérifiez que la clé API est correctement définie dans `.env`
- Assurez-vous qu'il n'y a pas d'espaces autour du signe `=`

### Erreur d'API

- Vérifiez que votre clé API est valide
- Assurez-vous d'avoir activé l'API Gemini dans Google Cloud
- Vérifiez votre connexion Internet

### Erreur d'importation

- Assurez-vous d'avoir installé toutes les dépendances : `pip install -r requirements.txt`
- Vérifiez que vous utilisez le bon environnement virtuel

## 📚 Ressources

- [Documentation Google Gemini](https://ai.google.dev/docs)
- [Google AI Studio](https://makersuite.google.com/)
- [API Reference](https://ai.google.dev/api/python/google/generativeai)

## 📄 Licence

Ce projet est open source et disponible sous licence MIT.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

## ✉️ Contact

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue sur GitHub.

---

**Développé avec ❤️ par Lcantet**
