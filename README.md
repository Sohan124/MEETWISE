# 🤖 MeetWise – AI Meeting Insights & Task Automation Agent

MeetWise is an AI-powered assistant that reads meeting transcripts, summarizes key discussion points, and assigns personalized action items to each participant — completely autonomously.

This project was built as part of the **Mini Hackathon** under the **AI Agents Workshop**.

---

## 📌 Features

- 🧠 Summarizes meeting transcripts using **Azure OpenAI GPT-4o**
- ✅ Detects and assigns tasks to respective speakers
- 🗂 Outputs structured summary + to-do list
- 💬 Console-based interface (simple, fast, lightweight)
- 🌐 Built with Azure OpenAI, Python, and dotenv

---

## 🖥️ Demo Video

🎥 [Watch the YouTube demo here](YOUR_VIDEO_LINK_HERE)

---

## 🧪 How It Works

### 🔹 Input:
A text file (`transcript.txt`) with content like:
John: We need to deploy the backend by Friday.
Sara: I will test all modules by Wednesday.
Mike: I will fix the UI bugs.

### 🔹 Output:
GPT-4o generates a summary and a task list like:

Summary:
Team discussed deployment, testing, and UI fixes.
Tasks:
John: Deploy backend by Friday
Sara: Test all modules by Wednesday
Mike: Fix UI bugs


---

## ⚙️ Tech Stack

- Python 3.10
- Azure OpenAI GPT-4o (via ChatCompletion API)
- `python-dotenv` for managing secrets

---
1. Install dependencies
2. Setup .env file
3. Add your meeting transcript
4. Run the app

Folder Structure :
meetwise :-
├── .env
├── meetwise.py
├── transcript.txt
├── README.md
└── requirements.txt

Future Scope
Integrate with Google Calendar or Notion for auto-task creation
Build a UI using Streamlit
Add Whisper integration for audio transcripts
Support for multilingual transcripts
Meeting analytics dashboard


Built By
Sohansingh
LinkedIn Profile
🔗 Hackathon Project – AI Agents Workshop (2025)
