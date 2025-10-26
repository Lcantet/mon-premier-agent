#!/usr/bin/env python3
"""
Agent conversationnel utilisant Google Gemini AI.
Cet agent maintient l'historique de conversation et permet une interaction en ligne de commande.
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv


def main():
    """Point d'entrée principal de l'agent conversationnel."""
    # Charger les variables d'environnement depuis le fichier .env
    load_dotenv()
    
    # Récupérer la clé API
    api_key = os.getenv('GOOGLE_API_KEY')
    
    if not api_key:
        print("❌ Erreur: GOOGLE_API_KEY non trouvée dans le fichier .env")
        print("Veuillez créer un fichier .env avec votre clé API Google.")
        return
    
    # Configurer l'API Google Generative AI
    genai.configure(api_key=api_key)
    
    # Initialiser le modèle Gemini
    model = genai.GenerativeModel('gemini-pro')
    
    # Démarrer une session de chat avec historique
    chat = model.start_chat(history=[])
    
    print("="*60)
    print("🤖 Agent Conversationnel Gemini")
    print("="*60)
    print("Tapez 'quit' ou 'exit' pour quitter.")
    print("="*60)
    print()
    
    # Boucle de conversation
    while True:
        try:
            # Obtenir l'entrée utilisateur
            user_input = input("Vous: ").strip()
            
            # Vérifier si l'utilisateur veut quitter
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Au revoir !")
                break
            
            # Ignorer les entrées vides
            if not user_input:
                continue
            
            # Envoyer le message et obtenir la réponse
            print("\n🤖 Agent: ", end="", flush=True)
            response = chat.send_message(user_input)
            print(response.text)
            print()
            
        except KeyboardInterrupt:
            print("\n\n👋 Au revoir !")
            break
        except Exception as e:
            print(f"\n❌ Erreur: {e}")
            print("Veuillez réessayer.\n")


if __name__ == "__main__":
    main()
