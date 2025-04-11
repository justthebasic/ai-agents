# 🧠 AI Coding Assistant

This project is a local AI assistant for programming support using [LangChain](https://github.com/langchain-ai/langchain), integrated with **Together AI's free LLaMA-4 model** and useful developer tools like:

- 📚 `documentation_tool`: Extracts and explains content from programming documentation URLs.
- 🧹 `black_formatter_tool`: Formats Python code using [Black](https://github.com/psf/black).

## 🔧 Features

- Uses [Together AI](https://www.together.ai/) instead of OpenAI (no need to pay or worry about rate limits).
- Reads `.env` file for API keys and environment config.
- Uses LangChain's `AgentExecutor` to decide when and how to use tools.
- Modular and easy to extend with more tools.

## 📦 Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-coding-assistant.git
cd ai-coding-assistant
```

### 2. Install dependencies

We use [Poetry](https://python-poetry.org/).

```bash
poetry install
```

### 3. Create a `.env` file

Add your Together API key:

```env
TOGETHER_API_KEY=your_api_key_here
```

You can get your free API key at: [https://together.ai/](https://together.ai/)

### 4. Run the agent

```bash
poetry run python agents.py
```

## 🛠️ Tools included

### 🧾 `documentation_tool(url, question)`

Scrapes and simplifies documentation from a given URL to help answer coding questions.

### 🖤 `black_formatter_tool(path)`

Formats a Python file using `black`. Expects a local file path.

---

## 📚 Example

```python
result = agent_executor.invoke({"input": "Format the file main.py using black."})
print(result['output'])
```

---

## ✅ TODO

- [ ] Add CLI or web interface
- [ ] More tools (test runner, linter, etc.)
- [ ] Automatic code summarization from large files

---

## 📄 License

MIT