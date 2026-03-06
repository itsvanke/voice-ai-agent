# Real-Time Multilingual Voice AI Agent

This project implements a Real-Time Voice AI Agent that can interact with patients and manage clinical appointments automatically.

The system processes user speech, understands the request using an AI model, performs appointment operations, and returns a response.

The agent supports:

* Appointment booking
* Appointment rescheduling
* Appointment cancellation
* Doctor availability checking
* Multilingual conversations

The system demonstrates a **complete AI voice pipeline**, including speech recognition, language detection, AI reasoning, tool orchestration, and scheduling logic.

## Features

* Real-time conversational AI agent
* Multilingual support (English, Hindi, Tamil)
* Voice-to-text processing
* AI intent detection using LLM
* Appointment scheduling engine
* Conflict detection and alternative suggestions
* Session and persistent memory
* Low latency architecture
* Modular backend architecture


## System Architecture

User Speech
     ↓
Speech-to-Text (Whisper)
     ↓
Language Detection
     ↓
AI Agent (LLM Reasoning)
     ↓
Tool Orchestration
     ↓
Appointment Scheduling Engine
     ↓
Text Response
     ↓
Text-to-Speech
     ↓
Audio Response


## Project Structure

voice-ai-agent
│
├── backend
│   ├── api
│   ├── controllers
│   └── routes
│
├── agent
│   ├── prompt
│   ├── reasoning
│   └── tools
│
├── services
│   ├── speech_to_text
│   ├── text_to_speech
│   └── language_detection
│
├── memory
│   ├── session_memory
│   └── persistent_memory
│
├── scheduler
│   └── appointment_engine
│
└── requirements.txt

## Technologies Used

* Python
* FastAPI
* WebSockets
* Whisper (Speech-to-Text)
* OpenAI LLM
* Redis (memory storage)
* PJSON store


## Installation

Clone the repository:

git clone https://github.com/itsvanke/voice-ai-agent.git
cd voice-ai-agent

Install dependencies:


pip install -r requirements.txt

Set your OpenAI API key:

export OPENAI_API_KEY=your_api_key
Run the Server

Start the backend service:

python -m uvicorn backend.api.main:app --reload

Server will start at:

http://127.0.0.1:8000
Example Interaction

User:

Book appointment with cardiologist tomorrow

Agent Response:

Available slots are 10 AM and 2 PM. Which time would you prefer?

User:

10 AM

Agent:

Your appointment with the cardiologist has been successfully booked for tomorrow at 10 AM.
Evaluation Criteria Addressed

This project demonstrates:

Real-time system architecture

AI agent reasoning

Tool orchestration

Memory design

Scheduling logic

Multilingual capability

Low-latency processing

Future Improvements

Real-time streaming voice interaction

Cloud deployment

Horizontal scaling

Automated reminder campaigns

Integration with hospital databases

Author

Venkatesh Gowda

Software Engineer | AI Systems Developmen
