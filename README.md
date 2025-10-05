# 🔍 React Search Agent (LangChain + Travily Web Search)

### 📂 Branch: `project/react-search-agent`

This branch demonstrates how to build a **Search Agent** using **LangChain**, **React**, and **Pydantic**, integrated with **Travily Web Search API** and **LangSmith tracing**.

---

## 🧠 Overview

The **React Search Agent** performs intelligent web searches using an LLM (`gpt-4`) that:
- Takes user input from a React frontend.
- Processes it through a Pydantic-based input schema.
- Uses **Travily Web Search API** for fetching real-time results.
- Applies reasoning via **React-style Prompt Template** (Input → Thought → Action → Answer).
- Formats structured responses with a Pydantic output model.
- Executes reasoning chain steps using **AgentExecutor** and **RunnableLambda**.
- Traces all steps in **LangSmith** for observability and debugging.

---

## ⚙️ Tech Stack

| Component | Description |
|------------|--------------|
| **Language** | Python 3.9+ |
| **Framework** | LangChain |
| **Model** | OpenAI GPT-4 |
| **Data Models** | Pydantic (Input & Output schemas) |
| **Web Search** | Travily API |
| **Tracing** | LangSmith |
| **Execution** | AgentExecutor + RunnableLambda |
| **Frontend** | React (prompt input + results display) |

---

## 🧩 Architecture Flow

