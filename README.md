# AI SIDEKICK ASSISTANT
⚠️  experimental project


## Description

**FR**  
AI-Sidekick est un assistant IA expérimental reposant sur l’architecture Langraph, qui organise le raisonnement en graphes composés de nodes et de edges, orchestrés via des supersteps. Il combine plusieurs technologies avancées pour offrir une expérience d’assistance complète : recherche web via Serper, navigation automatisée avec Playwright, exécution de code Python, gestion de fichiers locaux, consultation d’emails Gmail, et accès à la base de connaissances de Wikipedia. Grâce au pattern Evaluator, chaque réponse est évaluée selon des critères de succès précis, assurant la pertinence et la qualité avec la capacité pour l’agent de s’autoévaluer et de s’auto-corriger de manière autonome en cas d’erreur. 
⚠️ Ce projet est expérimental et sans guardrails, à utiliser prudemment.

**EN**  
AI-Sidekick is an experimental AI assistant built on the Langraph architecture, organizing reasoning as structured graphs through supersteps. It integrates multiple technologies to provide versatile assistance, including web search, code execution, file management, and email access. The project employs a response evaluation system to ensure quality, with the agent capable of self-assessing and autonomously correcting itself when mistakes occur.  
⚠️ This project is experimental, without safeguards, and should be used with caution.

---

## Fonctionnalités / Features
**FR** 
- 🧠 **Langraph** : gestion du raisonnement par graphes et supersteps.  
- 🔍 **Serper** : moteur de recherche web intégré.  
- 🌐 **Playwright** : navigation automatisée et contrôle du navigateur.  
- 📲 **Notifications mobiles** : envoi d’alertes sur téléphone.  
- 📂 **Gestion de fichiers** : création et modification de fichiers locaux.  
- 🐍 **PythonREPL** : exécution dynamique de code Python 
(⚠️ Le PythonREPL vous donne le pouvoir d’exécuter du code Python directement, ce qui peut être risqué. Si ça vous inquiète, mieux vaut désactiver cet outil. Mais si vous faites attention, tout ira bien !).  
- ✉️ **Gmail via Langchain Google Community** : accès et lecture des emails.  
- 📚 **Wikipedia API** : consultation directe de Wikipedia.  
- ✅ **Evaluator Pattern** : validation des réponses selon des critères précis mettant en lumière la capacité de l’IA à s’auto-évaluer et à s’ajuster intelligemment en cas d’erreurs.

---
**EN** 
- 🧠 **Langraph**: reasoning management via graphs and supersteps.  
- 🔍 **Serper**: integrated web search engine.  
- 🌐 **Playwright**: automated browsing and browser control.  
- 📲 **Mobile notifications**: alerts sent to your phone.  
- 📂 **File management**: creation and editing of local files.  
- 🐍 **PythonREPL**: dynamic Python code execution (use with caution).  
⚠️ PythonREPL lets you run Python code directly, which can be risky. If that makes you uneasy, it’s better to disable this tool. But if you’re careful, everything should be just fine!
- ✉️ **Gmail via Langchain Google Community**: access and read emails.  
- 📚 **Wikipedia API**: direct consultation of Wikipedia.  
- ✅ **Evaluator Pattern**: response validation based on clear criteria showcasing the AI’s ability to self-assess and intelligently adjust when errors occur.

---

## Demo

You can see a demo of the AI Sidekick Assistant in action here:  
[AI Sidekick Assistant Demo Video](https://drive.google.com/file/d/1q4y5yFmMHtf4N3U7WncXWXR6v8bpbm9k/view)  

This demo showcases the assistant performing tasks such as web scraping with Playwright, summarizing search results, writing markdown files, and sending emails automatically.

---

## Installation & Running 🚀

1. **Prepare environment variables**  
   Duplicate the `.env.example` file and rename it to `.env`. Then, fill in your API keys and configuration values. 

 The main environment variables you need to provide are:

OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
PUSHOVER_USER=your_pushover_user_key_here
PUSHOVER_TOKEN=your_pushover_token_here
HF_TOKEN=your_huggingface_token_here
RESEND_API_KEY=your_resend_api_key_here
SERPER_API_KEY=your_serper_api_key_here

LANGSMITH_TRACING=true_or_false
LANGSMITH_ENDPOINT=your_langsmith_endpoint_here
LANGSMITH_API_KEY=your_langsmith_api_key_here
LANGSMITH_PROJECT=your_langsmith_project_name_here


 **Set up Gmail credentials**  
To enable Gmail integration, you need to create a `credentials.json` file with your Google API client secrets.  
- Follow Google's official guide to create your OAuth 2.0 client ID for a desktop application:  
  [Gmail API Quickstart](https://developers.google.com/workspace/gmail/api/quickstart/python?hl=en#authorize_credentials_for_a_desktop_application)  
- Download the `credentials.json` file and place it in the root of your project.  
- Make sure the Gmail API is enabled in your Google Cloud Console.

**Set up Langsmith Keys**
Langsmith enables tracing, monitoring, and debugging of your AI workflows, which is essential for effective evaluation and logging within this project.

- Sign up at [Langchain Langsmith](https://www.langchain.com/langsmith) then create API KEY and copy all environment variables then paste it in the .env 



If you do not intend to use Gmail or Langsmith features, you can skip the Gmail credentials and Langsmith setup steps, but make sure your `.env` file includes all required keys for the features you do plan to use.

---

2. **Install dependencies**  

This project uses `uv` from Astral (https://docs.astral.sh/uv/guides/install-python/).  
Run `uv sync` to install all required dependencies and set up the environment.

---

3. **Run the App**

`uv run main.py`
The local Url where the app is running will be showed in the terminal.
