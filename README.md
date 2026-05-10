#  BuddyBot

> A friendly conversational AI assistant built with LangChain, Hugging Face, and Streamlit.

---

## ✨ Overview

BuddyBot is a lightweight, interactive chatbot that brings together the power of **LangChain**'s conversational chains, **Hugging Face**'s open-source language models, and **Streamlit**'s rapid UI capabilities — all in one clean, easy-to-run application.

Whether you're exploring conversational AI or building a quick prototype, BuddyBot gives you a solid starting point with minimal setup.

---

## 🚀 Features

- 💬 **Conversational memory** — BuddyBot remembers the context of your conversation within a session
- 🤗 **Hugging Face model integration** — Powered by open-source LLMs via the Hugging Face Hub
- 🔗 **LangChain backbone** — Uses LangChain's chain abstractions for clean, modular conversation handling
- 🖥️ **Streamlit UI** — Simple, browser-based chat interface that's ready to run instantly
- ⚡ **Lightweight & hackable** — Easy to extend with new models, memory types, or UI features

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend / UI | [Streamlit](https://streamlit.io/) |
| LLM Orchestration | [LangChain](https://www.langchain.com/) |
| Language Model | [Hugging Face Hub](https://huggingface.co/) |
| Language | Python 3.9+ |

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/buddybot.git
cd buddybot
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token_here
```

> Get your free API token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

---

## ▶️ Running the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 🗂️ Project Structure

```
buddybot/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment variables
```

---

## 🧩 Requirements

```txt
streamlit
langchain
langchain-community
huggingface-hub
python-dotenv
```

---

## 🔧 Configuration

You can swap out the underlying model by changing the `repo_id` in `bot/chain.py`:

```python
llm = HuggingFaceHub(
    repo_id="google/gemma-2-2B-t",   # Change this to any HF model
    model_kwargs={"temperature": 0.7, "max_length": 512}
)
```

Some recommended models to try:
- `google/flan-t5-large`
- `mistralai/Mistral-7B-Instruct-v0.1`
- `tiiuae/falcon-7b-instruct`

---

## 🛣️ Roadmap

- [ ] Add persistent conversation history across sessions
- [ ] Support multiple model providers (OpenAI, Cohere, etc.)
- [ ] Add user authentication
- [ ] Deploy to Streamlit Cloud / HuggingFace Spaces
- [ ] Customizable system prompt via UI

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

<p align="center">Made with ❤️ and a lot of tokens</p>
