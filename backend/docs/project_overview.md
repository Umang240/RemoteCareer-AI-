# RemoteCareer AI

## Overview

RemoteCareer AI is an AI-powered career guidance platform built with FastAPI and MongoDB to support online and distance education students in making informed career decisions. The platform helps learners identify suitable career paths, assess their skills, and receive personalized guidance for professional growth.

## Project Vision

Online and distance education students often lack access to structured career counseling and placement support available to traditional on-campus students. RemoteCareer AI aims to bridge this gap through personalized career recommendations and AI-driven guidance.

### Core Objectives

* Career assessment based on skills and interests
* Skill gap identification for target roles
* Personalized learning roadmaps
* Portfolio project recommendations
* AI-powered career guidance
* Interview preparation support

## Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn

### Database

* MongoDB Atlas

### Validation

* Pydantic v2

### AI Integration (Planned)

* Google Gemini API

### Frontend (Planned)

* React.js
* Tailwind CSS

## Features Implemented

### User Profile Management

#### Create Profile

`POST /create-profile`

Create a user profile containing:

* Name
* Email
* Education
* Skills
* Target Career Role

#### Get Profiles

`GET /profiles`

Retrieve all user profiles.

#### Update Profile

`PUT /update-profile/{id}`

Update an existing profile.

#### Delete Profile

`DELETE /delete-profile/{id}`

Delete a profile by ID.

### Career Assessment

#### Assess Career

`POST /assessment`

Analyze user interests and skills to recommend suitable career paths.

Example:

Input:

```json
{
  "education": "Online MCA",
  "skills": ["Python", "SQL"],
  "interests": ["AI", "Data Science"]
}
```

Output:

```json
{
  "recommended_roles": [
    "AI Engineer",
    "Data Analyst"
  ]
}
```

## Project Architecture

```text
Frontend (React + Tailwind)
            |
            v
      FastAPI Backend
            |
     ----------------
     |              |
     v              v
MongoDB Atlas   Gemini API
```

## Current Development Status

### Completed

* FastAPI project setup
* MongoDB Atlas integration
* User Profile CRUD APIs
* Career Assessment API
* Career-role mapping logic
* Request validation using Pydantic

### Planned

* Skill Gap Analysis Module
* Learning Roadmap Generator
* Gemini-powered Career Advisor
* Frontend Dashboard
* API Documentation
* Improved Error Handling
* Deployment

## Development Roadmap

### Phase 1 (MVP)

* User Profile Management
* Career Assessment
* Skill Gap Analysis
* Learning Roadmap Generator

### Phase 2

* Gemini Integration
* Personalized Career Advice
* Project Recommendations

### Phase 3

* React Frontend
* Dashboard and Analytics
* Deployment

```
```
