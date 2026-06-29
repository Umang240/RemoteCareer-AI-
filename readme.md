# RemoteCareer AI

RemoteCareer AI is an AI-powered career guidance platform designed specifically for online and distance education students. The platform helps learners discover suitable career paths, assess their current skills, identify skill gaps, and receive personalized guidance for career growth.

## Problem Statement

Students pursuing online and distance education often have limited access to career counseling, placement support, and mentorship opportunities available to traditional on-campus students. RemoteCareer AI aims to bridge this gap through AI-powered career guidance and structured career development tools.

## Features

### Implemented

* User Profile Management

  * Create Profile
  * View Profiles
  * Update Profile
  * Delete Profile

* Career Assessment

  * Analyze user interests and skills
  * Recommend suitable career roles

* Skill Gap Analysis

  * Compare current skills with target roles
  * Identify missing role-specific skills

* Learning Roadmap Generator

  * Generate personalized learning paths
  * Recommend learning milestones for career goals

* AI-Powered Career Advisor

  * Generate personalized career guidance with Gemini
  * Suggest next skills to learn
  * Recommend projects to build
  * Provide interview preparation tips

### Planned

* Portfolio Project Recommendations
* Interview Preparation Assistant
* Frontend Dashboard

## Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn

### Database

* MongoDB Atlas

### Validation

* Pydantic v2

### AI Integration

* Google Gemini API for career advice generation

### Frontend (Planned)

* React.js
* Tailwind CSS

## Project Structure

```text
RemoteCareer-AI/
│
├── backend/
│   ├── app/
│   │   ├── database/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── docs/
│   └── project_overview.md
│
└── README.md
```

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd RemoteCareer-AI
```

### Create Virtual Environment

```bash
cd backend
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
MONGODB_URL=your_mongodb_connection_string
DATABASE_NAME=remotecareer_ai
GEMINI_API_KEY=your_gemini_api_key
```

### Run Server

```bash
uvicorn app.main:app --reload
```

### API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

## Development Roadmap

### Phase 1

* FastAPI Setup
* MongoDB Integration
* User Profile CRUD
* Career Assessment
* Skill Gap Analysis

### Phase 2

* Learning Roadmap Generator

### Phase 3

* Gemini-Based Career Advice
* Personalized Career Guidance

### Phase 4

* React Frontend
* Deployment

## License

This project is developed for educational and portfolio purposes.
