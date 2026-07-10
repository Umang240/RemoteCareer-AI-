# API Documentation

## Base URL

```text
http://127.0.0.1:8000
```

## Health Check

### Endpoint

```http
GET /
```

### Success Response

```json
{
  "message": "CareerGPT backend server is running"
}
```

---

# Authentication APIs

## User Signup

Register a new user account.

### Endpoint

```http
POST /auth/signup
```

### Request Body

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securePassword123"
}
```

### Success Response

```json
{
  "message": "User registered successfully"
}
```

### Error Response

```json
{
  "message": "Email already exists"
}
```

### Notes

* Password must be between 8-72 characters
* Email must be a valid email format

---

## User Login

Authenticate user with email and password.

### Endpoint

```http
POST /auth/login
```

### Request Body

```json
{
  "email": "john@example.com",
  "password": "securePassword123"
}
```

### Success Response

```json
{
  "message": "Login successful",
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Error Response

```json
{
  "message": "Invalid credentials"
}
```

---

# User Profile APIs

## Create Profile

Create a new user profile.

### Endpoint

```http
POST /create-profile
```

### Request Body

```json
{
  "name": "Umang Balodhi",
  "email": "umang@example.com",
  "education": "Online MCA",
  "skills": [
    "Python",
    "FastAPI",
    "MongoDB"
  ],
  "target_role": "AI Engineer"
}
```

### Success Response

```json
{
  "message": "Profile created successfully"
}
```

---

## Get All Profiles

Retrieve all user profiles.

### Endpoint

```http
GET /profiles
```

### Success Response

```json
[
  {
    "name": "Umang Balodhi",
    "email": "umang@example.com",
    "education": "Online MCA",
    "skills": [
      "Python",
      "FastAPI"
    ],
    "target_role": "AI Engineer"
  }
]
```

---

## Update Profile

Update an existing user profile.

### Endpoint

```http
PUT /update-profile/{id}
```

### Path Parameters

| Parameter | Type   | Description         |
| --------- | ------ | ------------------- |
| id        | string | MongoDB document ID |

### Request Body

```json
{
  "name": "Umang Balodhi",
  "email": "umang@example.com",
  "education": "Online MCA",
  "skills": [
    "Python",
    "FastAPI",
    "MongoDB",
    "Machine Learning"
  ],
  "target_role": "AI Engineer"
}
```

### Success Response

```json
{
  "message": "Profile updated successfully"
}
```

---

## Get Single Profile

Retrieve a specific user profile by ID.

### Endpoint

```http
GET /profiles/{id}
```

### Path Parameters

| Parameter | Type   | Description         |
| --------- | ------ | ------------------- |
| id        | string | MongoDB document ID |

### Success Response

```json
{
  "_id": "507f1f77bcf86cd799439011",
  "name": "Umang Balodhi",
  "email": "umang@example.com",
  "education": "Online MCA",
  "skills": [
    "Python",
    "FastAPI",
    "MongoDB"
  ],
  "target_role": "AI Engineer"
}
```

### Error Response

```json
{
  "detail": "Invalid profile id format"
}
```

or

```json
{
  "detail": "Profile not found"
}
```

---

## Delete Profile

Delete a user profile.

### Endpoint

```http
DELETE /delete-profile/{id}
```

### Path Parameters

| Parameter | Type   | Description         |
| --------- | ------ | ------------------- |
| id        | string | MongoDB document ID |

### Success Response

```json
{
  "message": "Profile deleted successfully"
}
```

### Error Response

```json
{
  "detail": "Profile not found"
}
```

---

# Career Assessment APIs

## Assess Career

Analyze user education, skills, and interests to recommend career roles.

### Endpoint

```http
POST /assessment/
```

### Request Body

```json
{
  "education": "Online MCA",
  "skills": [
    "Python",
    "SQL"
  ],
  "interests": [
    "AI",
    "Data Science"
  ]
}
```

### Success Response

```json
{
  "recommended_roles": [
    "AI Engineer",
    "Data Analyst"
  ]
}
```

### Notes

* Education must be a non-empty string
* Skills must be a non-empty list of strings
* Interests must be a non-empty list of strings

---

## Skill Gap Analysis

Compare current skills with target role requirements and identify missing skills.

### Endpoint

```http
POST /skill-gap/
```

### Request Body

```json
{
  "target_role": "AI Engineer",
  "current_skills": [
    "Python",
    "SQL"
  ]
}
```

### Success Response

```json
{
  "target_role": "AI Engineer",
  "missing_skills": [
    "Machine Learning",
    "Deep Learning",
    "PyTorch",
    "TensorFlow"
  ]
}
```

### Error Response

```json
{
  "error": "No skill data found for role: AI Engineer"
}
```

### Notes

* Target role must be a non-empty string
* Current skills must be a non-empty list of strings

---

# Career Mapping

The Career Assessment module currently uses a rule-based mapping system.

| Interest        | Recommended Role  |
| --------------- | ----------------- |
| AI              | AI Engineer       |
| Data Science    | Data Analyst      |
| Web Development | Backend Developer |
| Cybersecurity   | Security Analyst  |
| Cloud Computing | Cloud Engineer    |

---



## Learning Roadmap Generator

Generate a structured learning roadmap for a target career role.

### Endpoint

```http
POST /roadmap/
```

### Request Body

```json
{
  "target_role": "AI Engineer"
}
```

### Success Response

```json
{
  "target_role": "AI Engineer",
  "roadmap": [
    "Master Python fundamentals and data structures",
    "Learn Linear Algebra and Statistics",
    "Master Machine Learning algorithms (Supervised & Unsupervised)",
    "Deep Learning with TensorFlow/PyTorch",
    "Build portfolio projects (NLP, Computer Vision, RL)",
    "Learn cloud deployment (AWS, GCP, Azure)",
    "Practice system design and optimization",
    "Participate in Kaggle competitions",
    "Prepare for AI Engineer interviews",
    "Apply for AI Engineer positions"
  ]
}
```

### Error Response

```json
{
  "error": "No roadmap found for role: AI Engineer"
}
```

### Notes

* Target role must be a non-empty string
* Roadmap data is retrieved from the predefined roadmaps database

---

# AI Career Advisor

Generate personalized career guidance using Google Gemini AI based on education, current skills, and target role.

### Endpoint

```http
POST /career-advice/
```

### Request Body

```json
{
  "education": "Online MCA",
  "skills": ["Python", "FastAPI", "MongoDB"],
  "target_role": "AI Engineer"
}
```

### Success Response

```json
{
  "career_advice": "With your FastAPI and MongoDB background, you have a strong foundation for building AI applications. Focus on machine learning fundamentals and cloud deployment to bridge the gap to AI Engineering roles.",
  "next_skills": [
    "Machine Learning",
    "Deep Learning with PyTorch",
    "TensorFlow",
    "Docker & Kubernetes",
    "Cloud Deployment (AWS/GCP)"
  ],
  "recommended_projects": [
    "Build a FastAPI-based AI recommendation system",
    "Deploy a machine learning model on cloud using Docker",
    "Create an NLP chatbot application",
    "Develop a computer vision project",
    "Build end-to-end ML pipeline with monitoring"
  ],
  "interview_tips": [
    "Be prepared to discuss your machine learning projects in detail",
    "Understand the mathematical foundations of ML algorithms",
    "Practice system design questions for scalable ML systems",
    "Have examples of handling real-world datasets",
    "Demonstrate knowledge of deployment and MLOps practices"
  ]
}
```

### Error Response

```json
{
  "error": "Failed to generate career advice"
}
```

### Notes

* Requires a valid Gemini API key configured in the environment as `GEMINI_API_KEY`
* Uses Google's Gemini 2.5 Flash model for generating personalized guidance
* Education must be a non-empty string
* Skills must be a non-empty list of strings
* Target role must be a non-empty string
* Response includes structured career guidance with actionable recommendations

---

# Status

### Completed

* ✅ User Profile CRUD APIs (Create, Read, Get All, Update, Delete)
* ✅ Authentication APIs (Signup, Login)
* ✅ Career Assessment API
* ✅ Skill Gap Analysis API
* ✅ Learning Roadmap Generator API
* ✅ AI Career Advisor API (Gemini Integration)
* ✅ MongoDB Integration
* ✅ FastAPI Backend Setup
* ✅ JWT Token-based Authentication
* ✅ Input Validation with Pydantic Models

### Planned

* Frontend Dashboard with React
* Advanced Role Matching Algorithm
* Real-time Collaboration Features
* Progress Tracking Dashboard
* Recommendation Engine Enhancements
