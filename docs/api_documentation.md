# API Documentation

## Base URL

```text
http://127.0.0.1:8000
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

---

# Career Assessment APIs

## Assess Career

Analyze user interests and skills to recommend career roles.

### Endpoint

```http
POST /assessment
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

---

## Skill Gap Analysis

Compare current skills with target role requirements.

### Endpoint

```http
POST /skill-gap
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
    "Deep Learning"
  ]
}
```

### Error Response

```json
{
  "error": "No skill data found for role: AI Engineer"
}
```

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

# Future APIs

The following APIs are planned for future development.

## Learning Roadmap Generator

### Endpoint

```http
POST /roadmap
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
    "Learn Python Fundamentals",
    "Learn Machine Learning",
    "Build AI Projects",
    "Create Portfolio",
    "Apply for Internships"
  ]
}
```

### Error Response

```json
{
  "error": "No roadmap found for role: AI Engineer"
}
```

---

## AI Career Advisor

```http
POST /career-advice
```

Purpose:

* Generate personalized career guidance using Google Gemini.

---

# Status

### Completed

* User Profile CRUD APIs
* Career Assessment API
* Skill Gap Analysis API
* Learning Roadmap Generator API
* MongoDB Integration
* FastAPI Backend Setup

### Planned

* Gemini Integration
* Frontend Dashboard

