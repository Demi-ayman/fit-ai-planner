# 🏋️‍♂️ ProFit AI: Personal Health & Macro Planner

A full-stack AI application that delivers personalized fitness coaching and precision nutritional targeting. This project uses a **FastAPI** backend to orchestrate specialized AI workflows built in **Langflow**, visualized through a reactive **Streamlit** dashboard.

## 🧠 Core Features

### 1. AskAiV2 (The Virtual Coach)
* **Natural Language Interaction:** Processes user physical profiles and fitness queries.
* **Smart Routing:** Uses a Conditional Router to distinguish between general advice and logical queries.
* **Accuracy:** Automatically triggers a **Calculator Tool** for math-intensive questions (like BMI or protein ratios) to ensure data accuracy.

### 2. Macro Flow (The Precision Nutritionist)
* **Deterministic Logic:** Calculates exact daily targets for Calories, Protein, Carbohydrates, and Fats based on biometrics and specific goals.
* **Structured Data:** Returns results in valid **JSON format**, allowing for seamless integration with frontend visualizations and charts.

## 🛠️ Tech Stack
* **Frontend:** Streamlit (Python)
* **Backend:** FastAPI (Python)
* **AI Orchestration:** Langflow
* **LLMs:** Google Gemini 2.5 (Flash & Lite)
* **Tools:** LangChain Tool-Calling, AstraDB

## 🚀 Getting Started

1. **Clone the repo:** `git clone https://github.com/Demi-ayman/fit-ai-planner.git`
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Set up Environment:** Create a `.env` file with your `API_KEY`.
4. **Run Backend:** `uvicorn ai:app --reload`
5. **Run Frontend:** `streamlit run app.py`
