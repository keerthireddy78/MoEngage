# MoEngage
AI-Powered Documentation Improvement Agent

Overview
This project implements an AI-powered agent to analyze MoEngage's public documentation articles and suggest actionable improvements. The goal is to improve readability, structure, completeness, and adherence to style guidelines using Large Language Models (LLMs) and web content scraping.

Features
Documentation Analyzer Agent
Analyzes a given MoEngage documentation URL and generates a structured report with suggestions for:
-Readability (e.g., sentence complexity, jargon)
-Structure and flow (headings, paragraph length, navigation)
-Completeness and examples (clarity and sufficiency of content)
-Style guideline adherence (clarity, tone, action-oriented language)

(Bonus) Documentation Revision Agent
Incorporates some suggestions automatically to revise the original documentation content.

Technologies Used:
Python 3.x
Requests and BeautifulSoup (for web scraping)
OpenAI API (for LLM usage)
JSON and Markdown (for report generation)

## Setup and Installation

1. Clone the repository:
   git clone https://github.com/keerthireddy78/MoEngage

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set your OpenAI API key as an environment variable:

   ```bash
   export OPENAI_API_KEY="your_openai_api_key_here"
   ```

---

## Usage

### Run the Documentation Analyzer Agent

```bash
python run.py --url "https://help.moengage.com/hc/en-us/articles/your-article-id"
```

This will generate a structured report with suggestions on readability, structure, completeness, and style.

Run the Documentation Revision Agent

Currently, partial implementation is provided for automatic content revision based on analyzer suggestions.

File Structure

* `scraper.py` — Fetches and parses the article HTML content from the URL.
* `analyzer.py` — Contains logic to analyze the article and generate improvement suggestions using LLM.
* `revision_agent.py` — (Bonus) Attempts to revise the documentation based on suggestions.
* `run.py` — Entry point script to run the agents.
* `requirements.txt` — Python dependencies.
* `README.md` — This file.

---

## Design Choices and Approach

* **LLM Usage:** Used OpenAI’s GPT models to assess readability and style, as well as generate detailed suggestions.
* **Readability:** Applied standard readability metrics and combined with LLM explanations tailored to non-technical marketers.
* **Style Guidelines:** Simplified Microsoft Style Guide principles focusing on clarity, tone, and actionability.
* **Parsing:** Used BeautifulSoup for reliable HTML parsing and extraction of headings, paragraphs, and lists.

---

## Challenges

* Balancing automated content revision complexity with time constraints.
* Handling diverse documentation styles and structures robustly.
* Generating meaningful, actionable feedback rather than generic comments.

---

## Future Improvements

* Fully implement the revision agent for more automated improvements.
* Add UI or API endpoints for easier integration.
* Extend style guideline checks with customizable rule sets.
* Support more documentation sources beyond MoEngage.
