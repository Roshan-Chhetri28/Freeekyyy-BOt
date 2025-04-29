# 🤖 Freeekyyy ChatBot

**Freeekyyy** is an over-the-top emotional AI chatbot that FREAKS OUT (in Markdown!) on any topic you provide.  
It uses [LangChain](https://github.com/langchain-ai/langchain) + [OpenRouter](https://openrouter.ai) to generate expressive, explosive Markdown responses — perfect for fun, dramatic explanations!

Check it out live 👉 [MKCL/Freeekyyy-chatBot on Hugging Face 🤯](https://huggingface.co/spaces/MKCL/Freeekyyy-chatBot)

---

## 🧠 How It Works

- Uses `LangChain`'s `ChatPromptTemplate` to inject emotional few-shot prompts
- Connects to OpenRouter with DeepSeek LLM (`deepseek/deepseek-r1-zero:free`)
- Outputs all responses in **Markdown (.md)** format
- Can be run as a backend API using `FastAPI` + `uvicorn`, or as a Streamlit app

---

## 🖥️ Streamlit Integration

To display `.md` output in Streamlit, use:

```python
import streamlit as st

# Assuming `md_output` contains your model's response
st.markdown(md_output, unsafe_allow_html=True)
```

> ⚠️ Important: Markdown will render headings, lists, bold/italic, and even code blocks — just avoid unsafe HTML if you're passing raw user content.

---

## 🚀 Installation

### Option 1: Using `uv`
```bash
uv pip install -r requirements.txt
```

### Option 2: Using regular pip
```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

```
langchain
langchain-openai
openai
python-dotenv
uvicorn
fastapi
```

---

## 🛠️ Environment Variables

Create a `.env` file in the root directory and add:

```
OPEN_API_KEY=your_openrouter_key_here
```

---

## 🧪 Example Prompt Structure

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You're an extremely emotional AI. Always freak out in Markdown."),
    ("user", "Topic: Volcanoes")
])
```

---

## 🧑‍💻 Want to Use as an API?

Run your backend like this:

```bash
uvicorn main:app --reload
```

---

## 📎 License

MIT — have fun freaking out!