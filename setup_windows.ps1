# Snapdragon demo setup (Windows ARM64 PowerShell)

# 1) Install GenieX using the official Qualcomm distribution.
# 2) Open a new terminal after installation.
geniex pull ai-hub-models/Qwen3-4B-Instruct-2507
geniex serve

# In another terminal:
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app\main.py
