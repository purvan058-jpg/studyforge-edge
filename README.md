# StudyForge Edge — Private On-Device Study Copilot

A Snapdragon-optimized study assistant designed to keep student material on-device.

## Why it fits the Snapdragon AI Lab challenge
- Uses a Qualcomm AI Hub model through GenieX.
- Designed for Windows on Snapdragon and local NPU inference.
- No cloud LLM is required for core generation.
- Converts lecture notes into summaries, flashcards, quizzes, and a revision plan.
- Privacy-first: source material stays on the laptop.

## Core stack
- Python + Streamlit
- PyMuPDF for PDF extraction
- Qualcomm GenieX local OpenAI-compatible server
- Recommended model: `ai-hub-models/Qwen3-4B-Instruct-2507`
- Target: Snapdragon X Elite / X2 Elite Windows ARM64

Qualcomm AI Hub currently documents Qwen3 models for Snapdragon compute and GenieX provides a local OpenAI-compatible endpoint.

## Run
1. Install Windows ARM64 GenieX.
2. Pull the model:
   `geniex pull ai-hub-models/Qwen3-4B-Instruct-2507`
3. Start the local server:
   `geniex serve`
4. In a Python environment:
   `pip install -r requirements.txt`
5. Run:
   `streamlit run app/main.py`

Open the local Streamlit URL shown in the terminal.

## Demo flow
1. Upload a lecture PDF.
2. Click "Analyze".
3. Generate a concise summary.
4. Generate 5 exam-style questions.
5. Generate a 3-day revision plan.
6. Explain one selected concept using the local model.

## Important
This repository is a competition-ready learning prototype/template. Before any real submission, test the complete flow on the exact Snapdragon laptop and document actual latency, memory use, and NPU execution. Do not claim benchmark numbers that were not measured.

## Eligibility
The Snapdragon AI Lab challenge shown in the accompanying submission screenshots has an age eligibility requirement. This package is for learning/prototyping unless the participant independently meets all official eligibility rules.
