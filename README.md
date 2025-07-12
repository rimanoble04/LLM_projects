# Project Fetching: Agentic AI Final Year Ideas

This project demonstrates how to gather and refine final year project ideas in the field of **Agentic AI** using multiple LLMs, and then generate a clean, organized PDF summary with an audio overview via **NotebookLM**.

## Objective

Provide **innovative, technically challenging** project ideas for computer science students in Agentic AI, not easily solvable with no-code tools like Zapier or n8n.

## Process Overview

1. **Prompt Sent to Multiple LLMs**  
   A common prompt was sent to the following language models:
   - **Google Gemini (1.5 Flash)**
   - **Groq (LLaMA 3-70B)**
   - **Cohere (Command R+)**

2. **Content Aggregation**  
   - The responses from all three models were written to a `.txt` file.
   - A follow-up prompt was used to reorganize and clean the raw responses into a numbered list including:
     - Project Title
     - Description
     - Applications
     - Challenges

3. **PDF Generation**  
   The cleaned response was converted to a professional PDF using `FPDF`.

4. **Audio Overview (NotebookLM)**  
   The final PDF was uploaded to **NotebookLM**, which generated a structured **audio overview** via its **Deep Dive** feature, summarizing the project ideas in relation to AI agents.

## 🔊 Final Output

🎧 **[Listen to the Audio Overview](https://notebooklm.google.com/notebook/03d59303-3638-4270-a8a0-f3511bc81fe9/audio)** (via NotebookLM)

## Tech Stack

- `Python`
- `google.generativeai`
- `cohere`
- `groq`
- `fpdf`
- `dotenv`
- `NotebookLM` (manual upload for audio generation)

## 📎 Output Files

- `project_ideas.txt` — Raw output from all models  
- `project_ideas_cleaned.txt` — Organized project list  
- `project_ideas.pdf` — Final formatted version  
- **NotebookLM Audio** — Summary of all ideas

---

Feel free to explore the repo and try it yourself!
